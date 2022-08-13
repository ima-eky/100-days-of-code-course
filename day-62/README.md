# Coffe & Wifi Project
- Coffe & Wifi Project consists of cafes that you can  remote-work (stored in a CSV).  
- There's a secret route "/add" which doesn't have a button, but those in the know should be able to access it to add cafes to csv data
- [WTForms](https://pythonhosted.org/Flask-Bootstrap/forms.html) is used to  create a quick_form.You can be sure that entered data is valid( for 
example ,that URL given is a URL [https://wtforms.readthedocs.io/en/2.3.x/validators/](https://wtforms.readthedocs.io/en/2.3.x/validators/), 
[https://stackoverflow.com/questions/41300647/wtforms-disable-client-side-validation-on-cancel/61166621#61166621](https://stackoverflow.com/questions/41300647/wtforms-disable-client-side-validation-on-cancel/61166621#61166621))
- When the user successfully submits the form ,the data get's appended to end of CSV file
- Refresher on working with csv [files](https://www.w3schools.com/python/python_file_write.asp)
 
 
 
### Prerequesites
- Install requirements `pip install -r requirements.txt`

### How to run script/development server
- Navigate to project/day's directory
- export FLASK_APP=main.py (if you use windows,use set instead of export)
- To enable development features,export the FLASK_ENV environment variable and set it to development (export FLASK_ENV=development) before running the server.
- python3 main.py
- or flask run

### OutPut Expected

 ![cofee_wifi_project](https://user-images.githubusercontent.com/101118595/184419124-4af13b92-47c5-4623-99bc-553d48c1766a.png)
