string = "Reverse This String"

#Method 1
rev = string[::-1]
print(rev)

#Method 2
li = list(string)
li.reverse()
string = "".join(li)
print(string)