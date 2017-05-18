
import pickle
from urllib.request import urlopen  # using urllib since requests wasn't working with pickle data

http = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(http)
for line in data:
    # data is tuple in the format of character * number of that char
    print("".join([k * v for k, v in line]))