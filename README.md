# WeatherAlert

#### Description:

WeatherAlert – A simple web app that displays the users current weather and sends text messages of the weather. The user will be
able to put in their location, phone number and time of alert. The web app will send a text message saying the current weather
for that day. 

Technology stack – Twilio, Yahoo Weather API, Google Geolocator, Python, Django, GitHub, Visual Studio 2017, Heroku


#### Try it out yourself!

To run this application on your own local server
1. Pull Code off GitHub
2. pip install Django==2.1.4
3. download python... (3.6.0)
4. pip install requests (2.20.1)
5. python /your_local_path/manage.py runserver


#### Test:
Once your on the application, go to the top right and create an account
1. Click Register
2. Fill out application - you can try typing in wrong information but application will stop you!
3. wait a few second to receive a code on your phone
4. check out the weather tab and profile tab!

#### NOTE:
There are a few things I did not complete. One, the morning texts are only able to be sent when website is running on Heroku.
The reason for this is because this application uses a Heroku Scheduler which runs a scripts every 10 minutes. Sadly I did not 
have time to troubleshoot issues with hosting my website :(. However keep checking in and hopefully I will have something 
working by the end of the week!

#### IMPORTANT!!!!:
DO NOT put in false phone numbers, this application will text you! Don't let others get your security code text!!!
ALSO: The only way this application will work is if you have the secret key. I will keep these in my applications for the
weekend, BUT they will be changed so I don’t get charged for unnecessary API calls!!!




