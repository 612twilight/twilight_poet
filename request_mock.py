import urllib.request
import urllib.parse


def sendReq():
    params = urllib.parse.urlencode(
        {'start': '你好呀', 'style': 3})
    # url = 'http://115.159.197.227:80/?%s' % params
    url = 'http://localhost:5000/poem?%s' % params
    with urllib.request.urlopen(url) as f:
        print(f.read().decode('utf-8'))


if __name__ == '__main__':
    sendReq()