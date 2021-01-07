from pyngrok import ngrok
import requests
import os
import time
import sys
http_tunnel = ngrok.connect(8080).public_url
print(http_tunnel)
time.sleep(5)
params = (
    ('fid', '124pjM5LggSuwI1n40bcD5tQ13wS0M6wg'),
)
response1 = requests.get(http_tunnel+'/api/gdurl/count', params=params)
print(response1)
files = {
    'url': (None, http_tunnel+'/api/gdurl/tgbot'),
}
response2 = requests.post('https://api.telegram.org/bot'+sys.argv[1]+'/setWebhook', files=files)
print(response2)
while True :
	continue
