#oddeven

a = int(input())

if a < 0:
    print("negative")
    exit(0)

if a % 2 == 0:
    print("The no is even")
else:
    print("The no is odd")