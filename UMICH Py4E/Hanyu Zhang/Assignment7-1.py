fname = input("Enter file name: ")
fh = open('src/' + fname)
inp = fh.read().strip().upper()
print(inp)