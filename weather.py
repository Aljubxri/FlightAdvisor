import requests


class weather:
    api_key = "df41e917a7b76258a4ae8016fe219073"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # https://openweathermap.org/current is the API documentation



    def askinput(self):
        location = input("Please enter your location of interest (City)")
        unit_type = input("What unit you would like your report in? Please enter C or F")
        location = location.strip()
        unit_type = unit_type.strip()
        return self.temp(unit_type, location)

    def temp(self,unit,city):

        # For text parsing the unit
        if unit == 'C' or unit == 'c':
            unit = "metric"
        elif unit == 'F' or unit == 'f':
            unit = "imperial"
        else:
            print("Error input C or F")
            pass
        c_or_f = unit.capitalize() + "°"

        # API call
        complete_url = self.base_url + "&q=" + city + "&units=" + unit + "&appid=" + self.api_key
        response = requests.get(complete_url)
        jason = response.json()
        jason_main = jason["main"]  # main branch
        jason_weather = jason["weather"]  # weather branch

        # Return statement
        print("The weather in " + city + " looks like " + jason_weather[0]["description"] + " with " + str(jason_main["temp"]) + c_or_f)


