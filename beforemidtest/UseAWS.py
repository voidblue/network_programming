import sys
import requests
import requests_aws4auth as AA
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import mimetypes

f = open('ID.txt')                  #아이디 받아오기
access_id = f.read()
f = open('Key.txt')                 #엑세스 키 받아오기
access_key = f.read()
region = 'ap-northeast-2'           #위치 설정
endpoint = 's3-{}.amazonaws.com'.format(region)     #s3를 사용하는데 알맞은 Url형태로 만듦ㅎ
auth = AA.AWS4Auth(access_id,access_key, region, 's3')      #s3에 접속
ns = 'http://s3.amazonaws.com/doc/2006-03-01/'     #?????

def xml_pprint(element):
    print(minidom.parseString(element).toprettyxml())    #엘레먼트 트리의 xml형태의 변수를 xml형태에 맞춰 출력시켜준다.

def upload_file (bucket, s3_name, local_path, acl = 'private'):
    data = open(local_path, 'rb').read()                #모르겠다.
    url = 'http://{}.{}/{}'.format(bucket,endpoint,s3_name)       #준비해둔 url 양식을 끼워넣음
    headers = {'x-amz-acl': acl}                                    #헤더중에 접근권한 성정 변경
    mimetype = mimetypes.guess_type(local_path)[0]              #자료형태를 추측??

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
    res = requests.get(url, auth = auth)
    if res.ok:
        open(local_path,'wb').write(res.content)
        print('download {} OK'.format(s3_name))
    else:
        handle_error(res)


def create_bucket(bucket):
    XML = ET.Element('CreateBucketConfiguration')                       #XML에 속성을 추가하는 것으로 버킷을 만듦
    XML.attrib['xmlns'] = ns                                            #CreateBucketConfiguration엘리먼트 태그 안에 xmlns에 변수 ns라는 값을 가지게 한다.
    loaction = ET.SubElement(XML, 'LocationConstraint')                 #CreateBucketConfiguration엘리먼트 하위에 LocationConstraint를 추가하고 LocationConstraint를 loaction이란 변수에 추가.
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
    output = 'Status code : {} \n'.format(response.status_code)         #상태코드 출력
    root = ET.fromstring(response.text)                                 #상태 메시지
    code = root.find('Code').text                                       #상태코드
    output += code
    message = root.find('Message').text
    output += message
    print(output)


if __name__ == "__main__":
    cmd, *args = sys.argv[1:]                                           #cli로 파이선을 실행시켰을 때 함수와 파라미터를 받아들인다 덕분에 다른 방법으로 실행은 import로 해야한다.
    globals()[cmd](*args)
