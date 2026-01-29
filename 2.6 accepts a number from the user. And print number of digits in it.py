a = int(input("Enter number"))
count = 0

if a == 0:
        count = 1

else:
    while a != 0:
        a //= 10
        count += 1

print("number of digits =", count)
        
