from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/numbergame")
def numbergame():

    return render_template("numbergame.html")

@app.route("/rocksipa")
def rocksipa():

    return render_template("rocksipa.html")


if __name__ == "__main__":
    app.run(debug=True)