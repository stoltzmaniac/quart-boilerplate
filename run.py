from quart import Quart, jsonify, websocket
from api.views import api


app = Quart(__name__)
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def index():
    return jsonify({'Index': 'Page'})


@app.websocket('/ws')
async def ws():
    while True:
        data = await websocket.receive()
        await websocket.send(f"echo {data}")


if __name__ == '__main__':
    app.run()
