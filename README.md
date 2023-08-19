# Doug Mercer YouTube

## Thank you =]

Thanks for sponsoring the channel! Your contribution helps support the production of educational programming content on YouTube.

## Contents
This repository contains the code used in my YouTube videos.

At the top level, I break up the videos by year, beginning with 2022 and up to the current year. After, each subfolder within a year corresponds to a video, with the first four digits indicating the publish date of the video in `mmdd` format, followed by a few words describing the topic of the video.

## Setup
If you just want to browse the code, feel free to click around and view the code in Github's WebApp browser.

That said, there are at least two good reasons why I recommend cloning a copy this repository:
1. If you want to run or modify the code, you'll need a local copy of it.
1. If you cancel your sponsorship, you'll no longer have access to this page. So, if you clone it, you'll at least have a local copy of everything!

To clone the repository,
1. Install Git on your local device.
2. Authenticate to Github. I generally recommend using SSH. You can find more info about authenticating using SSH [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
3. Run `git clone git@github.com:dougmercer-yt/dougmercer-yt.git`

After, you'll have cloned the `dougmercer-yt` repository into the `dougmercer-yt` folder within your current directory.

Now that you've cloned the code, you might want to run it. I use `conda`/`mamba` to manage my virtual environments. You can find instructions for installing `mamba` on your platform [here](https://github.com/conda-forge/miniforge#mambaforge).

Once you've installed `mamba`, you should be able to `cd` to the directory containing the video whose code you want to test. After, you can follow the instructions for getting setup for that particular video's codebase in the `README.md` within that directory. However, in general, the setup will typically tell you to run the following command,

```sh
mamba env create -f environment.yml
```

This command creates a `conda` environment specified by the contents of the `environment.yml` file in your current directory.

After, you should be able to `activate` the newly created environment by following the instructions output at the end of the `env create` command. Generally, this is
```sh
mamba activate $ENV_NAME  # whatever it is for the specific video
```

## FAQ

### How do I get an updated versions of this code?

Assuming you have a clean working directory,

```sh
git pull
```

### Why is this repo a monorepo?
I'd rather it not be, but Github Sponsors currently only allows me to grant access to one repository per "tier". In order to grant access to all video's code, rather than just one, I needed to organize the repository as a monorepo `¯\_(ツ)_/¯`.

### What is the license for all this code?
I'm still in the process of figuring out what license is appropriate. In the meantime:
1. You are welcome to use snippets of any code in this repository as you wish...
2. ... however, I ask that you not share or reupload this repository in its entirety.

Restricting the redistribution of this code raises money for my YouTube channel, and helps me make more videos or purchase equipment, software, assets, or subscriptions that improve the quality of my videos. I hope that one day the channel will be profitable enough to freely distribute this code, but in the meantime thank you for supporting this channel!
