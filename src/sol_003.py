import requests
import re
from helpers import CommentHTMLParser

#regex = re.compile('[A-Z]{3}[a-z][A-Z]{3}')
regex = re.compile('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+')

parser = CommentHTMLParser()

def find_little_letters(data):
    print(''.join(regex.findall(data)))

try:
    rsp = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
    if rsp.status_code == 200:
        parser.feed(rsp.text)
        find_little_letters(parser.data)
except Exception as e:
    print('error fetching page...', str(e))