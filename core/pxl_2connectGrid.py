#!/usr/bin/env python3.3
###############################################################################
# Copyright © 2012-Now, SVAKSHA (https://github.com/svaksha) AllRightsReserved.
# License: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>
# All copies must retain this Copyright notice and this permission notice.
###############################################################################

import numpy
import numpy as np
from numpy import array, newaxis
import Image
import glob, sys
import os, os.path
import shutil as sh
import pathya
img_path = pathya.filePath()


im = Image.open("/PA200001.JPG").convert('L')
im.show()
print (im.size)        # 2560 x 1920 pixels

# converting the greyscale image into a floating type
# shades of gray are coded as unsigned one-byte integer values with 0
# corresponding to black and 255 corresponding to white.
bmap = np.array(im, dtype=float)
bmfloat = bmap/256        # convert image to floating types bet 0 to 1
print (bmfloat)

def diffRow():
    newRow = np.array(bmfloat[:-1, :-1])    #last elem, lastElem
    for row in range(len(newRow)):
        for col in range(len(newRow)):
            newRow[row][col] = bmfloat[row][col] - bmfloat[row+1][col]
            continue
    print ("printing newRow")
    print (newRow)
# post computation output of a (n-1) X (n-1) matrix for each ROW
diffRow()
print (np.shape(diffRow))

def diffCol():
    for row in range(len(a)):
        for column in range(len(a[0])): #start from 0-th position
            answer[row][column]=a[row][column]-a[row][column+1 ]

    newCol = np.array(bmfloat[:-1, :-1]) #last elem, lastElem
    for row in range(len(newCol)):
        for col in range(len(newCol)):
            newCol[row][col] = bmfloat[row][col] - bmfloat[row][col+1]
            continue
    print ("printing newCol")
    print (newCol)
diffCol() #post computation output of a (n-1) X (n-1) matrix for each COLUMN
print (np.shape(diffRow[:,newaxis] + diffCol))


def gridRowCol(diffCol, diffRow):
    """
    For a two-connected matrix, I'm adding the values of the two new arrays,
    diffRow and diffCol to get a new grid, which will be the edge detected Picture.
    """
    print "111"
    #gridRC = np.concatenate([diffRow(), diffCol()])
    #gridRC = np.add(diffCol(), diffRow())
    #return gridRC
    for row in newRow():     #return the number of items in a sequence.
        #newRow = np.array(bmfloat[:-1, :-1])
        for col in diffRow(): #
            # newaxis index operator inserts a new axis into a,
            # making it a two-dimensional 4x1 array.
            gridRC = diffRow[:,newaxis] + diffCol[:,newaxis]
            continue
        print ("gridRC", gridRC)

gridRowCol(diffCol, diffRow)
for index in np.ndindex(3, 2, 1):
    print (index)
