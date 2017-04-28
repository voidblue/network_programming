from urllib.parse import urlparse, urljoin, parse_qs

result = urlparse('http://www.python.org/dev/peps')
print(result)

print(result.netloc)
print(result.path)
print(result.port)

print(urlparse('http://www.python.org:8080'))


join = urljoin('http://www.debian.org', 'intro/about')
print(join)

join2 = urljoin('http://www.debian.org/intro/about/' , '../News')

join4 = urljoin('http://www.debian.org/intro/about/' , '../../News')
print(join2)
print(join4)

join3 = urljoin('http://www.debian.org/about', 'http://www.python.org')
print(join3)

target = urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default')
xxx = parse_qs(target.query)                    #쿼리를 parse해서 보여준다.
print(xxx)