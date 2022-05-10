from email import message
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    countries_url = "https://restcountries.com/v3.1"
    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    capital= dic.get("capital")
    country = dic.get("country")

    # find country from capital
    if capital:
      url = f"{countries_url}/capital/{capital}"
      res = requests.get(url)
      data = res.json()
      country = data[0]["name"]["common"]

      message = f"The capital of {country} is {capital}."
    
    # find capital from country
    elif country:
      url = f"{countries_url}/name/{country}"
      res = requests.get(url)
      data = res.json()
      capital = data[0]["capital"][0]
    
      message = f"The capital of {country} is {capital}."
    else:
      message = "Error 404: Not Found!"
    
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()  
    self.wfile.write(message.encode())
    return
