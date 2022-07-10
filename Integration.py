"""
    Launches the Flask app
"""
import os
import flask
from settings import app, socketio
import collections
from collections import abc
collections.MutableMapping = abc.MutableMapping

# ======================================================================================
@app.route("/")
def about():
    """ main page """
    return flask.render_template("landing_page.html")
# =======================================================================================
@app.route("/resume.html")
def resume():
    """ main chat window """
    return flask.render_template("resume.html")
# =======================================================================================
@app.route("/projects.html")
def projects():
    """ main chat window """
    return flask.render_template("projects.html")
# =======================================================================================
@app.route("/contact.html")
def contact():
    """ main chat window """
    return flask.render_template("contact.html")

# =======================================================================================
@app.route("/main_chat.html")
def main():
    """ main chat window """
    return flask.render_template("main_chat.html")


# =========================================================================================
@app.route("/options.html")
def options():
    """ main chat window """
    # save_progress()
    return flask.render_template("options.html")


# =======================================================================================

# RUNS ON THIS HOST AND PORT
if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "192.168.86.38"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
