#!/usr/bin/env python3.3
###############################################################################
# Copyright © 2012-Now: SVAKSHA (https://github.com/svaksha) AllRightsReserved.
# License: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>
# All copies must retain this permission notice with the copyright notice.
###############################################################################

# Stdlib imports
import numpy
import numpy as np
from numpy import array, newaxis
from PIL import Image
import glob, sys
import os, os.path

def imageBuddha(image_path):
    pix = Image.open(image_path)
    pix.show()
    img = pix.convert('L')
    imcropd = img.crop([0,0,5,5])
    imcropd.size
    return img


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
    topLeftbotRight = abs(np.subtract(df[0:-dist,0:-dist] , df[dist:,dist:]))
    print ("topLeftbotRight", topLeftbotRight)
    botLefttopRight = abs(np.subtract(df[0:-dist,dist:] , df[dist:,0:-dist]))
    print ("botLefttopRight", botLefttopRight)
    diaDD = topLeftbotRight + botLefttopRight
    return diaDD




if __name__ == '__main__':
    # build paths to import modules via pathya.py
    full_path = os.path.realpath(__file__)
    dir_path, prog_file = os.path.split(full_path)
    parent_root = os.path.abspath(os.path.join(dir_path, os.pardir))
    label_daemon = 'daemon'
    pathya_path = os.path.join(parent_root, label_daemon)
    sys.path.append(pathya_path)
    import pathya

    def _safe_exists(path):
        """
        Check path, but don't let exceptions raise
        """
        try:
            return os.path.exists(path)
        except Exception:
            return False

    for count in range(3):
        label_images = 'images'
        images_path = os.path.join(parent_root, label_images)
        image_path = pathya.imagePath(images_path, count)
        img = imageBuddha(image_path)
        df = convFloat(img)
        diaMatriX = diagonalMatrix(df, 5)
        # diagonal computation output of a (n-1) X (n-1) matrix:
        print ("Output of the diagonal MatriX", diaMatriX)

        diaMatriX = Image.fromarray(diaMatriX*256)
        diaMatriX.show()

