from apscheduler.schedulers.blocking import BlockingScheduler
from app.models import UsersProfile
from datetime import datetime, time, timedelta
from app import YahooWeather
from app import GoogleLocator
from app import Twilio

##This is a Scheduler that requires deployment to Heroku
#this module is defined in Profile and ran by a Heroku Scheduler
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=10)
def timed_job():
    users = UsersProfile.query.all()
    for user in users:
        if needs_message_now(user):
            try:
                sent = send_forecast(user)
            except Exception as e:
                pass


    def needs_message_now(user):
        utc_now = datetime.utcnow()

            #format is ##:## ##
        time = user.time.split(":")
        temp = time[1].split(" ")

        hour = time[0]
        minute = temp[0]
        day_night = temp[1]

        today = datetime.today()
        todays_desired_alarm_time = datetime(
            hour=int(hour),
            minute=int(minute),
            year=today.year,
            month=today.month,
            day=today.day
        )

        #incase app doesn't run exactly every 10 minutes....
        margin_of_error = timedelta(seconds=60*9)  # 9 minutes in either direction 
        if utc_now - margin_of_error < todays_desired_alarm_time: #< utc_now + margin_of_error:
            return True


    def send_forcast(user):

        #magic number
        TEMPERATURE = 1
        CONDITIONS = 2
        HIGH = 3
        LOW = 4
        IMAGE= 5
        LOCTION = 6

        #Get Objects for weather and loction
        weather = YahooWeather.Weather()
        location = GoogleLocator.GeoCodingClient()

        #get Lat and Lon for specfic lociton
        data = location.lookup_location(str(user.location))

        #get weather based off lat and lon
        jsonobject = weather.get_forecast(location.Current_Location(data,1),location.Current_Location(data,2))

        weather = {
                'city' : weather.Current_Weather(jsonobject,LOCTION),
                'temperature' : weather.Current_Weather(jsonobject,TEMPERATURE),
                'description' : weather.Current_Weather(jsonobject,CONDITIONS),
            }

        message = "the current weather in " + weather.city + " is " + weather.temperature + " conditions: " + weather.description
        Twilio.send_message(user.phoneNumber, message)

sentry.captureException()

sched.start()







