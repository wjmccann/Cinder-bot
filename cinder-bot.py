import pynder
import cleverbot
import time
import requests

cb = cleverbot.Cleverbot()
	
FB_USER_ID = <USER ID>
FB_USER_TOKEN = <ACCESS TOKEN>

#getToken(FB_APP_ID, FB_APP_SECRET)

#print(FB_USER_TOKEN)

session = pynder.Session(FB_USER_ID, FB_USER_TOKEN)
print('Facebook Authentication Success!')

session.update_location(<LAT>, <LONG>)

for user in session.nearby_users():
	user.like()
		
def sendto(match):
	ms = match['messages']
	me = session.profile.id
	if not ms:
		#Message a match first
		#time.sleep(3)
		#session._api._post('/user/matches/' + match['id'],
        #                   {"message": "Hey You, wannna hook up? lol jk"})
		return
	spoken = False
	name = match['person']['name']
	for m in ms:
		if m['from'] == me:
			spoken = False
		else:
			spoken = True
	
	if spoken:
		time.sleep(3)
		text = m['message']
		text = text.encode('ascii', 'ignore').decode('ascii')
		send = cb.ask(text)
		session._api._post('/user/matches/' + match['id'],
                           {"message": send})

while True:
	matches = session._api.matches()
	for m in matches:
		sendto(m)		