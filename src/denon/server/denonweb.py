import web
import sys, os
from denon.api.commander import commander
from denon.data.commands import commands
from denon.data.commands import parameters

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
        return render.command({'commands': commands, 'parameters': parameters})

    def POST(self):
        x = web.input()
        if not x.command:
            return False
        if d.connect():
            d.sendCommand(x.command)
        else:
            return render.badConnection(d)
        buffer = d.readBuffer()
        d.disconnect()
        return render.command({'command': x.command, 'buffer': buffer, 'commands': commands, 'parameters': parameters})
        
         
class Main:
    def GET(self):
        return sys.path

def app():
    d = web.application(urls, globals())
    return d
