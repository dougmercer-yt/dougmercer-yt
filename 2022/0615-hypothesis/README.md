# property testing

Code from https://youtu.be/xBhUzShDv8k.

There really isn't much code in this video! If you want me to add something to this repository from the video, please feel free to submit an issue.

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
