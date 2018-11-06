from quart import Quart, websocket, jsonify
from config import settings
from views import api, users


app = Quart(__name__)
is_debug = True

app.register_blueprint(users.blueprint, url_prefix='/users')
app.register_blueprint(api.blueprint, url_prefix='/api')


def configure_app():
    mode = 'dev' if is_debug else 'prod'
    data = settings.load(mode)


@app.route('/')
def index():
    return jsonify({'hello': 'index'})


@app.websocket('/ws')
async def ws():
    while True:
        data = await websocket.receive()
        await websocket.send(f"echo {data}")


def run_web_app():
    app.run(debug=is_debug, port=5001)


if __name__ == '__main__':
    run_web_app()
