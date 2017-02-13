import re, bs4, requests

html = 'http://www.xin.com/beijing/s/'

res = requests.get(html)
res.raise_for_status
test = bs4.BeautifulSoup(res.text, 'html.parser')

print(test)