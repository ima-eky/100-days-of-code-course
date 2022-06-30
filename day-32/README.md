# Sending Emails

 This script sends message to a list of recipent.(Though,what was built was a possibly helpful tool where we can automate a happy birthday email to all of our friends and family on their birthdays).
 - There's a birthday.csv file that contains birthdays  and emails of people
 - The code checks if there is any match (the day the code is run) and sends email if there's match.(There are 3 different templates(in leter templates) of letters in (you can add more),and a letter is picked at random,customized for the match and that is what is sent)
You can keeps yours at sending a bulk email to different recipent(,especially if you are not able to run your code in the cloud). 
 ## Libraries used
 - Email SMTP  (a module that comes pre-bundled with Python and  helps us send email using Python code.(`import smtplib`))
 - pandas
 - datetime (from datetime import datetime)
The script deals with the conventions for Gmail.com.If you use another email provider,, just Google for your email provider e.g. "Gmail SMTP address" and port number

## How to run script
Open your terminal

Navigate to the project and day's directory

Run the script

`python main.py`

## Output expected
- Email gets sent
- No error when program is sent

<br><img src="https://github.com/ima-eky/100-days-of-code-course/blob/main/img/send_email.png" title="Sample output of when script is run" width="400"/>
