import requests
session  = requests.Session()
session.get('http://httpbin.org/cookies/set/number/123456789')
r = session.get('http://httpbin.org/cookies')
print(r.text)