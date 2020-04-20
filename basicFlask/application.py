from flask import Flask

app = Flask(__name__)  # new Flask web application; __name__ represents the name of this webapp

@app.route("/")  # / represents the default Webpage.  The function defined immediately underneath will be executed at /
def index():
    return "Hello there!"

@app.route("/shree")
def shree():
    return "Hello, Shree!"

@app.route("/<string:name>")
def hello(name):
    return(f"Hello, {name}!")


if __name__ == "__main__":
    app.run()
