import web, sys, os
from denon.api.commander import commander
from denon.data.commands import commands
from denon.data.commands import parameters
from web.contrib.template import render_mako

urls = (
    '/command/', 'Command',
    '/ajax/', 'Ajax',
    '/', 'Main',
)

app = web.application(urls, globals())
templatesDir = os.path.join(os.path.dirname(__file__), "templates")
# render = web.template.render(templatesDir, base="layout")
# Use mako templates instead of webpy builtin.
render = render_mako(
        directories=[templatesDir],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )
d = commander()
         
class Main:
    def GET(self):
        x = commander()
        return render.status(d=d, x=x)


class Ajax:
    def GET(self):
        x = web.input()
        buffer = '[]'
        web.header("Content-Type", "application/json")
        if not x.command:
            return False
        else:
            commands = x.command.split(',')
        if d.connect():
            d.sendCommand(commands)
        else:
            return "{'status': 'error', 'message': 'Couldn\\'t connect to serial port'}"
        if int(x.readbuffer):
            buffer = d.readBuffer().split('\r')
        return "{'status': 'success', 'buffer': %s}" % buffer


def app():
    d = web.application(urls, globals())
    return d
