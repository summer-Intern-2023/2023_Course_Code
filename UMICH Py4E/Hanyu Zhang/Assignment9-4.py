fname = input("Enter flie name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
with open('src/' + fname) as fh :  
   all = fh.read()
lines = all.split("\n")
senders = {}
for line in lines :  
   if line.startswith("From ") :  
       sender = line.split(" ")[1]  
       if sender in senders :  
           senders[sender] += 1  
       else :  
           senders[sender] = 1
most = max(senders, key=senders.get)
print(most, senders[most])  