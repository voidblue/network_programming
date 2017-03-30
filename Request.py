import requests



prrams = {'action' : 'search', 'term' : 'Are you quite '}
res = requests.get('http://www.debian.org')


print(res.status_code)
print(res.encoding)


#request로 해서 검색하는거 해볼것