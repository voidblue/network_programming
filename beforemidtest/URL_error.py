from urllib.request import urlopen
import urllib.error


try:
    response = urlopen("http://www.ietf.org/rfc/rfc0.txt")   #
    # response = urlopen("http://192.0.2.1/index.html")   #시간 없어서 못받아옴
except urllib.error.HTTPError as e:
    print('status : ',e.code)                   #상테코드 출력
    print('url : ',e.url)                       #에러 url출력
    print('reason : ',e.reason)                 #에러 이유 출력 (상태코드 설명???)












# e1 = response.status   #상태 읽어오기
# e2 = response.readline() #
# e3 = response.read()
# print('status : ',e1)
# print('readline : ',e2)
# print('read : ',e3)


