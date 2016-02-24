#!/usr/bin/env python3
"""
    Luis Gonzalez Fernandez
    luisgf@luisgf.es

    Watson Detection Tools, 01/08/2014

"""

GREEN = '\033[92m\033[1m'
RED = '\033[91m\033[1m'
END = '\033[0m'
BOLD = '\033[1m'


def fail(msg):
    """ Devuelve un mensaje en Rojo y Negrita """
    return '%s%s%s' % (RED, msg, END)

def ok(msg):
    """ Devuelve un mensaje en Verde y negrita """
    return '%s%s%s' % (GREEN, msg, END)

def bold(msg):
    """ Devuelve un mensaje en negrita """
    return '%s%s%s' % (BOLD, msg, END)
