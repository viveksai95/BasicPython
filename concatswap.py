#concatswap

a = input('enter a\n')
b = input('enter b\n')

#a = str(123)
#b = str(456)

for i in range(a,b):
    temp = a[2] 
    a[2] = b[2]
    b[2] = temp
    
c = a + " " + b
print(c)

#temp = a
#a = b
#b = temp

#print(a)
#print(b)