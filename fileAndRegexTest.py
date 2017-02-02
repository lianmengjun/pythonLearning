import re,requests,bs4,os

'''

helloFile = open('hello','a')

helloFile.write('hello world!\n')

helloFile.close()

'''



helloFile = open('hello')
helloFile1 = open('regexTest','a')

inData = re.compile(r'''(\w+):(\d+)''')

while True:

    test = helloFile.readline()

    if test == '':
        break

    testRe = inData.search(test)

    if testRe is not None:
        mo = testRe.group(1)
        helloFile1.write(mo+'-')
        mo = testRe.group(2)
        helloFile1.write(mo + '\n')
        print(mo)

#    print(test)

helloFile.close()
helloFile1.close()


