#!python
#cython: language_level=3, boundscheck=False

from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("../tests",['test.pyx'],)]
setup(
	name = 'test11',
	packages=find_packages(),
	cmdclass = {'build_ext': build_ext},
	ext_modules = ext_modules,
)