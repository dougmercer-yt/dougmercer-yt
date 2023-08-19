# whisper

Not a lot of code in this one! I'd recommend referring to the native documentation for directions on usage, but you might find the `environment.yml` I made helpful.

## Setup

```sh
mamba env create -f environment.yml
```

## Usage

### CLI

I've found myself using the command line interface more than the programmatic one.

```sh
whisper --model medium.en --language en --fp16 False path/to/clip.mp4
```

Here, I set the model to the best English-only model (`medium.en`), explicitly set the language to English (`en`), disabled 16bit floating point arithmetic (because my hardware does not support it) and then specified the path to my video.

If I wanted to work with a nonenglish video, I would use a one of the multilanguage models (i.e., whose name does not end with `.en`) and would either change the `--language` argument to the appropriate language or remove it entirely and allow the model to figure out what the primary language being spoken is from the first few seconds of the input clip. When working with a nonenglish clip, leaving the task blank will default to the `transcribe` task, which will use the native language for the transcribed audio. Alternatively, if you set `--task translate`, whisper will translate the transcription to English. **There is currently no option to translate into nonenglish language**.

If you want to dig into the other arguments available, you can run

```sh
whisper --help
```

### Python

Similarly, you can use the Python API by doing something like,

```python
model = whisper.load_model("base.en")
result = model.transcribe("path/to/clip.mp4", language="en")
```
