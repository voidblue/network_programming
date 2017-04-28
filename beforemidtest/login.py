from urllib.request import Request, urlopen
from urllib.parse import urlencode,urljoin
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor


data_dict = {'id':'kimqwe12300', 'qw' : ''}
data = '?' + urlencode(data_dict)   #딕셔너리를 '키=값'의 스트링 형태로 변환
print(data)
url = urljoin('https://logins.daum.net/accounts/loginform.do?url=http%3A%2F%2Fwww.daum.net%2F%3Fnil_top%3Dmobile/',data)
res = Request(url)
print(res.full_url)         #리퀘스트 url출력

cookie_jar = CookieJar()
opener = build_opener(HTTPCookieProcessor(cookie_jar))
opener.open(res)

cookies = list(cookie_jar)
print(len(cookie_jar))
for i in cookies:
    print(i.secure)
    try:
        print(i.get_nonstandard)
    except:
        pass
