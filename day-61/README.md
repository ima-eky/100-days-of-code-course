#  Building Advanced Forms
- You're going to build forms using a Flask extension called Flask-WTF.It has a number of benefits over the simple HTML Form
######
For example:
- Easy [Form Validation](https://wtforms.readthedocs.io/en/2.3.x/validators/#module-wtforms.validators):Makes sure the user is entering data in the required format in all the required fields
- Easy display of [errors](https://wtforms.readthedocs.io/en/2.3.x/crash_course/#displaying-errors)
- Easier to get hold of the form [data](https://wtforms.readthedocs.io/en/2.3.x/crash_course/#how-forms-get-data)
- Less Code(You should not create any <label> or <input> elements manually using HTML.).[https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields](https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields)
- Built in CSRF(Cross Site Request Forgery) Protection:it's an attack that can be made on website forms which forces your users to do unintended actions
 #
- The website in this script, that holds some secrets. Only with the right username and password can you access the page with our secrets.
- Creating [WTForms](https://flask-wtf.readthedocs.io/en/1.0.x/form/)
- [Inheriting Templates Using Jinja2](https://svn.python.org/projects/external/Jinja-1.1/docs/build/inheritance.html)

### Prerequesites
- Install requirements `pip install -r requirements.txt`
- We are installing Flask-Bootstrap to use [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html) as an Inherited Template.Also,
 Flask-Bootstrap has one of the most convenient methods for [generating forms](https://pythonhosted.org/Flask-Bootstrap/forms.html) with WTForms

### How to run script/development server
- Navigate to project/day's directory
- export FLASK_APP=main.py (if you use windows,use set instead of export)
- To enable development features,export the FLASK_ENV environment variable and set it to development (export FLASK_ENV=development) before running the server.
- python3 main.py
- or flask run

### Output expected
 
![wtf_forms](https://user-images.githubusercontent.com/101118595/184462832-d58783c9-e5c0-4fe6-afad-712a0d04d4d6.png)
