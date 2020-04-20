from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, from a variable!"
    return render_template("index.html", headline=headline)

if __name__ == "__main__":
    app.run()
