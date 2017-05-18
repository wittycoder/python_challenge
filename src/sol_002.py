import requests

from helpers import CommentHTMLParser

chars = {}

parser = CommentHTMLParser()

def count_chars(data):
    for c in data:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

try:
    rsp = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
    if rsp.status_code == 200:
        parser.feed(rsp.text)
        count_chars(parser.data)
except Exception as e:
    print('error fetching page...', str(e))

print([k if v < 10 else '' for k,v in chars.items()])
