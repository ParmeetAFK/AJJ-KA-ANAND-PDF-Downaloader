import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import date
import datetime

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

    u0 = "aajkaanand.epapers.in/encyc/625/"

    dt = date.today()

    #date_today = str(datetime.date.strftime(dt, "%Y/%m/%d"))

    u1 = '2020/04/12' + "/Ppage_"

    u2 = u1 + '1'

    u3 = '.pdf'

    global url

    url = u0 + u2 + u3


def download_pdf():

    # -------------------- Visits webpage and downloads the pdf file ----------------------------------

    r = requests.get("http://aajkaanand.epapers.in/encyc/625/2020/04/12/Ppage_1.pdf?", allow_redirects=True)
    open('2.pdf' ,'wb').write(r.content)


connection()
build_url()
download_pdf()