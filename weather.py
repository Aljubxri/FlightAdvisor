import requests
import bs4
import flightFinder


class weather:
    api_key = "-API KEY GOES HERE-"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Uses Openweathermap API for current data, the api_key has been redacted for privacy purposes
    # https://openweathermap.org/current is the API documentation

    # This function gets all the input needed from the user and will make a flightFinder object if needed
    def askinput(self):
        what_do_you_want = input("Would you like to see the weather by flight number or city?(Enter 'city' or 'flight')")
        unit_type = input("What unit you would like your report in? (Enter 'C' or 'F')")

        if what_do_you_want == "city":
            location = input("Please enter your city of interest (USA):")
            location = location.strip()  # Parses input so errors are not given
            unit_type = unit_type.strip()
            self.temp(unit_type, location)

        elif what_do_you_want == "flight":
            flightnumber = input("Please enter the flight number:")
            flight1 = flightFinder.flightFinder(flightnumber)
            location = str(flight1.destination_city()[1][1])    # finds the destination of flight using beautifulsoup4

            infotype = input("Would you also like to see current flight details? (Y/N)")
            if infotype == "Y" or infotype == 'Y':
                if flight1.destination_city()[0]:   # shows the flight details, like when it arrives and where etc
                    flight1.flightinfo()
                    self.temp(unit_type,location)

    # Connects to openweathermap api to bring the current weather from the destination city
    def temp(self,unit,city):

        # For text parsing the unit
        if unit == 'C' or unit == 'c':
            unit_u = "metric"
        elif unit == 'F' or unit == 'f':
            unit_u = "imperial"
        else:
            print("Error input C or F")
            pass
        c_or_f = unit.capitalize() + "°"

        # API call
        complete_url = self.base_url + "&q=" + city + "&units=" + unit_u + "&appid=" + self.api_key
        response = requests.get(complete_url) # the following code parses the JSON of the api call in order to get data
        jason = response.json()
        jason_main = jason["main"]  # main branch
        jason_weather = jason["weather"]  # weather branch

        # Return statement
        print("The weather in " + city + " looks like " + jason_weather[0]["description"] + " with " + str(jason_main["temp"]) + c_or_f)


