from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

DEPENDANCIES_LIST = ['prob.pyx']

setup(
        cmdclass = {'build_ext': build_ext},
        ext_modules = [Extension("prob", DEPENDANCIES_LIST)]
    )
