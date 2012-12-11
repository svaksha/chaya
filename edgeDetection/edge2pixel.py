#!/usr/bin/env python
# -*- coding: utf-8 -*-
##*************************************************************************
## COPYRIGHT © 2011-Now. VidAyer <svaksha|AT|gmail*com> All Rights Reserved.
## LICENSE
# AGPLv3 LICENSE <http://www.gnu.org/licenses/agpl.html>
# See LICENSE.md file. The above Copyright notice and this permission notice
# must be included in all copies or substantial portions of the Software.
##*************************************************************************

import numpy
import numpy as np
from numpy import array, newaxis
import Image
import glob, os.path, sys # system level stuff
import shutil as sh

im = Image.open("/home/m/Envs/jn/chaya/img-3D/PA200001.JPG").convert('L')
im.show()
print im.size # 2560 x 1920 pixels

# converting the greyscale image into a floating type
# shades of gray are coded as unsigned one-byte integer values with 0
# corresponding to black and 255 corresponding to white.
bmap = np.array(im, dtype=float)
bmfloat = bmap / 256 # converts my image to floating types bet 0 to 1
print bmfloat

def diffRow():
    newRow = np.array(bmfloat[:-1, :-1]) #last elem, lastElem
    for row in range(len(newRow)):
        for col in range(len(newRow)):
            newRow[row][col] = bmfloat[row][col] - bmfloat[row+1][col]
            continue
    print "printing newRow"
    print newRow
diffRow() #post computation output of a (n-1) X (n-1) matrix for each ROW
print np.shape(diffRow)

def diffCol():
    newCol = np.array(bmfloat[:-1, :-1]) #last elem, lastElem
    for row in range(len(newCol)):
        for col in range(len(newCol)):
            newCol[row][col] = bmfloat[row][col] - bmfloat[row][col+1]
            continue
    print "printing newCol"
    print newCol
diffCol() #post computation output of a (n-1) X (n-1) matrix for each COLUMN
print np.shape(diffRow[:,newaxis] + diffCol)

def gridRowCol(diffCol, diffRow):
    """
    For a two-connected matrix, I am adding the values if the two new arrays,
    diffRow and diffCol to get a new grid, which will be the edge detected Picture.
    """
    print "111"
    #gridRC = np.concatenate([diffRow(), diffCol()])
    #gridRC = np.add(diffCol(), diffRow())
    #return gridRC
    for row in newRow(): #return the num.of.items of a sequence.
        #newRow = np.array(bmfloat[:-1, :-1])
        for col in diffRow(): #
            # newaxis index operator inserts a new axis into a,
            # making it a two-dimensional 4x1 array.
            gridRC = diffRow[:,newaxis] + diffCol[:,newaxis]
            continue
        print "gridRC", gridRC
gridRowCol(diffCol, diffRow)
