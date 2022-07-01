# Rain Alert
This program is going to send you a text message in the morning, just before you head out, telling you to bring an umbrella if it's going to rain in the day(So this way you don't have to check the weather.An API like Twilio would be used to send SMS messages to ourselves or you can send yourself a mail.
Read on [Running your code in the cloud](https://github.com/ima-eky/100-days-of-code-course/blob/main/running_your_code_in_the_cloud) if you don't have a platform to run your code on cloud

- Current Weather Data [Documentation](https://openweathermap.org/current).Also ,[here](https://openweathermap.org/api/one-call-api)
- Sign in or create new account for [Open Weather Map](https://home.openweathermap.org/users/sign_in) to get API keys
- Find your longitude and latitude [here](https://www.latlong.net/)
- You can use json online viewer to view data in a better [form](http://jsonviewer.stack.hu/)
- Open Weather Condition [Codes](https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2) to know how to detect when it is raining
- Sign up for [Twilio](https://www.twilio.com/try-twilio) to be able to send SMS with your account S-ID and auth token/You don't have to sign up if you are going to send yourself an email.(Go back to day-32 if you need help sending yourself an email)
- SMS python [documentation](https://www.twilio.com/docs/sms/quickstart/python) using Twilio

How to get Twilio work on [Python everywhere](https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/)

## Library used
- requests(Run `python -m pip install requests` to install requests,then `import requests`in your code)
 ### How to run script
Open your terminal

Navigate to the project and day's directory

Run the script

`python main.py`

<br><img src="https://github.com/ima-eky/100-days-of-code-course/blob/main/img/rain_alert.jpeg" title="Sample"/>
