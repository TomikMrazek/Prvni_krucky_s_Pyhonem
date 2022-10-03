import re
num_1 = 'abbbc'

regex = r'ab+c'

print(re.match(regex, num_1))