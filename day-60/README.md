# Making the Contact Form Work (from day-59)
-  For the contact form in our blog to work,you'll need to understand how HTML forms are submitted 
and how to use the data from the form to actually send an email to ourselves with the data submitted by the user(You might need to review script on smtplib from Day 32.)
- [HTML <form> action Attribute](https://www.w3schools.com/tags/att_form_action.asp)
- [HTML <form> method Attribute](https://www.w3schools.com/tags/att_form_method.asp)
- Sending data from HTML form to a [Python script](https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask) 
  in [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object).
  
 ### Prerequesites
- `pip install flask`

### How to run script/development server
- Navigate to project/day's directory
- export FLASK_APP=main.py (if you use windows,use set instead of export)
- To enable development features,export the FLASK_ENV environment variable and set it to development (export FLASK_ENV=development) before running the server.
- python3 main.py
- or flask run

### Output expected
- Code should get hold of the name and password that was entered into the form and send it back to the client as a h1(heading).

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
