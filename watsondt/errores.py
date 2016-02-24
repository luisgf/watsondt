#!/usr/bin/env python3
"""
    Luis Gonzalez Fernandez
    luisgf@luisgf.es

    Watson Detection Tools, 01/08/2014

"""

class ErrorGeneral(Exception):
    pass

class IOCException(ErrorGeneral):
    pass

class IOCFormatError(IOCException):
    pass

class IOCTypeError(IOCException):
    pass
