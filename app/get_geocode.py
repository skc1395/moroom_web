import requests

def Get_geocode(address,key):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&components=country:KR&key={}'.format(address,key)
    req = requests.get(url)
    response = req.json()
    lng = response['results'][0]['geometry']['location']['lng']
    lat = response['results'][0]['geometry']['location']['lat']
    return (lng,lat)
