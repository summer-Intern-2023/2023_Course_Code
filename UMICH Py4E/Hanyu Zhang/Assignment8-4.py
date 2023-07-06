fname = input("Enter file name: ")
fh = open('src/' + fname)
lst = list()
for line in fh :
    l = line.split()
    for word in l:
        if word not in lst :
            lst.append(word)
            lst.sort()
        else :
            continue
print(lst)