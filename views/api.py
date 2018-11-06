import quart

blueprint = quart.blueprints.Blueprint(__name__, __name__)


@blueprint.route('/')
def index():
    return quart.jsonify({'hello': 'api'})


@blueprint.errorhandler(404)
def not_found(_):
    return quart.Response("The page was not found.", status=404)
