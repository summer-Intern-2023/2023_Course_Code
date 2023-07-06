fname = input("Enter file: ")
fh = open('src/' + fname)
count = 0
for line in fh :
    if "From:" in line :
        end = line.find(" ", 6)
        print(line[6:end].split()[0])
        count += 1
    else :
        continue

print("There were", count, "lines in the file with From as the first word")