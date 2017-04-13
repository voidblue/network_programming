import sys
import requests
import requests_aws4auth as AA
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import mimetypes

f = open('ID.txt')
access_id = f.read()
f = open('Key.txt')
access_key = f.read()
region = 'ap-northeast-2'
endpoint = 's3-{}.amazonaws.com'.format(region)
auth = AA.AWS4Auth(access_id,access_key, region, 's3')
ns = 'http://s3.amazonaws.com/doc/2006-03-01/'

def xml_pprint(element):
    print(minidom.parseString(element).toprettyxml())

def upload_file (bucket, s3_name, local_path, acl = 'private'):
    data = open(local_path, 'rb').read()
    url = 'http://{}.{}/{}'.format(bucket,endpoint,s3_name)
    headers = {'x-amz-acl': acl}
    mimetype = mimetypes.guess_type(local_path)[0]

    #다운로드 없이 바로 이미지 띄움
    if mimetype:
        headers['Content-type'] = mimetype
    req = requests.put(url, data = data,headers = headers , auth = auth)

    if req.ok:
        print('Uploaded {} OK'.format(local_path))
    else:
        handle_error(req)


def download_file(bucket, s3_name, local_path):
    url = 'http://{}.{}/{}'.format(bucket, endpoint, s3_name)
    req = requests.get(url, auth = auth)
    if req.ok:
        open(local_path,'wb').write(req.content)
        print('download {} OK'.format(s3_name))
    else:
        handle_error(req)


def create_bucket(bucket):
    XML = ET.Element('CreateBucketConfiguration')
    XML.attrib['xmlns'] = ns
    loaction = ET.SubElement(XML, 'LocationConstraint')
    loaction.text = auth.region
    data = ET.tostring(XML, encoding = 'utf-8')
    xml_pprint(data)


    url = 'http://{}.{}'.format(bucket, endpoint)
    req = requests.put(url, data=data, auth=auth)
    if req.ok:
        print('Create Bucket : {} is OK'.format(bucket))
    else:
        handle_error(req)

def handle_error(response):
    output = 'Status code : {} \n'.format(response.status_code)
    root = ET.fromstring(response.text)
    code = root.find('Code').text
    output += code
    message = root.find('Message').text
    output += message
    print(output)


if __name__ == "__main__":
    cmd, *args = sys.argv[1:]
    globals()[cmd](*args)
