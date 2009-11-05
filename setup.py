#!/usr/bin/env python
import os
import sys
from distutils.core import setup, Extension 

try:
    BUFR_LIBRARY_PATH=os.environ['BUFR_LIBRARY_PATH']
    BUFR_TABLES=os.environ['BUFR_TABLES']
except KeyError, e:
    print ("""Please define system variables 
            
            BUFR_LIBRARY_PATH, directory containing libbufr.a

            BUFR_TABLES, path to your BUFR tables, this can be changed
            runtime by changing the environment variable
            
            """)
    sys.exit(1)

BUFRFile = Extension('pybufr/BUFRFile',
                            define_macros = [('DTABLE_PATH', BUFR_TABLES),],
                            sources = ['pybufr/BUFRFile.c',], 
                            extra_compile_args = ['-O3', ], 
                            extra_link_args = [], 
                            libraries = ['bufr','gfortran',],
                            library_dirs = ['/usr/local/lib',BUFR_LIBRARY_PATH, ],
                            include_dirs = ['/usr/local/include'])

setup(name='pybufr',
      version='0.3',
      description='Generic Python BUFR file reader based on the ECMWF BUFR library',
      author='Kristian Rune Larsen',
      author_email='krl@dmi.dk',
      packages = ['pybufr'],
      ext_modules = [ BUFRFile, ]
     )
