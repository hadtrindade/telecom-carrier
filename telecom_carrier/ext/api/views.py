from flask import Blueprint


api = Blueprint("api", __name__)


@api.route("/api/v1/did", methods=["GET"])
def view_get_did():
    return "hello word", 200


def init_app(app):
    app.register_blueprint(api)
