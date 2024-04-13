import pandas as pd
from prefect import flow, task, unmapped
from prefect.artifacts import create_table_artifact, create_markdown_artifact

import our_team

MODELS: dict[str, our_team.Model] = {
    "fast": our_team.FastModel(),
    "slow": our_team.SlowModel(),
    "buggy": our_team.BuggyModel(),
    "good": our_team.GoodModel(),
    "terrible": our_team.TerribleModel(),
}


@task(retries=42)
def get_data():
    return our_team.get_data()


@task(task_run_name="backtest-{model_name}")
def backtest(model_name: str, data: pd.DataFrame) -> pd.DataFrame:
    model = MODELS[model_name]
    preds = our_team.backtest(model, data)
    create_markdown_artifact(
        key=f"{model_name}-predictions",
        markdown=preds.to_markdown(),
    )
    return preds


@task
def run_metric(truth: pd.DataFrame, pred: pd.DataFrame) -> pd.DataFrame:
    return our_team.metric(truth, pred)


@task
def choose_best_model(metrics):
    best_model_name, _ = min(metrics.items(), key=lambda x: x[1])
    return best_model_name


@task
def run_model(model_name, data):
    return MODELS[model_name].fit(data).predict()


@flow
def run_pipeline() -> float:
    data = get_data()

    # Backtest models on recent data
    prediction_futures = backtest.map(MODELS.keys(), unmapped(data))
    predictions = {
        model_name: result
        for model_name, pred in zip(MODELS.keys(), prediction_futures)
        if not isinstance(result := pred.result(raise_on_failure=False), Exception)
    }

    # Compute metrics using backtested predictions
    metric_futures = run_metric.map(unmapped(data), predictions.values())
    metrics = {
        model_name: metric.result()
        for model_name, metric in zip(predictions.keys(), metric_futures)
    }

    # Make an artifact for the metrics table
    create_table_artifact(key="metrics", table=[metrics])

    # Choose the best performing model and predict next week's value.
    best_model_name = choose_best_model(metrics)
    next_week = run_model(best_model_name, data)

    # Make an artifact for next week's prediction
    create_table_artifact(key="next-week", table=[{best_model_name: next_week}])

    return next_week


if __name__ == "__main__":
    run_pipeline.serve(
        name="weekly-prediction",
        cron="0 0 * * MON",
        pause_on_shutdown=False,
    )
