
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor



cookie_jar = CookieJar()
opener = build_opener(HTTPCookieProcessor(cookie_jar))
opener.open('http://www.github.com')

cookies = list(cookie_jar)
print(len(cookie_jar))
for i in cookies:
    print(i.secure)


    print(i.get_nonstandard)
