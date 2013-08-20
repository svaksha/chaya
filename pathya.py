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


def filePath(dirpath, file_name, fnprd, fnsfx):
    '''
    Construct filePath from inputs with a decorator function that expects
    ANOTHER function as parameter. Inside, the decorator defines a function
    on the fly: the wrapper. This function is going to be wrapped around the
    original function so it can execute code before and after it.
    '''
    file_name = os.path.abspath(dirpath, fnprd, fnsfx)
    def wrap_filePath():   # my decorator wrapper
        out_file_name = (file_name + fnprd + fnsfx)
        fnoutpath = os.path.join(dirpath, out_file_name)
        print ('running from %s' % os.path.abspath(fnoutpath))
        return fnoutpath
    return wrap_filePath()


def fullPath(fn):
    '''
    build path for parameter file
    '''
    full_path = os.path.realpath(__file__)
    dirpath, prog_file = os.path.split(full_path)

    def wrap_fullPath():    # my decorator wrapper
        image_dir = '/images'
        for imgcount in range(3):
            count += 1
            print ('image')

        param_file = os.path.join(dirpath, image_dir, image)
    return wrap_fullPath

@filePath
@fullPath

