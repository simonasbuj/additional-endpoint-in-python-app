from flask import Flask
from waitress import serve

from .routes import bp as main_bp


app = Flask(__name__)
app.register_blueprint(main_bp)


def start_api():
    serve(app, port=5000)
    # app.run(debug=True, use_reloader=False, port=5000)


if __name__ == '__main__':
    start_api()