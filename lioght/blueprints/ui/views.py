from flask import render_template

from . import ui


@ui.route("/", methods=["GET"])
def index():
    return render_template("index.html")
