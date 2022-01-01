import bs4
import requests

class flightFinder:
    url = "https://www.google.com/search?q="    #Scrapes information from google using beautifulsoup4

    def __init__(self, flight): # takes in flight number when creating this object
        self.flight = flight
        pass

    def flightinfo(self): # uses a html parser to find the correct location of where the data will be
        url = self.url + self.flight
        request_result = requests.get(url)
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
        class_info = soup.findAll("div", class_="BNeawe")
        class_info = class_info[2].text
        # Finds destination airport from Flight number
        print(class_info)

    def destination_city(self): # From the data taken, this will parse to find the destination city
        url = self.url + self.flight
        request_result = requests.get(url)
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
        class_info = soup.findAll("div", class_="BNeawe")
        class_info = class_info[2].text
        split_String = class_info.strip().split()

        #finds the index for "arrives ___"
        city_found = False
        for word in range(3,len(split_String)):
            if split_String[word] == "Arrives":
                city_index = split_String[word:word+2]
                city_found = True

        return [city_found, city_index] # returns if a city is found, and the city name








