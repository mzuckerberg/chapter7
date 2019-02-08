import re
reob = re.compile(r'\d\d\d-\d\d\d-\d\d\d\dx\d\d')
rezz = reob.search('my fucking number is 420-696-9694x20. thanks.')
print('if theres a match it looks like this: ' + rezz.group())
