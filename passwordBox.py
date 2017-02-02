#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

password={'email':'1',
          'weibo':'2',
          'weixin':'3'}

import sys,pyperclip

'''
if len(sys.argv)<2:
    print('something wrong')
    sys.exit()

'''

account=input()

#account = sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print(password.get(account)+'here you are')
else:
    print('en')