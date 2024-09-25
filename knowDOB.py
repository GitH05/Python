number = int(input("Enter any number:"))
yearDOB = int(input("Enter your Birth year:"))
number = number * 2
number = number + 5

number = number * 50
birth_year = input("your birthday is in this year Y/N ?")
if(birth_year == 'Y'):
    number = number + 1772 - yearDOB
    print("Output:",number)
else:
    number = number + 1773 - yearDOB
    # print("Output:",number)

# calculate the age and year:
for digit in str(number):
    enteredNumber =str(number)[0]
    age = str(number)[1:]
print("Entered number:",enteredNumber)
print("Your age:",age)