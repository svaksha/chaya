################################################################################
"""
COPYRIGHT: 2012-Now, SVAKSHA :: https://github.com/svaksha
LICENSE: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>.
All copies must retain this permission notice with the copyright notice.
"""
################################################################################
__author__ = 'SVAKSHA'
__copyright__ = 'Copyright (c) 2012-Now, SVAKSHA'
__license__ = 'AGPLv3'

from __future__ import (absolute_import, division,print_function, unicode_literals)
import glob, sys
import os, os.path
import time, pdb
import io
# Scientific pkg
import numpy as np
from numpy import array, newaxis
from PIL import Image, ImageMath
import scipy as sci
from scipy.signal import freqz
from scipy.misc import toimage
from scipy.ndimage.interpolation import zoom
import matplotlib.pyplot as plt
# experimenting with parallel processing, https://medium.om/p/40e9b2b36148
from multiprocessing import Pool
from multiprocessing.dummy import Pool as tPool
#from chaya.daemon import pathya # dirPath, imageCounter
from chaya import datum
#
##==============================================================================
## PROGRAM USECASE: Edge Detection, http://en.wikipedia.org/wiki/Edge_detection
##------------------------------------------------------------------------------

def datumImage(pathToImages):
    pix = np.array(Image.open(pathToImages).convert('RGB'))
#    pix.show()
 #   pix = np.array((1024,1024))
    print(pix.dtype, pix.shape, pix.size)
    print(type(pix))
    imarray = np.array(pix.astype(float))
    print(imarray)
    pdb.set_trace()
    return imarray


def greyscale2Float(convertgf):
    """
    Converting the greyscale image into a floating type. Shades of gray are
    coded as unsigned one-byte integer values with 0 corresponding to black
    and 255 corresponding to white.
    """
    bitmap = np.array(convertgf, dtype=float)
    df = bitmap / 255      # converts my image to floating types between 0 to 1 (df /= 255)
    print(df)
    return df


def diagonalMatrix(df, dist=5):
    """
    The distance can be increased or decreased for finer or coarser edge
    detection.
    """
    tLbR = abs(np.subtract(df[0:-dist,0:-dist] , df[dist:,dist:]))
    print("tLbR", tLbR)
    print(np.median(tLbR, 1))   # print median
    bLtR = abs(np.subtract(df[0:-dist,dist:] , df[dist:,0:-dist]))
    print("bLtR", bLtR)
    diaDD = tLbR + bLtR
    return diaDD


##==============================================================================
# MAIN
##==============================================================================
if __name__ == '__main__':
    # build paths to import modules via pathya.py
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','daemon')))
    from pathya import *
    dir_daemon, dir_chaya, dir_api, dir_chAya, dir_datum = dirPath()


    def _safe_exists(path):
        """
        Check path, but don't let exceptions raise
        """
        try:
            return os.path.exists(path)
        except Exception:
            return False

    for image in image_list:
        image_label = image
        pathToimage = os.path.join(dir_datum, image_label)
        pix = datumImage(pathToimage)
        df = greyscale2Float(pix)
        diaMatriX = diagonalMatrix(df, 5)

        # diagonal computation output of a (n-1) X (n-1) matrix:
        print ("Output of the diagonal MatriX", diaMatriX)

        # Take numpy array, rescale to 0-255, convert to uint8, return PIL image.
        rescaledMatrix = (255.0 / imarray.max() * (imarray - imarray.min())).astype(np.uint8)
        #rescaledMatrix = Image.fromarray(diaMatriX * 255, np.uint8(diaMatriX))
        #rescaledMatrix = (255.0 / rescaledMatrix.max() * (rescaledMatrix - rescaledMatrix.min())).astype(np.uint8)
        #rescaledMatrix = Image.fromarray(rescaledMatrix)
        rescaledMatrix.show()
        rescaledMatrix.save('newImg.png')
#==============================================================================
#
#         rescaledMatrix[:] = imarray[:]
#         %timeit rescaledMatrix[:] = imarray[:]; sort(rescaledMatrix)
#==============================================================================


