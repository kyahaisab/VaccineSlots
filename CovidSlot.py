import bs4
import requests
import json

month="06"
start_date=12
end_date=20
while start_date<end_date :

   url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=624&date="+str(start_date)+"-"+month+"-2021"

   data=requests.get(url)

   soup=bs4.BeautifulSoup(data.text,'html.parser')
   json_result = json.loads(str(soup))

   for x in json_result["sessions"]:
       print(x)
       print(x['date'])
       print(x['name'])
       print(x['state_name'])
       print(x['pincode'])
       print(x['fee_type'])
       print(x['min_age_limit'])
       print(x['vaccine'])
       ans=str(x['district_name'])
       print(x['available_capacity'])
      # print(ans)
       print("\n")

   start_date=start_date+1


