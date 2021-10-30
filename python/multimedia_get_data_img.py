#!/usr/bin/env python3

###############################################
# Author: AISK11                              #
# Description: this snippet returns data from #
# image.                                      #
###############################################

## Useful documentation:
## https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html

## Dependency libraries:
import sys
import os

###############################################
# Add Pillow library from external directory: #
###############################################
# Linux: doas pip install --force-reinstall --prefix "${HOME}" Pillow
# Linux: doas chown -R $(whoami):$(whoami) "${HOME}/lib/"

## Pillow library from external directory:
#HOME_DIR = os.environ['HOME'] + '/' ## e.g. '/home/user1/'
#lib_path = HOME_DIR + 'python3/lib/python3.9/site-packages/'
#sys.path.append(lib_path)
###############################################

## Library for handling images:
from PIL import Image

def multimedia_get_data_img(img_input):

    ## Open image (identifies from file content):
    img = Image.open(img_input)

    ## Get image data:
    img_data = {
        ## 'img01.jpg'
        "img_filename": img.filename,
        ## 'JPEG'
        "img_format": img.format,
        ## 'RGB'
        "img_mode": img.mode,
        ## 1920
        "img_width": img.width,
        ## 1080
        "img_height": img.height,
        ## False
        "img_is_animated": getattr(img, "is_animated", False),
        ## 1
        "img_n_frames": getattr(img, "n_frames", 1)
    }

    return img_data


## USAGE:
# img_data = multimedia_get_data_img("img01.jpeg")
