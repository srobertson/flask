from aiohttp.wsgi import WSGIServerHttpProtocol
from asyncio import coroutine, sleep
import asyncio
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/hello/<string:name>")
@coroutine
def say_hi(name):
    yield from sleep(2)
    return "it worked %s" % request.args.get("name", name)

@app.route("/say", methods=["POST"])
@coroutine
def say_msg():
    yield from sleep(2)
    body = request.json
    return "it worked %s" % body['message']

loop = asyncio.get_event_loop()
asyncio.async(loop.create_server(lambda: WSGIServerHttpProtocol(app, readpayload=True), "localhost", 8000))
loop.run_forever()
