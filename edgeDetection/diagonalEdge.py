#!/usr/bin/env python3.3
###########################################################################
# COPYRIGHT © 2012. SVAKSHA, <https://github.com/svaksha>, AllRightsReserved.
# LICENSE: AGPLv3 LICENSE <http://www.gnu.org/licenses/agpl.html>
# All copies must retain this Copyright notice and this permission notice.
###########################################################################

import numpy
import numpy as np
from numpy import array, newaxis
from PIL.Image import core as _imaging
import glob, sys
import os, os.path
# import pathya
# img = pathya.filePath()


def image():
    img1 = pix1
    pix1 = Image.open("/images/P1010214.png")
    # pix2 = Image.open("/images/P1010218.png")
    # pix3 = Image.open("/images/P1010221.png")

    pix1.show()
    img1 = pix1.convert('L')
    # img2 = pix2.convert('L')
    # img3 = pix3.convert('L')
    return img

# converting the greyscale image into a floating type
# shades of gray are coded as unsigned one-byte integer values with 0
# corresponding to black and 255 corresponding to white.
bmap = np.array(img1, dtype=float)
df = bmap / 256       # converts my image to floating types between 0 to 1
print (df)


def diagonalMatrix(dist=5):
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
diaMatriX = diagonalMatrix(5)
#diagonal computation output of a (n-1) X (n-1) matrix:
print ("Output of the diagonal MatriX", diaMatriX)

diaMatriX = Image.fromarray(diaMatriX*256)
diaMatriX.show()


if __name__ == '__main__':
     main()
