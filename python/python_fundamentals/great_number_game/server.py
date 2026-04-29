from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "secret123"


@app.route("/")
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["result"] = ""

    return render_template("index.html", result=session["result"])


@app.route("/guess", methods=["POST"])
def guess():
    guess = int(request.form["guess"])
    number = session["number"]

    if guess > number:
        session["result"] = "high"
    elif guess < number:
        session["result"] = "low"
    else:
        session["result"] = "correct"

    return redirect("/")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)