import re, bs4, requests


def data(item):
    for i in range(0, len(item)):
        id = item[i].get('id')
        itemIdRe = re.compile(r'''(pmp-item-)(\d+)''')
        itemId = itemIdRe.search(id).group(2)
        print('id:' + itemId)

        title = item[i].select('a[title]')
        itemTitleRe = re.compile(r'''title="(.+)"''')
        itemTitle = itemTitleRe.search(str(title)).group(1)
        print('title:' + itemTitle)

        price = item[i].select('span b')
        priceRe = re.compile(r'''<b>(.+)</b>.*<b(.+)</b>.*<b>(.+)</b>''')
        itemPrice = priceRe.search(str(price)).group(3)
        print('Price:' + itemPrice)

        startTime = item[i].select('.soon-time')
        startTimeRe = re.compile(r'''\n(.+)开拍\n''')
        itemStartTime = startTimeRe.search(str(startTime)).group(1)
        print('starTime:' + itemStartTime.strip())

        endTime = item[i].select('span')
        endTimeRe = re.compile(r'结束</span>, <span class="time-num">(.+)</span>, <span class="info-num">')
        itemEndTime = endTimeRe.search(str(endTime)).group(1)
        print('endTime:' + itemEndTime)

        print()


print('please input the sellID:')
# sellID = input()
sellID = '2355097081'

html = 'https://paimai.taobao.com/pmp_seller/' + sellID + '.htm'

res = requests.get(html)
res.raise_for_status
test = bs4.BeautifulSoup(res.text, 'html.parser')

itemDateRe = re.compile(r'"data": ([\d\D]*)</script>\n'
                        r'<script class="J_pmp_item_list_template" type="text/template">')
itemDate = itemDateRe.search(str(test)).group(1)

# print(itemDate)
# print(test)

itemRe = re.compile(r'"currentPriceFmt": "(.*)",([\d\D]*?)'
                    r'"itemId": "(.*)",([\d\D]*?)'
                    r'"statusDesc": "(.*)",([\d\D]*?)'
                    r'"title": "(.*)",([\d\D]*?)')

item = itemRe.search(str(itemDate)).group(1)+itemRe.search(str(itemDate)).group(3)\
       + itemRe.search(str(itemDate)).group(5)+itemRe.search(str(itemDate)).group(7)
print(item)
