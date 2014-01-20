from asyncio import coroutine, sleep
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

app.run()
