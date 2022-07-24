from flask import Flask,render_template

# Creating a new flask application
app=Flask(__name__)

#home route
@app.route("/")
def print_hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)