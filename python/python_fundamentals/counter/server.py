from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "my_secret_key"


@app.route("/")
def index():
    if "visits" not in session:
        session["visits"] = 0

    if "counter" not in session:
        session["counter"] = 0

    session["visits"] += 1

    return render_template(
        "index.html",
        visits=session["visits"],
        counter=session["counter"]
    )


@app.route("/add_two")
def add_two():
    if "counter" not in session:
        session["counter"] = 0

    session["counter"] += 2
    return redirect("/")


@app.route("/reset")
def reset():
    session["counter"] = 0
    return redirect("/")


@app.route("/add_custom", methods=["POST"])
def add_custom():
    if "counter" not in session:
        session["counter"] = 0

    number = int(request.form["number"])
    session["counter"] += number

    return redirect("/")


@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)