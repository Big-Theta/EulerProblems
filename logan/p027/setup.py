from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

DEPENDANCIES_LIST = ['my_solver.pyx']

setup(
        cmdclass = {'build_ext': build_ext},
        ext_modules = [Extension("my_solver", DEPENDANCIES_LIST)]
    )
