import os

from flask import Flask, render_template, request, redirect, url_for
from irtp.db import post_email

def page_not_found(e):
    return render_template("errors/404.html"), 404

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_error_handler(404, page_not_found)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return "Under Construction! Please do not hack!"

    @app.route('/lp')
    def lp():
        return render_template("index.html")

    from . import presse
    app.register_blueprint(presse.bp)

    #CHANGE FOR AN AJAX REQUEST
    @app.route('/<path:path>', methods=["POST"])
    def newsletter(path):
        if request.method == "POST":
            email = request.form.get("email")
            post_email(email)
        return redirect(request.url)

    return app

#important addition in order to use waitress
app = create_app()
