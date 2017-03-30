from urllib.request import Request, urlopen
from urllib.parse import urlencode

data_dict = {'P':'Python'}
data = urlencode(data_dict).encode('utf-8')
req = Request('http://search.debian.org/cgi-bin/omega',data=data)

req.add_header('Content-Type', "application/x-www-form-urloncode; charser='urf-8'")

print(req.get_header('Content-Type'))
res = urlopen(req)
print(res.getheader('Content-Type'))
print(res.read())