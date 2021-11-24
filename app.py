from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/image")
def image():
    return render_template("image.html")

@app.route("/advanced")
def advanced():
    return render_template("advanced.html")

if __name__ == "__main__":
    app.run(debug=True)