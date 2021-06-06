

import random

file = open("lines.txt", 'r')
AllLines = file.read().split('\n')
file.close()
print(AllLines[random.randrange(len(AllLines))])
