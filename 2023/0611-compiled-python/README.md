# Compiled Python
In [this video](https://youtu.be/umLZphwA-dw) we show that just-in-time and ahead-of-time compiled Python can reach C++-level speeds.

## Setup

```sh
mamba env create -f environment.yml
```

## Usage
To run all of the benchmarks, run
```sh
./benchmark
```

To generate the Julia set visualization, run
```sh
python juliaset.py
```

To approximate the pi with Taichi, run,
```sh
python taichi_pi.py
```
