#!/usr/bin/env python3.3
###########################################################################
# COPYRIGHT © 2012. SVAKSHA, <https://github.com/svaksha>, AllRightsReserved.
# LICENSE: AGPLv3 LICENSE <http://www.gnu.org/licenses/agpl.html>
# All copies must retain this Copyright notice and this permission notice.
###########################################################################

import numpy
import numpy as np
from numpy import array, newaxis
import Image
from PIL.Image import core as _imaging
import glob, sys
import os, os.path
import pathya


def imageBuddha(image_path):
    pix = Image.open(image_path)
    pix.show()
    img = pix.convert('L')
    return img

def convFloat(img):
    # converting the greyscale image into a floating type
    # shades of gray are coded as unsigned one-byte integer values with 0
    # corresponding to black and 255 corresponding to white.
    bmap = np.array(img, dtype=float)
    df = bmap / 256       # converts my image to floating types between 0 to 1
    print (df)
    return df

def diagonalMatrix(df, dist=5):
    """
    The distance can be increased or decreased for finer or coarser edge
    detection.
    """
    topLeftbotRight = abs(np.subtract(df[0:-dist,0:-dist] , df[dist:,dist:]))
    print ("topLeftbotRight", topLeftbotRight)
    botLefttopRight = abs(np.subtract(df[0:-dist,dist:] , df[dist:,0:-dist]))
    print ("botLefttopRight", botLefttopRight)
    diaDD = topLeftbotRight + botLefttopRight
    return diaDD



if __name__ == '__main__':
    dirpath = pathya.dirPath()
    for count in range(3):
        image_path = pathya.imagePath(dirpath, count)
        img = imageBuddha(image_path)
        df = convFloat(img)
        diaMatriX = diagonalMatrix(df, 5)
        #diagonal computation output of a (n-1) X (n-1) matrix:
        print ("Output of the diagonal MatriX", diaMatriX)

        diaMatriX = Image.fromarray(diaMatriX*256)
        diaMatriX.show()

