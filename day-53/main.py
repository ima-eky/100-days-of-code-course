from flask import Flask

app=Flask(__name__)
print(__name__)

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World! </h1><p>This is a paragraph </p>' \
            '<img src="https://media3.giphy.com/media/YRVP7mapl24G6RNkwJ/200w.webp?cid=ecf05e47uoykxu9uy0fan1srslyr4o11hjyza4dbfukw8lok&rid=200w.webp&ct=g">'

# Different routes using the app.route decorator


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"
# Creating variables  paths  and converting the path to a pre-specified data type


@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hey {name} ,you are {number} years old!"


if __name__ == "__main__":
    #Run app in debug mode to autoreload server
    app.run(debug=True)
