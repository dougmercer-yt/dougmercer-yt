# Prefect
In [this video](https://youtu.be/Kt8GAZRpTcE) we use Prefect to schedule a Python script to run every week.

By making just a few changes to our code, we can:
- Schedule our Python Script to run on local or remote systems
- Handle Errors with Retries
- Monitor our workflows in an incredibly powerful web-based UI
- Parallelize and scale our code's using on-prem compute clusters or Cloud platforms
- Persist Python results and Markdown reports
- and more...

## Setup

```sh
mamba env create -f environment.yml
```

## Usage

To run the before/after versions of the code,
```sh
python original.py  # probably won't succeed!
python pipeline.py
```
