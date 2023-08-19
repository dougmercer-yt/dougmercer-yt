from Cython.Build import cythonize
from mypyc.build import mypycify
from setuptools import setup

setup(
    name="lcs",
    packages=["lcs"],
    ext_modules=cythonize(["lcs/cython2.pyx", "lcs/cython_.py"]) + mypycify(["lcs/mypyc_.py"]),
)
