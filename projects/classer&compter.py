# dict.setdefault() + pprint.pprint() - pretty print
# classer et compter des items en ordre alaphabetique et 1 item par ligne

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)
# {' ': 13,
#  ',': 1,
#  '.': 1,
#  'A': 1,
#  'I': 1,
#  'a': 4,
#  'b': 1,
#  'c': 3,
#  'd': 3,
#  'e': 5,
#  'g': 2,
#  'h': 3,
#  'i': 6,
#  'k': 2,
#  'l': 3,
#  'n': 4,
#  'o': 2,
#  'p': 1,
#  'r': 5,
#  's': 3,
#  't': 6,
#  'w': 2,
#  'y': 1}