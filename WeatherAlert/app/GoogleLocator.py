import urllib.request as urllib2, urllib
import json
import os

class GeoCodingClient(object):
    
    ###    A simple client for Google's GeoCoding API ###

    def __init__(self):
        super(GeoCodingClient, self).__init__()

    def lookup_location(self, location):
        try:
            #URL Base
            baseurl = "https://maps.googleapis.com/maps/api/geocode/json?"
            #Request URL
            yql_url = baseurl + "address=" + location + "&key=" + os.environ.get("GOOGLE_API_KEY")
            #Open URL
            result = urllib2.urlopen(yql_url).read()
        except urllib2.HTTPError as e:
            return False
        else:
            return result

    #Function that returns parsed json string based off given para
    #input: JsonObject - whole json to be parsed
    #input: ReturnType - what the user wants returned
    #       1 - lat
    #       2 - lon

    @staticmethod
    def Current_Location(JsonObject, ReturnType):

        
        if (ReturnType > 2 ) or (ReturnType < 1):
            return -1

        data = json.loads(JsonObject)
        CommonPath = data['results'][0]['geometry']['location']

        result = {
            1:CommonPath['lat'],
            2:CommonPath['lng'],
            }.get(ReturnType)

        return result
