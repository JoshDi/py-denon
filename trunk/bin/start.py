import os
import sys

def configure_server():
    from denon.config import default as conf
    from denon.server import denonweb

    denonweb.app().run()

def configure_path():
    base = os.path.dirname(__file__)
    src = os.path.abspath(os.path.join(base, "..", "src"))
    sys.path.insert(0, src)
    print 'Path added: %s' % src

def redirect_output():
    f = open('./denon.log', 'w')
    sys.stdout = f
    sys.stderr = f

if __name__ == '__main__':
    import socket

    #redirect_output()
    configure_path()
    configure_server()
