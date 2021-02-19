#fibonacci

a = int(input('enter a\n'))

first = 0
second = 1

if a<1:
    print("invalid")
    exit(0)
    
if a==1:
    print(0)
    exit(0)

print(first)
print(second)

for i in range(a-2):
    add = first + second
    first = second
    second = add
    print(add)