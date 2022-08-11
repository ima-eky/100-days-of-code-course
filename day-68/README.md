# Login and Registering Users with Authentication

To have users and associate data to user accounts, we need a way to register them and allow them to sign back into their accounts at a later date.
In this script, user  authentication is implemented which figures out how to register, login and logout users with email and password. So they can access
their own private profile pages.

### Prerequesites
- Install requirements `pip install -r requirements.txt`

### How to run script/development server
- Navigate to project/day's directory
- export FLASK_APP=server.py (if you use windows,use set instead of export)
- To enable development features,export the FLASK_ENV environment variable and set it to development (export FLASK_ENV=development) before running the server.
- python3 main  .py
- or flask run

### Output expected

![unauthorized](https://user-images.githubusercontent.com/101118595/184258337-72d07dd9-20b5-423c-94a3-9571f5cc2e14.png)
![login_authentication](https://user-images.githubusercontent.com/101118595/184258353-6d56c2c2-e927-4de3-ba15-7e1165f5b458.png)
