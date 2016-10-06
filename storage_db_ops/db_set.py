from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext


ext_modules=[
    Extension("db_ops",["db_operations.py"],),
    Extension('db_connections',['db_connection.pyx']) ]

setup(name='db ops package',
      packages=find_packages(),
      cmdclass = {'build_ext': build_ext},
      ext_modules = ext_modules,
     )
