from flask import Flask, render_template

app = Flask(__name__)

# 1. default → 8x8
@app.route("/")
def index():
    return render_template(
        "index.html",
        rows=8,
        cols=8,
        color1="red",
        color2="black"
    )

# 2. /4 → 8x4
@app.route("/<int:x>")
def one_param(x):
    return render_template(
        "index.html",
        rows=8,
        cols=x,
        color1="red",
        color2="black"
    )

# 3. /10/10 → x by y
@app.route("/<int:x>/<int:y>")
def two_params(x, y):
    return render_template(
        "index.html",
        rows=x,
        cols=y,
        color1="red",
        color2="black"
    )

# 4. BONUS → colors
@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def custom_colors(x, y, color1, color2):
    return render_template(
        "index.html",
        rows=x,
        cols=y,
        color1=color1,
        color2=color2
    )

# run server
if __name__ == "__main__":
    app.run(debug=True)