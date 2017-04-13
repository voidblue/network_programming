import json

l = ['s','t','r']
l =json.dumps(l)
print(l[0])

l = json.loads(l)
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
print(d_raw)
d_raw = {int(key) : value for key, value in d_raw.items()}
print(d_raw)