score = input("Enter Score: ")
s = float(score)

if 0 <= s < 0.6 :
    print("F")
elif 0.6 <= s < 0.7 :
    print("D")
elif 0.7 <= s < 0.8 :
    print("C")
elif 0.8 <= s < 0.9 :
    print("B")
elif 0.9 <= s < 1 :
    print("A")
else :
    print("Error")