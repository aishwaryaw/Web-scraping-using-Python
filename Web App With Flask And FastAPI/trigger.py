import requests

base_url = "http://4ac28d00407e.ngrok.io" #this url changes after ngrok is restarted
ngrok_url = f"{base_url}/scrape"

r = requests.get(ngrok_url)
# print(r.text)
print(r.json()["data"])