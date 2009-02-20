import os
import sys

def configure_server():
    import logging
    from denon.server import denonweb

    denonweb.app().run()

def configure_path():
    sys.path.insert(0, '/Users/chenry/Desktop/py-denon/src')

def redirect_output():
    f = open('./denon.log', 'w')
    sys.stdout = f
    sys.stderr = f

if __name__ == '__main__':
    import socket

    #redirect_output()
    configure_path()
    configure_server()
