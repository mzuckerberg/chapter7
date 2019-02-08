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

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code optional
    (s|-|\.)?                       # separator optional
    (\d{3})                         # first 3 digits
    (s|-|\.)                        # separator non optional
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension

'''), re.VERBOSE)

# TODO: Create email regex

# TODO: find matches in clipboard text

# TODO: copy results to the clipboard
