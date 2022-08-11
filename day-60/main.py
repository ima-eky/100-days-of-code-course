from flask import Flask,render_template,request
# Creating a new flask application
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=['POST'])
def get_data():
    if request != 'POST':
        pass

    values = request.values
    name = values['username']
    password = values['userpassword']
    return f"<h1>Name: {name}, Password: {password}</h1>"




if __name__ == '__main__':
    app.run(debug=True)