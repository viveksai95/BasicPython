#stringreplace

string_a = "15311a1983"
#           12345678910
print(string_a[:8]+"79")

string_a = "123ab567a6"
#           12345678910  

print(string_a[:3]+string_a[5:7]+string_a[8:])
string_b = string_a[:3]

string_c = string_a[5:7]

string_d = string_a[8:]

#print(string_a)
print(string_b)
print(string_c)
print(string_d)
#print(string_a[0])