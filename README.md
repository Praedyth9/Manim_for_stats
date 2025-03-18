# Manim for statistics

![logo](https://github.com/Praedyth9/manim_3b1b/raw/master/logo/cropped.png)

[![Build Status](https://travis-ci.org/3b1b/manim.svg?branch=master)](https://travis-ci.org/3b1b/manim)
[![Documentation](https://img.shields.io/badge/docs-EulerTour-blue.svg)](https://www.eulertour.com/docs)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
[![Manim Subreddit](https://img.shields.io/reddit/subreddit-subscribers/manim.svg?color=ff4301&label=reddit)](https://www.reddit.com/r/manim/)
[![Manim Discord](https://img.shields.io/discord/581738731934056449.svg?label=discord)](https://discord.gg/mMRrZQW)

The main goal of this repository is to provide python scripts to generate short animations using the manim library, as seen in the videos at [3Blue1Brown](https://www.3blue1brown.com/).
The script was tested on the community maintained version of Manim at https://github.com/ManimCommunity/manim/.
To get help or to join the development effort, please join the [discord](https://discord.gg/mMRrZQW).

## Installation
Manim runs on Python 3.7. You can install it from PyPI via pip:

```sh
pip3 install manimlib
```

System requirements are [cairo](https://www.cairographics.org), [ffmpeg](https://www.ffmpeg.org), [sox](http://sox.sourceforge.net), [latex](https://www.latex-project.org) (optional, if you want to use LaTeX).

You can now use it via the `manim` command. For example:

```sh
manim my_project.py MyScene
```

For more options, take a look at the [Using manim](#using-manim) sections further below.

### Directly

If you want to hack on manimlib itself, clone this repository and in that directory execute:

```sh
# Install python requirements
python3 -m pip install -r requirements.txt

# Try it out
python3 ./manim.py example_scenes.py SquareToCircle -pl
```

### Directly (Windows)
1. [Install FFmpeg](https://www.wikihow.com/Install-FFmpeg-on-Windows).
2. [Install Cairo](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo). For most users, ``pycairo‑1.18.0‑cp37‑cp37m‑win32.whl`` will do fine.
    ```sh
    pip3 install C:\path\to\wheel\pycairo‑1.18.0‑cp37‑cp37m‑win32.whl
    ```
3. Install a LaTeX distribution. [MiKTeX](https://miktex.org/download) is recommended.

4. [Install SoX](https://sourceforge.net/projects/sox/files/sox/).

5. Install the remaining Python packages. Make sure that ``pycairo==1.17.1`` is changed to ``pycairo==1.18.0`` in requirements.txt.
    ```sh
    git clone https://github.com/3b1b/manim.git
    cd manim
    pip3 install -r requirements.txt
    python3 manim.py example_scenes.py SquareToCircle -pl
    ```


## Anaconda Install

* Install sox and latex as above. 
* Create a conda environment using `conda env create -f environment.yml`
* **WINDOWS ONLY** Install `pyreadline` via `pip install pyreadline`. 


### Using `virtualenv` and `virtualenvwrapper`
After installing `virtualenv` and `virtualenvwrapper`
```sh
git clone https://github.com/3b1b/manim.git
mkvirtualenv -a manim -r requirements.txt manim
python3 -m manim example_scenes.py SquareToCircle -pl
```

### Using Docker
Since it's a bit tricky to get all the dependencies set up just right, there is a Dockerfile and Compose file provided in this repo as well as [a premade image on Docker Hub](https://hub.docker.com/r/eulertour/manim/tags/). The Dockerfile contains instructions on how to build a manim image, while the Compose file contains instructions on how to run the image.

The prebuilt container image has manim repository included.
`INPUT_PATH` is where the container looks for scene files. You must set the `INPUT_PATH`
environment variable to the absolute path containing your scene file and the
`OUTPUT_PATH` environment variable to the directory where you want media to be written.

1. [Install Docker](https://docs.docker.com)
2. [Install Docker Compose](https://docs.docker.com/compose/install/)
3. Render an animation:
```sh
INPUT_PATH=/path/to/dir/containing/source/code \
OUTPUT_PATH=/path/to/output/ \
docker-compose run manim example_scenes.py SquareToCircle -l
```
The command needs to be run as root if your username is not in the docker group.

You can replace `example.scenes.py` with any relative path from your `INPUT_PATH`.

![docker diagram](./manim_docker_diagram.png)

After running the output will say files ready at `/tmp/output/`, which refers to path inside the container. Your `OUTPUT_PATH` is bind mounted to this `/tmp/output` so any changes made by the container to `/tmp/output` will be mirrored on your `OUTPUT_PATH`. `/media/` will be created in `OUTPUT_PATH`.

`-p` won't work as manim would look for video player in the container system, which it does not have.

The first time you execute the above command, Docker will pull the image from Docker Hub and cache it. Any subsequent runs until the image is evicted will use the cached image.
Note that the image doesn't have any development tools installed and can't preview animations. Its purpose is building and testing only.
 
## Running the scripts

Before running the scripts, please check if you have the needed dependancies installed by typing `pip list` in a command window. To run the script, type in the command window the following command while being in the same folder as the script :

```sh
python3 -m manim Script_name.py class_name
```

The last parameter of the previous command line isn't mandatory in the case the file does have only one single class. Some other flags can be added to the command :
* `p` is for previewing, meaning that the video will automatically open one the render is over 
* `l` is used for a faster rendering with a lower quality
* `-s` to skip to the end and just show the final frame.
* `-n <number>` to skip ahead to the `n`'th animation of a scene.
* `-f` to show the file in finder (for OSX).

Set `MEDIA_DIR` environment variable to specify where the image and animation files will be written. By default, it will create a `media` folder where your script is actually located.

## Contact

If you want me to program specific animations related to statistics, please open a request on GitHub (with the issue menu). 
If something else than statistics, please contact me on discord : praae 
