name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
with open('src/' + name) as fh :
    all = fh.read()
time = {}
hour = {}
dic = {}
lines = all.split("\n")
for line in lines :
    if line.startswith("From ") :
        time = line.split(" ")[6]
    else :
        continue
    hour = time.split(":")[0]
    if hour in dic :
        dic[hour] += 1
    else :
        dic[hour] = 1
sorted_dict = sorted(dic.items())
for items in sorted_dict :
    print(items[0], items[1])