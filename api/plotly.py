# -*- coding: utf-8 -*-
#!/usr/bin/env python3.3
###############################################################################
# Copyright © 2012-Now, SVAKSHA, https://github.com/svaksha AllRightsReserved.
# License: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>
# All copies must retain this permission notice with the copyright notice.
###############################################################################
"""
Created on Wed Oct 16 21:04:41 2013
"""
##API
import plotly
import numpy as np
# from bottle import run, template, get, post, request


py = plotly(username='svaksha', key='jaa4r8qvt2')

username='svaksha'
email='svaksha@gmail.com'
response = plotly.signup(username, email)
api_key = response['api_key']
tmp_pw = response['tmp_pw']
print( "api_key:", api_key)
print( "tmp_pw:", tmp_pw)