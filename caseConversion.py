# capitalize, lower, swap, title, upper
# string examine/validation method[isalpha(), isalnum(), isdigit(), islower(), isupper(), isbase()]
str = "python"
print(str.capitalize())
str1 = "PYTHON"
print(str1.lower())
print(str.title())
print(str1.upper())

print(str1.isdigit())
print(str1.isalpha())



print(str.center(100,))  #centralize the character;
print(str.center(20,"_"))

print(str1.ljust(10,"_"))
print(str1.rjust(10,"_"))
print("  ".join(str))
print(str.startswith("p"))


lis=['ajay','aman','baisal','tabrej']
for name in lis:
    a=name.startswith("a")
    b=name.endswith("n")
    if a:
        print(name)
    if b:
        print(name)

alph="hey"
beta="   hey"
print(beta.strip()) #remove extra white spaces
c=alph.strip("o")
print(c)