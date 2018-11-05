from quart import Quart, jsonify
from api.views import api


app = Quart(__name__)
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def index():
    return jsonify({'Index': 'Page'})


if __name__ == '__main__':
    app.run()
