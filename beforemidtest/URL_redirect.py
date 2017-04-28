from urllib.request import urlopen
from urllib.request import Request

req = Request("http://www.google.com")
# req.add_header('Accept-Language','ko')
res = urlopen(req)
print(res.url)

try:
    print(req.redirect_dict)      #리다이렉션된 경로를 모두 출력한다.
except:
    print("리다이렉션 없음")
