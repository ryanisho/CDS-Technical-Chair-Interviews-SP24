from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/subteam/<variable>")
def de(variable):
    return render_template("subteam.html", subteam=variable)


# flask network config
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
