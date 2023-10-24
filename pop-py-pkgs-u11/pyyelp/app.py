import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization":"bearer " + config.api_key
}
params = {
    "term":"Barber",
    "location":"NYC"
}
response = requests.get(url=url,headers=headers,params=params,verify=False)#False is used to fix an issue

#print(response.text)

result = response.json()

businesses = response.json()["businesses"]

for business in businesses:
    print(business["name"])

names = [business["name"] for business in businesses if business["rating"] > 4.5]

print(names)