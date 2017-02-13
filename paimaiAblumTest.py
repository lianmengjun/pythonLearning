import re, bs4, requests

print('please input the sellID (like 2355097081):')
sellID = input()
# sellID = '2355097081'

html = 'https://paimai.taobao.com/pmp_seller/' + sellID + '_1.htm'

res = requests.get(html)
res.raise_for_status
test = bs4.BeautifulSoup(res.text, 'html.parser')

albumDateRe = re.compile(r'"data": ([\d\D]*?)</script>\n')
albumDate = albumDateRe.search(str(test)).group(1)

albumListRe = re.compile(r'"albumId": "(.*)",([\d\D]*?)'
                         r'"title": "(.*)",')
albumList = albumListRe.findall(albumDate)

for i in range(0, len(albumList)):
    print(str(i+1) +' '+albumList[i][0] + ' ' +albumList[i][2])

print('please input the ablumNum:')
ablumNum = input()
# ablumNum = 1

albumID = albumList[ablumNum - 1][0]

albumHtml = 'https://paimai.taobao.com/pmp_album/' + albumID + '.htm'
res = requests.get(albumHtml)
res.raise_for_status
test = bs4.BeautifulSoup(res.text, 'html.parser')

itemDate = test.select('.pmp-item-list')

itemlistRe = re.compile(r'<a href="//paimai.taobao.com/pmp_item/(.*?)\.htm"(.*?)'
                        r'title="(.*?)">(.*?)</a>([\d\D]*?)'
                        r'起拍价</span>\n<span class="price-num"><em>¥</em><b>(.*?)</b>([\d\D]*?)'
                        r'当前价</span>\n<span class="price-num"><em>¥</em>'
                        r'<b class="xmpp-current-price">(.*?)</b>([\d\D]*?)')

itemList = itemlistRe.findall(str(itemDate))

for i in range(0, len(itemList)):
    print(str(i + 1) + ' ' + itemList[i][0] \
          + ' ' + itemList[i][2] \
          + ' ' + itemList[i][5] \
          + ' ' + itemList[i][7])
