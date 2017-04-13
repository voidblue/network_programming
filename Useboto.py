import boto
from boto.s3.connection import Location
from boto.s3.key import Key

f = open('ID.txt')
access_id = f.read()
f = open('Key.txt')
access_key = f.read()

conn = boto.connect_s3(access_id, access_key)

# conn.create_bucket('voidbluecom21', location = Location.EU)
x = None
print([x for x in dir(Location) if x.isalnum()])

buckets = conn.get_all_buckets()
bnamelist = [b.name for b in buckets]

print(bnamelist)

bucket = conn.get_bucket('voidbluebucketeeecom')
print([k.name for k in bucket.list()])


key = Key(bucket)
key.key = 'privatefile1'

key.set_contents_from_filename('/home/voidbluelabtop/Desktop/python/network_programming/privatefile')

key = bucket.get_key('privatefile')
key.get_contents_to_filename('/home/voidbluelabtop/Desktop/python/network_programming/privatefile22')