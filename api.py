from flask import Flask, jsonify
from devtools.commands import hello, generate_uuid, slugify


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "app": "devtools-cli",
        "status": "running"
    })


@app.route("/uuid")
def uuid():
    return jsonify({"uuid": generate_uuid()})


@app.route("/slugify/<text>")
def slugify_text(text):
    return jsonify({"slug": slugify(text)})


@app.route("/hello/<name>")
def hello_name(name):
    return jsonify({"message": hello(name)})


if __name__ == "__main__":
    app.run()
