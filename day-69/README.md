# Adding Users to Blog
- The most important component of a website is having users,to have users and associate data to user accounts, we need a way to register them and allow them to sign back into their accounts at a later date. In this script, user  authentication is implemented in our blog (from day-67) in order for blog to have users that can  register/log in and make  comments on blog posts.
- Now only the admin(the first registered user) can create new blog posts, edit posts and delete posts.
- For more on [Hashing Passwords using Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security),[Authenticating Users with Flask-Login](https://flask-login.readthedocs.io/en/latest/) , [Flask Flash Messages](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/),[Passing Authentication Status to Templates](https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/)

### Prerequesites
- Install requirements `pip install -r requirements.txt`

### How to run script/development server
- Navigate to project/day's directory
- export FLASK_APP=server.py (if you use windows,use set instead of export)
- To enable development features,export the FLASK_ENV environment variable and set it to development (export FLASK_ENV=development) before running the server.
- python3 main.py
- or flask run

### Output expected



![adding_users (2)](https://user-images.githubusercontent.com/101118595/184257198-dfdf44b7-1eda-4d32-8071-382efc68d5a7.png)
