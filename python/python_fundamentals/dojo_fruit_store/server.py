from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("fruits.html")

@app.route("/checkout", methods=["POST"])
def checkout():
    strawberry = int(request.form["strawberry"])
    raspberry = int(request.form["raspberry"])
    apple = int(request.form["apple"])

    name = request.form["name"]
    student_id = request.form["student_id"]

    count = strawberry + raspberry + apple

    print(f"Charging {name} for {count} fruits")

    return render_template("checkout.html",
        strawberry=strawberry,
        raspberry=raspberry,
        apple=apple,
        name=name,
        student_id=student_id,
        count=count
    )

if __name__ == "__main__":
    app.run(debug=True)