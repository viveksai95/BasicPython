#digitprint

a = int(input())
add = 0
mul = 1

while a > 0 :
    rem = a % 10
    #print(rem)
    a = int(a/10)
    #add += rem
    mul *= rem
    
#print(add)
print(mul)