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
import shutil as sh
import numpy
import numpy as np
from numpy import array, newaxis
from PIL import Image, ImageMath



def datumImage(pathToImages):
    pix = np.array(Image.open(pathToImages).convert('RGB'))
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
    df = bitmap / 255      # converts images to floating types between 0 to 1.
    print(df)
    return df


def north():
    nRow = np.array(bmfloat[:-1, :-1]) #last elem, lastElem
    for row in range(len(newRow)):
        for col in range(len(newRow)):
            newRow[row][col] = bmfloat[row][col] - bmfloat[row+1][col]
    print newRow
diffRow() #post computation output of a (n-1) X (n-1) matrix for each ROW

def east():
    nRow = np.array(bmfloat[:-1, :-1]) #last elem, lastElem
    for row in range(len(newRow)):
        for col in range(len(newRow)):
            newRow[row][col] = bmfloat[row][col] - bmfloat[row+1][col]
    print newRow
diffRow() #post computation output of a (n-1) X (n-1) matrix for each ROW

def west():
    nRow = np.array(bmfloat[:-1, :-1]) #last elem, lastElem
    for row in range(len(newRow)):
        for col in range(len(newRow)):
            newRow[row][col] = bmfloat[row][col] - bmfloat[row+1][col]
    print newRow
diffRow() #post computation output of a (n-1) X (n-1) matrix for each ROW

def south():
    nRow = np.array(bmfloat[:-1, :-1]) #last elem, lastElem
    for row in range(len(newRow)):
        for col in range(len(newRow)):
            newRow[row][col] = bmfloat[row][col] - bmfloat[row+1][col]
    print newRow
diffRow() #post computation output of a (n-1) X (n-1) matrix for each ROW

