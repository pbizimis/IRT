from flask import render_template

def page_not_found(e):
    return render_template("errors/404.hmtl"), 404