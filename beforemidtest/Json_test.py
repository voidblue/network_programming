import json

l = ['s','t','r']
l =json.dumps(l)    #리스트 모양을 그대로 문자열로 변환
print(l[0])

l = json.loads(l)     #문자열을 다시 리스트나 딕셔너리형태로 변환
print(l[0])

dic = {'a' : 'apple', 'b' : 'banana'}
dic = json.dumps(dic)
print(dic)
print(dic[0])

dic = json.loads(dic)
print(dic)
print(dic['a'])


j = json.dumps({1:10, 2:20, 3:30})
d_raw = json.loads(j)
print(d_raw)              #키값이 상수였는데 문자열로 변 한것 을 알수있다.
d_raw = {int(key) : value for key, value in d_raw.items()}    #따로 수정해주는 방법
print(d_raw)