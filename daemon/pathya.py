#!/usr/bin/env python3.3
# encoding: utf-8
################################################################################
# Copyright(C) 2012-Now SVAKSHA. <https://github.com/svaksha> AllRightsReserved.
# Distributed under the AGPLv3 License <http://www.gnu.org/licenses/agpl.html>
# All copies must retain this permission notice with the copyright notice.
################################################################################
# PATH finder for your system.
##==============================================================================
# Imports
##------------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals ##python3.x
import glob
import sys
import os, os.path
##==============================================================================
# PROGRAM
##------------------------------------------------------------------------------

image_list = ['NamdrolingMonastry.png',
              'Buddha.png',
              'Amitabha.png',
              ];


def dirPath():
    '''
    build path for parameter file
    '''
    full_path = os.path.realpath(__file__)
    dir_daemon, prog_file = os.path.split(full_path)
    dir_chaya = os.path.abspath(os.path.join(dir_daemon,os.pardir))
    dir_api = os.path.join(dir_chaya,"api")
    dir_chAya = os.path.join(dir_chaya,"chAya")
    dir_datum = os.path.join(dir_chaya,"datum")
    return dir_daemon, dir_chaya, dir_api, dir_chAya, dir_datum

count = 1
def imageCounter(count):
    dir_datum_png = image_list[count]
    return dir_datum_png
imageCounter(count)

