#!/usr/bin/env python
# -*- coding: utf-8 -*-
##*************************************************************************
## COPYRIGHT © 2012-Now. VidAyer <svaksha|AT|gmail*com> All Rights Reserved.
## LICENSE
# AGPLv3 LICENSE <http://www.gnu.org/licenses/agpl.html>
# See LICENSE.md file. The above Copyright notice and this permission notice
# must be included in all copies or substantial portions of the Software.
##*************************************************************************

import numpy
import numpy as np
from numpy import array, newaxis
import Image
import glob, sys

pix = Image.open("/home/m/Envs/jna/chaya/images/P1010218.JPG")
pix.show()
im = pix.convert('L')

# converting the greyscale image into a floating type
# shades of gray are coded as unsigned one-byte integer values with 0
# corresponding to black and 255 corresponding to white.
bmap = np.array(im, dtype=float)
df = bmap / 256 # converts my image to floating types bet 0 to 1
print df

def diaM(dist=5):
    """
    The distance can be increased or decreased for finer or coarse edge detection.
    """
    tLbR = abs(np.subtract(df[0:-dist,0:-dist] , df[dist:,dist:]))
    print "tlbr", tLbR
    bLtR = abs(np.subtract(df[0:-dist,dist:] , df[dist:,0:-dist]))
    print "bLtR", bLtR
    diaDD = tLbR + bLtR
    return diaDD
diaMatriX = diaM(5)
#diagonal computation output of a (n-1) X (n-1) matrix:
print "Output of the diagonal MatriX", diaMatriX

diaMatriX = Image.fromarray(diaMatriX*256)
diaMatriX.show()
