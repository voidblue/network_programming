from urllib.request import urlopen
from urllib.request import Request

req = Request("http://www.google.com")

res = urlopen(req)
print(res)
# print(res.readline())
# print(res.read())
print(res.url)
# print(res.status)
# print(res.getheaders())
try:
    print(req.redirect_dict)
except:
    print("리다이렉션 없음")
