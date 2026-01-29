a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
if a>b and b>c :
    print("a is largest value")
    print("c is smallest value")
elif b>a and a>c:
    print("b is largest value")
    print("c is smallest value")
elif c>b and b>a:
    print("c is largest value")
    print("a is smallest value")
    
