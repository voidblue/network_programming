from urllib.request import urlopen
from urllib.request import Request

# 리퀘스트로 헤더 조작하기기
req = Request('http://www.debian.org')

encodings = 'deflate, gzip, identity'  #안돼면 앞에서부터 차례대로

req.add_header('Accept-Language','ko')         #Contents negotiation
req.add_header('Accept-Encoding','gzip')
req.add_header('User-Agent', 'I am voidblue')   # rv:24.0 Geclp/20140722 Firefox/24.0')

print(req.header_items())
print(req.get_header('User-agent'))
res = urlopen(req)
format = res.getheader('Accept-Language','ko')
print(res.status)
print(format)
format = res.getheader('User-agent')
print(format)
