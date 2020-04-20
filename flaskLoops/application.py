from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Shree", "John", "Joe"]
    return render_template("index.html", names=names)

if __name__ == "__main__":
    app.run()
