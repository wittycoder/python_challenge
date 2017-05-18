import requests
import re

# Start values of nothing...
#nothing = 12345
nothing = 16044 / 2

regex = re.compile("and the next nothing is (\d+)")

while True:
    try:
        rsp = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d' % nothing)
        if rsp.status_code == 200:
            match = regex.search(rsp.text)
            if not match:
                print('ended with: ', rsp.text)
                break
            num = match.group(1)
            nothing = nothing + (int(num) - nothing)
            print(rsp.text)
    except:
        break