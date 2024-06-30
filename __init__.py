from flask import Flask, render_template
from .API.routes import routes as routes_blueprint

def create_app():
    app = Flask(__name__)
    app.secret_key = '123456789'
    app.register_blueprint(routes_blueprint, url_prefix='/api')

    @app.route('/')
    def home():
        return render_template('index.html')

    return app
