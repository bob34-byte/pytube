import requests
from requests_html import HTMLSession
 
url = "https://www.google.com/"
 
try:
    session = HTMLSession()
    response = session.get(url)
     
except requests.exceptions.RequestException as e:
    print(e)
