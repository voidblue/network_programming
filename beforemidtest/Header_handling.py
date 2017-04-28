from urllib.request import urlopen
from urllib.request import Request

# 리퀘스트로 헤더 조작하기기
req = Request('http://www.debian.org')

encodings = 'deflate, gzip, identity'  #안돼면 앞에서부터 차례대로

req.add_header('Accept-Language','ko')     #헤더에 언어정보를 ko로 변경
req.add_header('Accept-Encoding','gzip')   #인코딩 형식을 gzip으로 변경
req.add_header('User-Agent', 'I am voidblue')   # User-Agent를 변경

print(req.header_items())                   #리퀘스트의 모든 헤더 출력
print(req.get_header('User-agent'))         #리퀘스트 헤더 중 User-agent속성의 값 출력
res = urlopen(req)
format = res.getheader('Accept-Language','ko')
print(res.status)                           #response의 상태 출력 200 정상,404에러 등등
print(format)
format = res.getheader('User-Agent')
print(format)
