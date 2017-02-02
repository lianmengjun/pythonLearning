import re, bs4, requests


def data(item):
    for i in range(0,len(item)):

        id = item[i].get('id')
        itemIdRe = re.compile(r'''(pmp-item-)(\d+)''')
        itemId = itemIdRe.search(id).group(2)
        print('id:'+itemId)

        title = item[i].select('a[title]')
        itemTitleRe = re.compile(r'''title="(.+)"''')
        itemTitle = itemTitleRe.search(str(title)).group(1)
        print('title:'+itemTitle)

        price = item[i].select('span b')
        priceRe = re.compile(r'''<b>(.+)</b>.*<b(.+)</b>.*<b>(.+)</b>''')
        itemPrice = priceRe.search(str(price)).group(3)
        print('Price:'+itemPrice)

        startTime = item[i].select('.soon-time')
        startTimeRe = re.compile(r'''\n(.+)开拍\n''')
        itemStartTime = startTimeRe.search(str(startTime)).group(1)
        print('starTime:'+itemStartTime.strip())

        endTime = item[i].select('span')
        endTimeRe = re.compile(r'结束</span>, <span class="time-num">(.+)</span>, <span class="info-num">')
        itemEndTime = endTimeRe.search(str(endTime)).group(1)
        print('endTime:'+itemEndTime)

        print()

for page in range(100,105):

    html = 'https://paimai.taobao.com/pmp_list/3____1_1.htm?page=' + str(page)

    res = requests.get(html)
    res.raise_for_status()
    test = bs4.BeautifulSoup(res.text, "html.parser")

    item = test.select('.item-status-now')
    data(item)
    item = test.select('.item-status-soon')
    data(item)
    item = test.select('.item-status-over')
    data(item)







