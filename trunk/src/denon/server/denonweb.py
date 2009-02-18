import web
import sys, os
from denon.api.commander import commander

urls = (
    '/command/', 'Command',
    '/', 'Main',
)

app = web.application(urls, globals())
templatesDir = os.path.join(os.path.dirname(__file__), "templates")
render = web.template.render(templatesDir, base="layout")
d = commander()

class Command:
    def GET(self):
        return render.command()

    def POST(self):
        x = web.input()
        if not x.command:
            return False
        d.sendCommand(x.command)
        return render.command(x.command)
        

class Main:
    def GET(self):
        return sys.path

def app():
    d = web.application(urls, globals())
    return d