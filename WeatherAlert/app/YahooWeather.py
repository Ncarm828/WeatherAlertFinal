import urllib.request as urllib2, urllib
import json

class Weather(object):


    ###   An API for accessing Yahoo Weather   ###
    def __init__(self):
        super(Weather, self).__init__()


    def get_forecast(self,lat,lon):
       
        try:
            #URL Base
            baseurl = "https://query.yahooapis.com/v1/public/yql?"
            #Query
            yql_query = "select * from weather.forecast where woeid in (SELECT woeid FROM geo.places WHERE text='({}, {})') and u = 'f'"
            #Request URL
            yql_url = baseurl + urllib.parse.urlencode({'q':yql_query.format(lat, lon)}) + "&format=json"
            #Open URL
            result = urllib2.urlopen(yql_url).read()
        except urllib2.HTTPError as e:
            return False
        else:
            return result


    #Function that returns parsed json string based off given para
    #input: JsonObject - whole json to be parsed
    #input: ReturnType - what the user wants returned
    #       1 - Current Temp
    #       2 - Current Conditions
    #       3 - Current Temp High
    #       4 - Current Temp Low
    #       5 - Current Conditions Code
    #       6 - Current Location 

    @staticmethod
    def Current_Weather(JsonObject, ReturnType):

        if (ReturnType > 6 ) or (ReturnType < 1):
            return -1

        data = json.loads(JsonObject)
        CommonPath = data['query']['results']['channel']['item']

        result = {
            1:CommonPath['condition']['temp'],
            2:CommonPath['forecast'][0]["text"],
            3:CommonPath['forecast'][0]['high'],
            4:CommonPath['forecast'][0]['low'],
            5:CommonPath['forecast'][0]['code'],
            6:CommonPath['title']
            }.get(ReturnType)

        return result


    #returns Gif based off code that is passed in
    @staticmethod
    def get_GIF(code):

        #Magic numbers are based off yahoo weather code chart for current weathers conditions 
        if int(code) < 1 or int(code) > 47:
            return -1

        #URL Base
        baseurl =  "http://l.yimg.com/a/i/us/we/52/"
        ImagePath = baseurl + code + ".gif"
        return ImagePath                               

