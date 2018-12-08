# Design of WeatherAlert


![High Level image](https://github.com/Ncarm828/WeatherAlertFinal/blob/master/WeatherAlert/img/High%20Level%20Diagram.png)
**Template:** The UI for the user where the user will be able to interact with the Web App

**View:** The main hub of all connections. This will receive and send the necessary data based off the response from the Template. The View will also pass data to the Model, connects to the Google API, Yahoo API and Twilio API. 

**Models:** Defines and connects to the database. Currently the Database is connected to a SQLite but with the change of locations in the setting.py, you can connect to a server of your choosing

**Google API:** Connects to Google Geolocator service and gets a response in the form of a json file. The json file has the latitude and longitude of a person when given an address

**Yahoo API:** Connects to Yahoo API service and gets a response in the form of a json file. The json file has the weather forecast when given a latitude and longitude

**Twilio API:** Connects to the Twilio API service. This service will text any person when you provide the service a message and their phone number. 

**Text Dispatcher:** This runs a scheduler that runs every 10 minutes.  It will run through the entire database looking for someone that needs their weather. If some needs their weather, it will get the current weather conditions and send a request to the Twilio API. 



![Low Level image](https://github.com/Ncarm828/WeatherAlertFinal/blob/master/WeatherAlert/img/Low%20Level%20Diagram.png)


