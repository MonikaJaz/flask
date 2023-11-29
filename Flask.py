from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")  # main page
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__": # runs the app
    app.run(debug=True)






'''
@app.route("/<name>")  # redirects to another page
def user(name):
    return f"Hello {name}!"

# redirecting to the pages
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))
'''


