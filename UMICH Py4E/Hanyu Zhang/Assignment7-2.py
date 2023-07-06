numbers = []

fname = input("Enter file name: ")
fh = open('src/' + fname)
for line in fh :
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    a = line.find(":")
    b = float(line[a + 2: ].strip())
    numbers.append(b)

total = 0
def average(numbers) :
    global total
    count = len(numbers)
    for number in numbers :
        total += number
    return total / count

print("Average spam confidence:", average(numbers))