import requests


params = {'q' : 'python'}
headers = {'Accept-Language':'ko','Accept-Encoding' : 'gzip' }
res = requests.get('https://www.debian.org', params=params, headers = headers)

print(res.url)
print(res.content)
print(res.headers)
