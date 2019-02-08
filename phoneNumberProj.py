'''
get text off clipboard using pyperclip:
import sys, pyperclip
text = pyperclip.paste()

find all phone # and email addresses in the text:


paste them to the clipboard:
pyperclip.copy()

two regexes:
one for matching phone #s
one for matching emails

find all matches not just first

neatly format matched strings in to a single string to paste

display some kind of message if no matches found
'''

#! python3
import pyperclip, re

# phone number regex

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code optional
    (s|-|\.)?                       # separator optional
    (\d{3})                         # first 3 digits
    (s|-|\.)                        # separator non optional
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    '''), re.VERBOSE)

# email regex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # at symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot something
    )''', re.VERBOSE)

# TODO: find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO: copy results to the clipboard
