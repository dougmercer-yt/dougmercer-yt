# Doug Mercer YouTube

## Contents
This repository contains the example code demonstrated in my YouTube videos.

Directories in this repository are organized by year, beginning with 2022. Within each year, each subfolder contains the code for a particular video. Video directories begin with the video's release date (in `mmdd` format) followed by the video's working title.

## Setup
If you just want to browse the code, feel free to click around and view the code in Github's WebApp.

To clone the repository,
1. Install Git on your local device.
2. Authenticate to Github. I generally recommend using SSH. You can find more info about authenticating using SSH [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
3. Run `git clone git@github.com:dougmercer-yt/dougmercer-yt.git`

After, you'll have cloned this repository into the `dougmercer-yt` folder within your current directory.

Now that you've cloned the repository, you might want to run it. I use `conda`/`mamba` to manage my virtual environments. I generally find `mambaforge` to be fast and easy to install and use. You can find your platform-specific installer for `mambaforge` [here](https://github.com/conda-forge/miniforge#mambaforge). Alternatively, if you are a Mac user, [you can install it via `brew`](https://formulae.brew.sh/cask/mambaforge)

Once you've installed `mamba`, you should be able to `cd` to the directory containing the code you want to test. You can follow the instructions for getting setup in the video-specific README. However, in general, these instructions will simply be,
```sh
mamba env create -f environment.yml
```

This command creates a `conda` environment specified by the contents of the `environment.yml` file in your current directory.

After, you should be able to `activate` the newly created environment by following the instructions printed at the end of the `env create` output. Generally, this is will direct you to run,
```sh
mamba activate $ENV_NAME  # where ENV_NAME isn't a real variable, but whatever the output says for the specific video
```

## FAQ

### How do I get an updated versions of this code?

Assuming you have a clean working directory,

```sh
git pull
```

### Some code from a video is missing-- can you add it?

Maybe! If you create an issue describing what code you want added, I'll do my best to add it.

### Why is this repo a monorepo?
This was originally set up as a Github Sponsors benefit. Github Sponsors only allows automatically granting access to one repository per "tier". In order to grant access to all video's code, rather than just one, I decided to organize this repository as a monorepo. But now, the repo is openly available so... `¯\_(ツ)_/¯`.
