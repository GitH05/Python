# multi method to swap
a = 1
b = 2
# first method:
a,b = b,a
print(a,b, sep=" ")

# second mehod:
a = a+b
b = a-b
a = a-b
print(a,b)

# third method:
a = a*b
b = a//b
print(a,b)


# method four
a = a^b
b = a^b
a = a^b
print(a,b)