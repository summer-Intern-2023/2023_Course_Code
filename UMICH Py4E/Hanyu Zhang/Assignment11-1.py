import re
fh = open('src/' + "data-sum2.txt")
numbers = re.findall('[0-9]+', fh.read())
count = 0
for number in numbers :
    count += int(number)
print(count)