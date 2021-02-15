#large3

a = int(input())
b = int(input())
c = int(input())

if a>b and a>c :
    print("a is greater",a)
elif b>a and b>c:
    print("b is greater",b)
elif c>a and c>b:
    print("c is greater",c)
else:
    print("All are equal")