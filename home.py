import requests
from requests_html import HTMLSession
 
url = "https://bob34-byte.github.io/pytube/vid"
 
try:
    session = HTMLSession()
    response = session.get(url)
     
except requests.exceptions.RequestException as e:
    print(e)
