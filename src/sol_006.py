import requests
import zipfile
import re
import os

regex = re.compile("Next nothing is (\d+)")
num = 90052

# Download the zip file, if not here
try:
    if 'channel.zip' not in os.listdir():
        with open('channel.zip', 'wb') as f:
            rsp = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip', stream=True)
            for chunk in rsp.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
except Exception as e:
    print('error fetching page...', str(e))

comments = []
# Now loop through the zip file to find the answer
z = zipfile.ZipFile('channel.zip')
while True:
    data = z.read(str(num) + '.txt').decode("utf-8")
    comments.append(z.getinfo(str(num) + '.txt').comment.decode("utf-8"))
    print(data)
    match = regex.search(data)
    if not match:
        print(data)
        break
    num = match.group(1)

print(comments)
print(''.join(comments))
