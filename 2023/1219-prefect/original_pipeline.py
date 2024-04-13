import pandas as pd

import our_team

MODELS: dict[str, our_team.Model] = {
    "fast": our_team.FastModel(),
    "slow": our_team.SlowModel(),
    "buggy": our_team.BuggyModel(),
    "good": our_team.GoodModel(),
    "terrible": our_team.TerribleModel(),
}

def get_data():
    return our_team.get_data()

def backtest(model_name, data):
    model = MODELS[model_name]
    preds = our_team.backtest(model, data)
    # Write predictions to file
    # TODO: Don't overwrite old files.
    pd.DataFrame(preds).to_markdown(f"out/{model_name}.md")
    return preds

def run_metric(truth: pd.DataFrame, pred: pd.DataFrame) -> pd.DataFrame:
    return our_team.metric(truth, pred)

def choose_best_model(metrics):
    best_model_name, _ = min(metrics.items(), key=lambda x: x[1])
    return best_model_name

def run_model(model_name, data):
    return MODELS[model_name].fit(data).predict()

def run_pipeline() -> float:
    # TODO: This fails sometimes. Just run it again if it does.
    data = get_data()

    # Backtest models on recent data
    # TODO: One model is buggy. If it acts up, drop it and run again.
    predictions = {
        model_name: backtest(model_name, data)
        for model_name in MODELS.keys()
    }

    # Compute metrics using backtested predictions
    metrics = {
        model_name: run_metric(data, pred)
        for model_name, pred in predictions.items()
    }

    # Write metrics report to file
    # TODO: Again, don't overwrite old files!
    pd.DataFrame.from_dict(metrics, orient="index").to_markdown("out/metrics.md")

    # Choose the best performing model and predict next week's value.
    best_model = choose_best_model(metrics)
    next_week = run_model(best_model, data)

    # Write next week's prediction to file
    # TODO: Seriously, stop overwriting the files!
    pd.DataFrame({best_model: [next_week]}).to_markdown("out/next_week.md")

    return next_week

if __name__ == "__main__":
    from pathlib import Path
    Path("out").mkdir(exist_ok=True)
    run_pipeline()
