import bs4
import requests
import json

month="06"
start_date=12
end_date=20
payment_type="Free"      # Either Free or Paid
age_limit=str(45)   # Either 45 or 18

msg_body="Age limit is "+age_limit+" Payment type is "+payment_type+"\n"
flag=0

print("You are seeking vaccine of age above "+age_limit+" and payment type "+payment_type)
print("***********************************************************************\n")
while start_date<=end_date :

   url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=624&date="+str(start_date)+"-"+month+"-2021"
   data=requests.get(url)
   soup=bs4.BeautifulSoup(data.text,'html.parser')
   json_result = json.loads(str(soup))

   for x in json_result["sessions"]:
      if str(x['min_age_limit'])==age_limit and x['fee_type']==payment_type :
          print("Date : "+str(x['date']))
          print("Center Name : "+x['name'])
          print("Address : "+ x['address'])
          print("Pincode : "+ str(x['pincode']))
          print("Vaccine type : "+x['vaccine'])
          print("Slots : "+str(x['slots']))
          print("Dose 1: " + str(x['available_capacity_dose1'])+ "   Dose 2: "+ str(x['available_capacity_dose2']))
          flag=1
          msg_body=msg_body+"\n"+"Date : "+str(x['date'])+",  Center Name : "+x['name']+",  Address : "+ x['address']+",  Pincode : "+ str(x['pincode'])+",  Vaccine type : "+x['vaccine'] +",  Dose 1: " + str(x['available_capacity_dose1'])+ "   Dose 2: "+ str(x['available_capacity_dose2'])
          print("\n")

   start_date=start_date+1

if flag==1 :
    from twilio.rest import Client

    account_sid = "AC35d94ea1c5b8bfb5eb7ce645d16b0154"
    auth_token = "a9a411648302a8611d3a54708f1dfe22"
    client = Client(account_sid, auth_token)
    if len(msg_body)>1500 :
        msg_body=msg_body[0:1500]
    for i in range(1):
        client.messages.create(from_="+15512268221", body=msg_body, to="+917355182778")



