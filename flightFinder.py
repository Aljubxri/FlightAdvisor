import bs4
import requests

class flightFinder:
    url = "https://www.google.com/search?q="

    def __init__(self):
        pass

    def flightinfo(self, flight):
        url = self.url + flight
        request_result = requests.get(url)
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
        class_info = soup.findAll("div", class_="BNeawe")
        class_info = class_info[2].text




        # Finds destination airport from Flight number
        print(class_info)