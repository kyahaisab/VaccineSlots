import bs4
import requests
import json

#*****************************Code to find district_id of different states and cities etc

ide=1
ans=""
while 0>-1 :
    ide=ide+1
    url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+str(ide)+"&date=31-03-2021"

    data=requests.get(url)

    soup=bs4.BeautifulSoup(data.text,'html.parser')
    json_result = json.loads(str(soup))

    for x in json_result["sessions"]:
       #print(x)
       print(str(ide)+".")
       print(x['state_name'])
       print(x['pincode'])
       #ans=str(x['state_name'])
       ans=str(x['district_name'])
       print(ans)
       print("\n")
       break

    if ans=="Prayagraj" :
        break

print(ide)

#************************NOTE*****************

#Prayagraj district_id is 624