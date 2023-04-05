import requests
response=requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
#if(response.status_code != 200)
    #rasie Exception("Bad response from ISS")
#print(response.status_code)
response.raise_for_status()
data = response.json()["iss_position"]
print(data)
data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (longitude, latitude)
print(iss_position)