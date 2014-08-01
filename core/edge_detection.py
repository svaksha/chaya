#!/usr/bin/env python
#encoding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
################################################################################
"""
COPYRIGHT© 2012-Now SVAKSHA :: https://github.com/svaksha
LICENSE: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>.
All software copies must retain the Copyright, Licence and permission notice.
"""
################################################################################
__author__ = 'SVAKSHA'
__copyright__ = 'Copyright (c) 2012-Now, SVAKSHA'
__license__ = 'AGPLv3'
__version__ = "14.04.dev"

import glob, sys
import os, os.path
import time#, pdb
import io
import numpy as np
from numpy import array, newaxis
import PIL.Image as Image
import PIL.ImageOps as ImageOps

##==============================================================================
## PROGRAM USECASE: Edge Detection, http://en.wikipedia.org/wiki/Edge_detection
##==============================================================================

def datumImage(pathToImages):
    pix = np.array(Image.open(pathToImages).convert('RGB'))
    print(pix.dtype, pix.shape, pix.size)
    print(type(pix))
    imarray = np.array(pix.astype(float))
    print(imarray)
    return imarray


def fn_greyscale_toFloat(convertgf):
    """
    Converting the greyscale image into a floating type. Shades of gray are
    coded as unsigned one-byte integer values with 0 corresponding to black
    and 255 corresponding to white.
    """
    bitmap = np.array(convertgf, dtype=float)
    df = bitmap/255  #Converts my image to floating types between 0 to 1 (df /= 255)
    print(df)
    return df


def fn_diagonalMatrix(df, dist=5):
    """
    Distance can be increased or decreased for finer or coarser edge detection.
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
        df = fn_greyscale_toFloat(pix)
        diaMatriX = fn_diagonalMatrix(df, 5)

        # diagonal computation output of a (n-1) X (n-1) matrix 
        print ("Output of the diagonal MatriX", diaMatriX)
        # Fetch numpy array, rescale and convert, return PIL image.
        rescaled_matrix = np.array(diaMatriX.astype(float))
        
        
        image_list = ['Amitabha.png',
              'NamdrolingMonastry.png',
              'Buddha.png',              
              'brown_bluff_antarctic_peninsula_antarctica.jpg',
              'carnivore_preservation_trust_north_carolina.jpg',
              'chinstrap_penguins_antarctica.jpg',
              'churchill_manitoba_canada.jpg',
              'lakeside-reflection-gehman_1438_600x450.jpg',
              'mombo_okavango_delta_botswana.jpg',
              'northern_spotted_owl_california.jpg',
              'wise_owl.jpeg',
              ];

    counter = 1
    def count_processedImages(counter):
        processed_img_name = image_list[counter]
        return processed_img_name
    count_processedImages(counter)
    print("Finished processing image name",counter)
    
    
    
