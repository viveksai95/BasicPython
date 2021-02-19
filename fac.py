#fac

a = int(input('enter a\n'))

prod = 1

if a<0:
    print("negative number")
    exit(0)

for i in range(1,a+1):
    prod *= i
    
print(prod)