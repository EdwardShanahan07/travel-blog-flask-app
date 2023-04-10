from flask import Flask, render_template

# Flask App

app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("index.html", title="Welcome")


@app.route("/about")
def about(): 
    return render_template("about.html", title="About")


@app.route("/blog")
def blog(): 
    return render_template("blog.html", title="Blog")


@app.route("/contact")
def contact(): 
    return render_template("contact.html", title="Contact")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)

