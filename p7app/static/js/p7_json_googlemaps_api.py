import urllib.parse
import requests

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = input('Address: ')

url = main_api + urllib.parse.urlencode({'address': address})
print(url)

json_data = requests.get(url).json()

json_status = json_data['status']
print('API Status : ' + json_status)

if json_status == 'OK':
    location = json_data['results'][0]['geometry']['location']
    print(location)
