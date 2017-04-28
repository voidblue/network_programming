from urllib.request import Request, urlopen
from urllib.parse import urlencode,urljoin

data_dict = {'q':'Python'}
data = 'search?' + urlencode(data_dict)   #딕셔너리를 '키=값'의 스트링 형태로 변환
print(data)
url = urljoin('http://search.daum.net/',data)
req = Request(url)
print(req.full_url)         #리퀘스트 url출력

print(req.get_header('Content-Type'))
res = urlopen(req)
print(res.getheader('Content-Type'))
print(res.read())