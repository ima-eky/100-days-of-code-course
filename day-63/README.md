# Creating a Virtual Bookshelf
This is good for you if you ever wanted to keep track of the books you/others have read and give each book a rating.
- You'll need to create an SQLite database(using SQLAlchemy),then create, read, update and delete data (CRUD OPERATIONS)in the database.Then,connect your database with a Flask application
 to serve data whenever needed
- Here's more on URL Building: [https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask](https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask) , [https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building](https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building)

- SQLAlchemy is defined as an ORM Object Relational Mapping library. This means that it's able to map the relationships in the database into Objects.
- Tables can be defined as separate Classes and each row of data is a new Object.[Here's](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application) more documentation on SQLAchemy
- The main aim of this project is to get grasp of CRUD OPERATIONS.(You can always improve the front-end aspect of this project)


### Prerequesites
- Install requirements `pip install -r requirements.txt`

### How to run script/development server
- Navigate to project/day's directory
- export FLASK_APP=main.py (if you use windows,use set instead of export)
- To enable development features,export the FLASK_ENV environment variable and set it to development (export FLASK_ENV=development) before running the server.
- python3 main.py
- or flask run

### Output expected

![virtual_library](https://user-images.githubusercontent.com/101118595/184414721-9c347b1a-71fe-43f2-be26-02b78c42e7c9.png)

