#!/usr/bin/env python3.3
###########################################################################
# COPYRIGHT © 2012. SVAKSHA, <https://github.com/svaksha>, AllRightsReserved.
# LICENSE: AGPLv3 LICENSE <http://www.gnu.org/licenses/agpl.html>
# All copies must retain this Copyright notice and this permission notice.
###########################################################################

import glob, sys
import os, os.path

images_list = ['/P1010214.png',
              '/P1010218.png',
              '/P1010221.png',
              ];

def dirPath():
    '''
    build path for parameter file
    '''
    full_path = os.path.realpath(__file__)
    dirpath, prog_file = os.path.split(full_path)
return dirpath

def imagePath(dir_path, count):    # my decorator wrapper
        image_dir = 'images' +  count
        image_filepath = os.path.join(dir_path, image_dir)
        print (image_filepath)
return image_filepath



def fullPath(fn):
     '''
     build path for parameter file
     '''
     full_path = os.path.realpath(__file__)
     dirpath, prog_file = os.path.split(full_path)

     def wrap_fullPath():    # my decorator wrapper
         image_dir = '/images'

         param_file = os.path.join(dirpath, image_dir, image)
     return wrap_fullPath

#==============================================================================
# @filePath
# @fullPath
#==============================================================================

