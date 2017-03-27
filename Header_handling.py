from urllib.request import urlopen
from urllib.request import Request

# 리퀘스트로 헤더 조작하기기
req = Request('http://www.github.com')

encodings = 'deflate . gzip, identity'  #안돼면 앞에서부터 차례대로

req.add_header('Accept-Language','ko')         #Contents negotiation
req.add_header('Accept-Encoding',encodings)
req.add_header('User-agent', 'no no no no no Mozilla/5.0 (X11; Linux x86_64')   # rv:24.0 Geclp/20140722 Firefox/24.0')

print(req.header_items())
print(req.get_header('User-agent'))
response = urlopen(req)
format= response.getheader('User-agent')
print(format)
