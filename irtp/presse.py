from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for)

from irtp.db import get_articles, get_db

bp = Blueprint("presse", __name__, url_prefix='/presse')

@bp.route("/")
def presse():
    articles = get_articles()
    return render_template("presse/presse.html", articles=articles)
