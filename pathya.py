#!/usr/bin/env python3.3
###########################################################################
# COPYRIGHT © 2012. SVAKSHA, <https://github.com/svaksha>, AllRightsReserved.
# LICENSE: AGPLv3 LICENSE <http://www.gnu.org/licenses/agpl.html>
# All copies must retain this Copyright notice and this permission notice.
###########################################################################

import glob, sys
import os, os.path

# http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python?rq=1

def filePath(dirpath, file_name, fnprd, fnsfx):
    '''
    Construct filePath from inputs with a decorator function that expects
    ANOTHER function as parameter. Inside, the decorator defines a function
    on the fly: the wrapper. This function is going to be wrapped around the
    original function so it can execute code before and after it.
    '''
    file_name = os.path.abspath(dirpath, fnprd, fnsfx)
    def wrap_filePath():   # my decorator
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

    def wrap_fullPath():    # my decorater
        image_dir = '/images'
        for imgcount in range(3):
            image = imgcount + 1
            print ('image')
            image1 = '/P1010214.png'
            image2 = '/P1010218.png'
            image3 = '/P1010221.png'
        param_file = os.path.join(dirpath, image_dir, image)
    return wrap_fullPath

@filePath
@fullPath

'''
def hello():
    return "hello world"
print (hello()) ## returns <b><i>hello world</i></b>
'''

#==============================================================================
#
# def modulepath(local_function):
#    '''
#    returns the module path without the use of __file__.  Requires a function defined
#    locally in the module.
#    from http://stackoverflow.com/questions/729583/getting-file-path-of-imported-module
#    '''
#    print ('file is %s' % local_function)
#    return os.path.abspath(inspect.getsourcefile(local_function))
#==============================================================================


if __name__ == '__main__':
    funcout1 = filePath(fnoutpath)
    print ('fnoutpath=', fncout1)
    main()
