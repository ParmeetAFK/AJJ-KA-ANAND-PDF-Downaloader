import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import date

def connection(url='http://www.google.com/', timeout=5):

	# --------------------------------- Checks Internet Connection -----------------

    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("You're connected to internet\n")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def build_url():

    #------------------------------- Builds URL for todays Newspaper ---------------------------

    u0 = "http://aajkaanand.epapers.in/index.php?edition=Ppage&date="

    date_today = str(date.today())

    u1 = date_today + "&page="

    u2 = u1 + '2'

    url = u0 + u2

def visit_site(url):
    



build_url()