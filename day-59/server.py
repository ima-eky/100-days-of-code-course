from flask import Flask,render_template
import requests
from post import Post
 # using requests to get blog data
response=requests.get("https://api.npoint.io/2b98e8835e979b3f55c4")
data=response.json()
posts_object=[]

for post in data:
    post_data=Post(post['id'],post['title'],post['subtitle'],post['body'],post['author'],post['date'])
    posts_object.append(post_data)

app = Flask(__name__)

# Creating  different routes using the app.route decorator
@app.route('/index')
def home_page():
    return render_template('index.html',all_post=data)

@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/contact")

def contact():
    return render_template('contact.html')

@app.route("/<int:index>")
def display_post(index):
    requested_post=None
    for post_detail in posts_object:
        if post_detail.id == index:
            requested_post=post_detail
    return render_template("post.html",post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)