from quart import Blueprint, jsonify


api = Blueprint('api', __name__,
                template_folder='templates',
                static_folder='static')


@api.route('/<word>')
def word_return(word):
    return jsonify({'the_word': word})
