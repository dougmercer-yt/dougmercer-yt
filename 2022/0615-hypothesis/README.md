# property testing
In [this video](https://youtu.be/xBhUzShDv8k) we show that property-based testing can help discover hard-to-find bugs.

Note: There's not much code in this video. If you came here looking for something in particular, please feel free to create an issue asking me to add it.

## Setup
```sh
mamba env create -f environment.yml
```

## Usage
If you run
```sh
pytest
```
you will see that `hypothesis` correctly detects the error in our sorting implementation.
