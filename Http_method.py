from urllib.request import Request, urlopen
from urllib.parse import urlencode,urljoin

data_dict = {'q':'Python'}
data = 'search?' + urlencode(data_dict)
print(data)
url = urljoin('http://search.daum.net/',data)
req = Request(url)
print(req.full_url)

print(req.get_header('Content-Type'))
res = urlopen(req)
print(res.getheader('Content-Type'))
print(res.read())