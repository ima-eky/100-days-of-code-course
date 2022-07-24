from flask import Flask, render_template
import requests
from post import Post



posts_object=[]

response=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data=response.json()

for post in data:
    post_data=Post(post['id'],post['title'],post['subtitle'],post['body'])
    posts_object.append(post_data)


app = Flask(__name__)
@app.route('/')
def get_all_posts():
    print(posts_object)
    return render_template("index.html",blog_post=posts_object)

@app.route("/post/<int:index>")
def display_post(index):
    requested_post=None
    for post_detail in posts_object:
        if post_detail.id == index:
            requested_post=post_detail
    return render_template("post.html",post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
