from flask import Flask

app = Flask(__name__)


# 1️⃣ Hello World
@app.route("/")
def hello():
    return "Hello World!"


# 2️⃣ Champion
@app.route("/Champion")
def champion():
    return "Champion!"


# 3️⃣ say/<name>
@app.route("/say/<name>")
def say_name(name):
    return f"Hi {name}!"


# 4️⃣ repeat/<num>/<word>
@app.route("/repeat/<int:num>/<word>")
def repeat_word(num, word):
    return (word + " ") * num


# 5️⃣ Bonus (error handler)
@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."


# تشغيل السيرفر
if __name__ == "__main__":
    app.run(debug=True)