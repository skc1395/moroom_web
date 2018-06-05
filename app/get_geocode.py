import requests


def Get_geocode(address, key):
 """
 사용자가 주소 입력시, DB에 저장하기 전 view단에서 damm map api를 이용해서
 주소값을 올바른 경도, 위도 값으로 변환후, db에 저장해준다.

 만약 주소값에 오류가 있다면 -> api 요청 결과, 빈 리스트이면(IndexError)
 lng와 lat 값으로 0으로 주고, 사용자가 입력한 문(gate)의 위도와 경도값을 저장한다.
 
 """
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    headers = {'Authorization': 'KakaoAK {}'.format(key)}
    data = {'query': address}
    req = requests.get(url, headers=headers, data=data)
    
    
    response = req.json()
    
    try:
        lng = response['documents'][0]['address']['y']
        lat = response['documents'][0]['address']['x']

    except IndexError:
        lng = 0
        lat = 0
   
    return (lng,lat)