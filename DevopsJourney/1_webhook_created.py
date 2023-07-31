# Visit https://webhook.site/ to get a free webhook url

import requests
import json
 

webhook_url = 'https://webhook.site/c6ab812b-988c-4783-81d4-27e907752d8c'
data = {
    'name' : 'Sachin',
    'city' : 'Singapore'
}

r = requests.post(webhook_url,data=(data),headers={'Content-Type': 'application/json'})



