## Python
# Is an interface

## CPython -> compiles to bytecode; then interprets it
# Original python implementation

## Cython
# Implementation of python in C

## Jython
# Implementation of python in Java

## IronPython
# Implementation of python in C#


# -------------------------------------------------------------------------
# ByteCode: porable; between source code and machine code
# vs
# MachineCode: fast binary; runs directly on CPU


# -------------------------------------------------------------------------
# pip install cython
import distutils.core as dcore
import Cython.Build as cb
import sys

dcore.setup(ext_modules=cb.cythonize(sys.path[0] + "/test_cython.pyx"))