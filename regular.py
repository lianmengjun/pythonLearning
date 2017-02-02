import re

phoneNumberRegex = re.compile(r'\d{3}-\d{4}-\d{4}')

phoneNumber = 'my phone number : 186-8800-1576'

mo = phoneNumberRegex.search(phoneNumber)

if mo == None:
    print('no phonenumber')
else:
    print(mo.group())

