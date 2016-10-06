from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext

# ext_modules=[
#     Extension("home.vikrant-singh.vikrant.workspace.glydel.gateway.mobile_gateway_apis.test_scripts/tests.so",    # location of the resulting .so
#              ["/home/vikrant-singh/vikrant/workspace/glydel/gateway/mobile_gateway_apis/test_scripts/test.pyx"],) ]


ext_modules=[
    Extension(".tests",    # location of the resulting .so
             ["test.pyx"],) ]

setup(name='package 3',
      packages=find_packages(),
      cmdclass = {'build_ext': build_ext},
      ext_modules = ext_modules,
     )
