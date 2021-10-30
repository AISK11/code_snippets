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
HOME_DIR = os.environ['HOME'] + '/' ## e.g. '/home/user1/'
lib_path = HOME_DIR + 'python3/lib/python3.9/site-packages/'
sys.path.append(lib_path)
###############################################

## Library for handling images:
from PIL import Image


#################
#  ICON FORMATS #
#################
#########
#  ICO  #
#########
## size = (width, height); Supported options:
## [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
def multimedia_convert_img_to_ico(img_input, img_output=None, img_size=256):

    ## If 'img_output' was not set by user, use the same name as 'img_input', just change extension:
    if img_output == None:
        img_output = ''.join(img_input.split(".")[:-1])+".ico"

    ## Open image (identifies from file content):
    img = Image.open(img_input)

    ## Avoid unsupported resolution:
    if img_size <= 16:
        img_size = 16
    elif img_size <= 24:
        img_size = 24
    elif img_size <= 32:
        img_size = 32
    elif img_size <= 48:
        img_size = 48
    elif img_size <= 64:
        img_size = 64
    elif img_size <= 128:
        img_size = 128
    else:
        img_size = 256

    ## Save image (and converts based on the name extension):
    img.save(img_output, sizes=[(img_size, img_size)])


#########
# ICNS  #
#########
## size = (width, height); Supported options:
## [(16, 16), (32, 32), (48, 48), (128, 128), (256, 256), (512, 512)]
## scale = [1, 2]
def multimedia_convert_img_to_icns(img_input, img_output=None, img_size=512, img_scale=1):
    ## If 'img_output' was not set by user, use the same name as 'img_input', just change extension:
    if img_output == None:
        img_output = ''.join(img_input.split(".")[:-1])+".icns"

    ## Avoid unsupported resolution:
    if img_size <= 16:
        img_size = 16
    elif img_size <= 32:
        img_size = 32
    elif img_size <= 48:
        img_size = 48
    elif img_size <= 128:
        img_size = 128
    elif img_size <= 256:
        img_size = 256
    else:
        img_size = 512

    ## Avoid unsupported scale:
    if img_scale <= 1:
        img_scale = 1
    else:
        img_scale = 2

    ## Save image (and converts based on the name extension):
    img.save(img_output, sizes=[(img_size, img_size, img_scale)])





#########
#  BMP  #
#########
def multimedia_convert_img_to_bmp(img_input, img_output=None):

    ## If 'img_output' was not set by user, use the same name as 'img_input', just change extension:
    if img_output == None:
        img_output = ''.join(img_input.split(".")[:-1])+".bmp"

    ## Open image (identifies from file content):
    img = Image.open(img_input)

    ## Save image (and converts based on the name extension):
    img.save(img_output)



#########
#  JPG  #
#########
## quality = 0 - 100; Not recommended to go over 95.
## baseline = load line by live, progressive = gradually increase resolution.
def multimedia_convert_img_to_jpg(img_input, img_output=None, img_quality=95, img_progressive=False):

    ## If 'img_output' was not set by user, use the same name as 'img_input', just change extension:
    if img_output == None:
        img_output = ''.join(img_input.split(".")[:-1])+".jpg"

    ## Open image (identifies from file content):
    img = Image.open(img_input)

    ## Save image (and converts based on the name extension):
    img.save(img_output, quality=img_quality, optimize=True, progressive=img_progressive)


#########
#  PNG  #
#########
def multimedia_convert_img_to_png(img_input, img_output=None):

    ## If 'img_output' was not set by user, use the same name as 'img_input', just change extension:
    if img_output == None:
        img_output = ''.join(img_input.split(".")[:-1])+".png"

    ## Open image (identifies from file content):
    img = Image.open(img_input)

    ## Save image (and converts based on the name extension):
    img.save(img_output, optimize=True)


#########
# WEBP  #
#########
## For lossy: 0 gives smallest size, 100 gives largest.
## For lossless, 0 is fastest (larger), 100 is best compression.
def multimedia_convert_img_to_webp(img_input, img_output=None, img_quality=80, img_lossless=False):

    ## If 'img_output' was not set by user, use the same name as 'img_input', just change extension:
    if img_output == None:
        img_output = ''.join(img_input.split(".")[:-1])+".webp"

    ## Open image (identifies from file content):
    img = Image.open(img_input)

    ## Save image (and converts based on the name extension):
    img.save(img_output, quality=img_quality, lossless=img_lossless)




####################
## Usage Examples: #
####################
##########
#  ICO:  #
##########
## OUTPUT: 'img01.ico', 256x256:
#multimedia_convert_img_to_ico(HOME_DIR + "img01.jpg")
## OUTPUT: 'img02.ico', 256x256:
#multimedia_convert_img_to_ico(HOME_DIR + "img01.jpg", HOME_DIR + "img02.ico")
## OUTPUT: 'img01.ico', 16x16:
#multimedia_convert_img_to_ico(HOME_DIR + "img01.jpg", HOME_DIR + "img03.ico", -5)
##########
# ICNS:  #
##########


#multimedia_convert_img_to_icns(HOME_DIR + "img01.jpg", HOME_DIR + "img01.icns", 512, 2)

#multimedia_convert_img_to_bmp(HOME_DIR + "img01.jpg", HOME_DIR + "img01.bmp")
#multimedia_convert_img_to_jpg(HOME_DIR + "img01.png", HOME_DIR + "img01.jpg", 95, True)
#multimedia_convert_img_to_png(HOME_DIR + "img01.jpg", HOME_DIR + "img01.png")




