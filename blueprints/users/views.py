from quart import Blueprint, jsonify


users = Blueprint('users', __name__,
                  template_folder='templates',
                  static_folder='static')


@users.route('/<word>')
def word_return(word):
    return jsonify({'the_word': word})
