#prime

n = int(input("enter value of n\n"))

if n <= 1:
    print("invalid")
    exit(0)

factor = 0

for i in range (1,n+1):
    if n % i == 0:
        print(i)
        # factor+=1
        # break
        
# if factor > 0:
    # print("Not Prime number")
# else:
    # print("Prime Number")