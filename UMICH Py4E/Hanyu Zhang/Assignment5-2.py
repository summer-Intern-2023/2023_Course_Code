numbers = []

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    else:
        try:
            num = int(num)
            numbers.append(num)
        except:
            print("Invalid input")    

print("Maximum is", max(numbers))
print("Minimum is", min(numbers))