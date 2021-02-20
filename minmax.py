#minmax

list_a = [1,2,3,4,5]
least = list_a[0]

for i in list_a:
    #print(i)
    if i < least:
        least = i
#print(min(list_a))
#print(max(list_a))

print(least)