import requests

class weather:
    api_key = "df41e917a7b76258a4ae8016fe219073"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # https://openweathermap.org/current is the API documentation



    def __init__(self, city):
        self.city = city

    def temp (self,unit):
        self.unit = unit
        c_or_f = unit.capitalize() + "°"

        if unit == 'C' or unit == 'c':
            unit = "metric"
        elif unit == 'F' or unit == 'f':
            unit = "imperial"


        complete_url = self.base_url + "&q=" + self.city + "&units="+ unit + "&appid=" + self.api_key

        response = requests.get(complete_url)
        jason = response.json()
        jason_main = jason["main"]  # main branch
        jason_weather = jason["weather"]  # weather branch
        print("The weather in " + self.city + " looks like "+ jason_weather[0]["description"] + " with " + str(jason_main["temp"]) + c_or_f)


