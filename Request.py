import requests


params = {'q' : 'search'}
headers = {'Accept-Language':'ko','Accept-Encoding' : 'gzip' }
res = requests.get('http://search.debian.net/org', params=params, headers = headers)

print(res.url)
print(res.content)
print(res.headers)
