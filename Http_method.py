from urllib.request import Request, urlopen
from urllib.parse import urlencode,urljoin

data_dict = {'q':'Python'}
data = '?' + urlencode(data_dict)
print(data)
url = urljoin('https://search.debian.org/',data)
req = Request(url)
print(req.full_url)

req.add_header('Content-Type', "application/x-www-form-urloncode; charset=utf-16")

print(req.get_header('Content-Type'))
res = urlopen(req)
print(res.getheader('Content-Type'))

print(res.read())