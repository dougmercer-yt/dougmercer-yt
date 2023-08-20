# TorToiSe

In [this video](https://youtu.be/Bbg-dPLTUhE), we use the TorToiSe text-to-speech library to emulate the voices of popular content creators using less than a minute of sample audio.

For this video, I mostly just adapted the Google Colab provided by the repository author, [available here](https://colab.research.google.com/github/neonbjb/tortoise-tts/blob/main/tortoise_tts.ipynb).

Note: If there is particular info you want on this video, please feel free to create an issue and I'll update this README or add additional code examples.

## Tips

### Mounting Google Drive
In this video, I stored my voice samples on Google Drive.

You can mount Google Drive to a Colab notebook using,
```python
from google.colab import drive
drive.mount('/content/drive')
```

Then, you can copy your files from your Google Drive to your local Colab session by running the following in a Colab notebook cell,

```
! cp -n -r /content/drive/MyDrive/voices/* tortoise/voices/
```

Here, I copied my sample voices from the top-level `voices/` directory in my Google Drive to `voices/` subfolder of my locally cloned `tortoise` repository.
