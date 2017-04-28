import boto
from boto.s3.connection import Location
from boto.s3.key import Key

f = open('ID.txt')
access_id = f.read()
f = open('Key.txt')
access_key = f.read()

conn = boto.connect_s3(access_id, access_key) #id와 키로 간단하게 s3로 접속이 가능하다.
xx = '중간고사'.encode('utf-8')

conn.create_bucket('중간', location = Location.APSoutheast2)  #버킷만들기
x = None
print([x for x in dir(Location) if x.isalnum()])

buckets = conn.get_all_buckets()            #버킷 다 가져오기
bnamelist = [b.name for b in buckets]     #버킷리스중 버킷을 하나씩 가져와 이름을 가져온다.

print(bnamelist)

bucket = conn.get_bucket('midtest2013108181')        #버킷 하나 가져오기
bucket.set_acl('public-read')
print([k.name for k in bucket.list()])                  #버킷에서 파일 이름들 가져오기


key = Key(bucket)                                       #버킷의 키를 key에 저장
key.key = 'image.png'                                #저장될 파일 이름이다.
key.set_contents_from_filename('/home/voidbluelabtop/Desktop/python/network_programming/lec_09_06.png')

key.set_acl('public-read')

key = bucket.get_key('privatefile')                     #가져올 파일이름
key.get_contents_to_filename('/home/voidbluelabtop/Desktop/python/network_programming/privatefile22') #어느결로에 어떤 이름으로 저장할지!