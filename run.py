from quart import Quart, jsonify, websocket
from blueprints.api.views import api
from blueprints.users.views import users


app = Quart(__name__)
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(users, url_prefix='/users')


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
