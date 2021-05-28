from twilio.rest import Client

account_sid = "AC7a921870348e01d1695c3b44a49627e3"
auth_token = "6d6cdbcf11b3bfbba96dca5fbff0f504"
client = Client(account_sid, auth_token)
msg = "Preety cool "+"love you boy"
for i in range(2):
   client.messages.create(from_="+15868008247",body=msg, to="+917355182778")

#lets say you made a bot that will send msg to user when you met given share price condition:
#you applied search algo on web pages and when you got that send msg
# Acc used is sagardawn14...........
#Pass : Mao.......