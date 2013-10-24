#!/usr/bin/env python3.3
#
###############################################################################
# Copyright © 2012-Now: SVAKSHA (https://github.com/svaksha) AllRightsReserved.
# License: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>
# All copies must retain this permission notice with the copyright notice.
###############################################################################
#
# Edge Detection, http://en.wikipedia.org/wiki/Edge_detection
##=============================================================================
#
import numpy as np
from numpy import array, newaxis
from PIL import Image
import glob
import os, os.path
import sys
import time
import io, csv
import argparse
from scipy.ndimage.interpolation import zoom
from scipy.signal import freqz
#sys.path.append("..")
##=============================================================================



def imageBuddha(pathToImages):
    pix = Image.open(pathToImages)
    pix.show()
    pix = np.array((1024,1024))
    tn_pix = zoom(pix,0.5)
    aks = tn_pix.convert('L')
    imcropd = aks.crop([0,0,5,5])
    imcropd.size
    return aks


def convFloat(imgcropd):
    """
    Converting the greyscale image into a floating type. Shades of gray are
    coded as unsigned one-byte integer values with 0 corresponding to black
    and 255 corresponding to white.
    """
    bmap = np.array(imgcropd, dtype=float)
    df = bmap/256       # converts my image to floating types between 0 to 1
    print (df)
    return df


def diagonalMatrix(df, dist=5):
    """
    The distance can be increased or decreased for finer or coarser edge
    detection.
    """
    tLbR = abs(np.subtract(df[0:-dist,0:-dist] , df[dist:,dist:]))
    print ("tLbR", tLbR)
    bLtR = abs(np.subtract(df[0:-dist,dist:] , df[dist:,0:-dist]))
    print ("bLtR", bLtR)
    diaDD = tLbR + bLtR

    # Dump output to .npy
    for darray in image_list:
        dacsv = darray
        pathToimage = os.path.join(dir_datum, dacsv)
        data_npy = np.asarray(diaDD)
        np.save(r'npy_namdroling_monastry.npy', data_npy)
        np.save(r'npy_buddha.npy', data_npy)
        np.save(r'npy_amitabha.npy', data_npy)

        data_npy.seek(0) # Only needed here to simulate closing & reopening file
        np.load(data_npy)
    return diaDD



##=============================================================================
# MAIN
##=============================================================================
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
        aks = imageBuddha(pathToimage)
        df = convFloat(aks)
        diaMatriX = diagonalMatrix(df, 5)

        # diagonal computation output of a (n-1) X (n-1) matrix:
        print ("Output of the diagonal MatriX", diaMatriX)
        diaMatriX = Image.fromarray(diaMatriX*256)
        diaMatriX.show()


