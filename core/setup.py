#!/usr/bin/env python
#coding=utf-8
from __future__ import absolute_import, division,print_function, unicode_literals
################################################################################
"""
COPYRIGHT: 2012-Now, SVAKSHA :: https://github.com/svaksha
LICENSE: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>.
All copies must retain this permission notice and the copyright notice.
"""
################################################################################
__author__ = 'SVAKSHA'
__copyright__ = 'Copyright (c) 2012-Now, SVAKSHA'
__license__ = 'AGPLv3'
__version__ = "14.03.dev"


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('chaya', parent_package, top_path)

    config.add_subpackage('chAya')
    config.add_subpackage('api')
    config.add_subpackage('daemon')
    config.add_subpackage('tests')

    config.add_data_dir('datum')

    config.make_config_py()
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())


-A INPUT -m state --state NEW -m tcp -p tcp --dport 5432 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 1239 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 1240 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 1241 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 1242 -j ACCEPT
