#!/usr/bin/env python

"""Setup script for the MAD module distribution."""

import os, re, sys, string

from distutils.core import setup
from distutils.extension import Extension

VERSION_MAJOR = 0
VERSION_MINOR = 2
pymad_version = str(VERSION_MAJOR) + "." + str(VERSION_MINOR)

def get_setup():
    data = {}
    r = re.compile(r'(\S+)\s*?=\s*?(.+)')
    
    if not os.path.isfile('Setup'):
        print "No 'Setup' file. Perhaps you need to run the configure script."
        sys.exit(1)
        
    f = open('Setup', 'r')
        
    for line in f.readlines():
        m = r.search(line)
        if not m:
            print "Error in setup file:", line
            sys.exit(1)
        key = m.group(1)
        val = m.group(2)
        data[key] = val
        
    return data

data = get_setup()

mad_include_dir = data['mad_include_dir']
mad_lib_dir = data['mad_lib_dir']
mad_libs = string.split(data['mad_libs'])

madmodule = Extension(
    name='madmodule',
    sources=['src/madmodule.c',
             'src/pymadfile.c'],
    define_macros = [('VERSION_MAJOR', VERSION_MAJOR),
                     ('VERSION_MINOR', VERSION_MINOR),
                     ('VERSION', '"%s"' % pymad_version)],
    
    include_dirs=[mad_include_dir],
    library_dirs=[mad_lib_dir],
    libraries=mad_libs)

setup ( # Distribution metadata
    name = "pymad",
    version = pymad_version,
    description = "A wrapper for the MAD libraries.",
    author = "Jamie Wilkinson",
    author_email = "jaq@spacepants.org",
    url = "http://spacepants.org/src/pymad/",
    license = "GPL",
    
    packages = ['mad'],
    package_dir = {'mad' : 'src'},
    ext_package = 'mad',
    ext_modules = [madmodule])
