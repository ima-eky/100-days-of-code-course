# Build Your Own REST API Service from scratch using Flask.
- REST (REpresentational State Transfer) is an architectural style for designing APIs.There's a lot of rules for making an API RESTful.But the two  most important ones are using the HTTP request verbs and a specific pattern of routes and endpoint URLs.
- The database consists of a bunch of cafes to remote-work (you'll have to also consider the database CRUD functions)
- How to return a [JSON](https://www.adamsmith.haus/python/docs/flask.jsonify) of required data.
- Postman - The all in one API Testing Tool,allows you to create [documentation](https://learning.postman.com/docs/publishing-your-api/documenting-your-api/) for your API and also test your API.
- Make sure that you've made each of the requests and they work as you expect before building your documentation. 
-  You can download it [here](https://www.postman.com/downloads/) for free.
-  Here's a [link](https://documenter.getpostman.com/view/22470891/UzkV1vsF) to my documentation for my API service(It explains how to make requests and results you get by making ceratin requests.).

### Prerequesites
- Install requirements `pip install -r requirements.txt`

### How to run script/development server
- Navigate to project/day's directory
- export FLASK_APP=main.py (if you use windows,use set instead of export)
- To enable development features,export the FLASK_ENV environment variable and set it to development (export FLASK_ENV=development) before running the server.
- python3 main.py
- or flask run


