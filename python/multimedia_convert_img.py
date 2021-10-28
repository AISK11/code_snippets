#!/usr/bin/env python3

###############################################
# Author: AISK11                              #
# Description: this snippet converts image to #
# other image type.                           #
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
#lib_path = HOME_DIR + 'lib/python3.9/site-packages/'
#sys.path.append(lib_path)
###############################################

## Library for handling images:
from PIL import Image


def multimedia_convert_img(img_input, img_output, img_quality=95):
    ## Open image (identifies from file content):
    img = Image.open(img_input)
    ## Save image (and converts based on the name extension):
    img.save(img_output, quality=img_quality)


multimedia_convert_img(HOME_DIR + "img01.jpg", HOME_DIR + "img01.png", 100) ## CHANGE THIS
