from flask import Flask,render_template,request
import requests,smtplib
from post import Post

# using requests to get blog data
response=requests.get("https://api.npoint.io/2b98e8835e979b3f55c4")
data=response.json()
posts_object=[]

# Fill in details for it to work
EMAIL ="YOUR OWN EMAIL ADDRESS"
PASSWORD ="YOUR EMAIL ADDRESS PASSWORD"

for post in data:
    post_data=Post(post['id'],post['title'],post['subtitle'],post['body'],post['author'],post['date'])
    posts_object.append(post_data)

app = Flask(__name__)

# Creating  different routes using the app.route decorator
@app.route('/')
def home_page():
    return render_template('index.html',all_post=data)


@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/contact",methods=['POST','GET'])

def contact():
    if request.method == "POST":
        data = request.form
        send_email(data['username'],data['user_email'],data['phone_number'],data['yourMessage'])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name,email,phone,message):
    email_message=f"Subject:New Message\n\nName:{name} \nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=email,
                            msg=email_message)
@app.route("/<int:index>")
def display_post(index):
    requested_post=None
    for post_detail in posts_object:
        if post_detail.id == index:
            requested_post=post_detail
    return render_template("post.html",post=requested_post)



if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)