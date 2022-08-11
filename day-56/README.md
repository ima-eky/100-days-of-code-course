# Personal Blog (templating with jinja)
A simple blog with a number of blog posts.
Jinja is a templating language built for Python,and it allows you create the general layout of your blog.For example,if you had a blog and you wanted to have several different posts in the blog, you don't need to create a separate HTML file for each blog post using jinja.
- You can find a link to the jinja documentation [here](https://jinja.palletsprojects.com/en/3.1.x/)

### Prerequesites
- Install requirements `pip install -r requirements.txt`

### How to run script/development server
- Navigate to project/day's directory
- export FLASK_APP=server.py (if you use windows,use set instead of export)
- To enable development features,export the FLASK_ENV environment variable and set it to development (export FLASK_ENV=development) before running the server.
- python3 server.py
- or flask run

### Output expected
<img src="https://github.com/ima-eky/100-days-of-code-course/blob/main/img/simple_blog.png" title="Sample image" />

