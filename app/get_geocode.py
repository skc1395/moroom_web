import requests

kex = "a661789ae59ebe02ffc541fcf37ae534"
def Get_geocode(address, key):
 
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    headers = {'Authorization': 'KakaoAK {}'.format(key)}
    data = {'query': address}
    req = requests.get(url, headers=headers, data=data)
    
    response = req.json()
    lng = response['documents'][0]['address']['y']
    lat = response['documents'][0]['address']['x']
   
    return (lng,lat)




# print(Get_geocode('대구광역시 북구 복현동 597-33', kex))