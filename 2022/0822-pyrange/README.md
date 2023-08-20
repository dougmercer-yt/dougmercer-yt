# pyrange
In [this video](https://youtu.be/LRIUg089W2c) we implement the `range()` object in pure Python.

## Setup
I use `mamba` for setting up my virtual environments. If you have `mamba` installed, run

```sh
mamba env create -f environment.yml
```

## Usage
To run all of the unit tests, run

```sh
pytest
```

To run the various timing tests, run

```sh
python time_contains.py
python time_iter.py
python time_mixins.py
```
