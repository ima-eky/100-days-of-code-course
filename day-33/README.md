# International Space Station (ISS) OverHead Notifier
This project tries to track where the ISS is currently at in the sky. And at the time point when the ISS is in the night sky, right above where we are,then we're going to send ourselves an email telling us to look up and spot the fast-moving ISS.

 ## Libraries used
 - Email SMTP  (a module that comes pre-bundled with Python and  helps us send email using Python code.(`import smtplib`))
 - pandas
 - datetime (from datetime import datetime)
 - requests (import requests)
The script deals with the conventions for Gmail.com.If you use another email provider,, just Google for your email provider e.g. "Gmail SMTP address" and port number
- You can get your longitude and latitude from [here](https://www.latlong.net/)
- Sunset and sunrise API [Documentation](https://sunrise-sunset.org/api)
- ISS [Current Location](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
-Read More  on HTTP response status code(https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
-[Python Request Module](https://www.w3schools.com/python/module_requests.asp)

## How to run script
Open your terminal

Navigate to the project and day's directory

Run the script

`python main.py`

## Output expected
- Email gets sent
- No error when program is sent
https://www.w3schools.com/python/module_requests.asp<br><img src="https://github.com/ima-eky/100-days-of-code-course/blob/main/img/iss_notifier.png" title="Sample output of when script is run">
