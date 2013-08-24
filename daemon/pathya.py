#!/usr/bin/env python3.3
###############################################################################
# Copyright © 2012-Now, SVAKSHA (https://github.com/svaksha) AllRightsReserved.
# License: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>
# All copies must retain this Copyright notice and this permission notice.
###############################################################################

import glob, sys
import os, os.path

images_list = ['P1010214.png',
              'P1010218.png',
              'P1010221.png',
              ];

def dirPath():
    '''
    build path for parameter file
    '''
    full_path = os.path.realpath(__file__)
    dirpath, prog_file = os.path.split(full_path)
    return dirpath


def imagePath(dir_path, count):
    image_dir = images_list[count]
    image_filepath = os.path.join(dir_path, image_dir)
    print (image_filepath)
    return image_filepath
