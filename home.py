import requests
from requests_html import HTMLSession
 
url = "https://www.searchenginejournal.com/introduction-to-python-seo-spreadsheets/342779/"
 
try:
    session = HTMLSession()
    response = session.get(url)
     
except requests.exceptions.RequestException as e:
    print(e)
