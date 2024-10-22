# to check that the last digit is even or not:
number = 123
lastDigit = number % 10
if(lastDigit%2==0):
    print(f'The last digit:{lastDigit} in {number} is even')
else:
        print(f'The last digit:{lastDigit} in {number} is odd')


#_____________ reversed number
# number=123
# reverse=0
# while(number>0):
#     lastDigit = number%10
#     reverse = (reverse * 10)+lastDigit
#     number=number//10
# print(reverse)
    

#_______________check palindrome
# number=121
# temp = number
# reverse=0
# while(number>0):
#     lastDigit = number%10
#     reverse = (reverse * 10)+lastDigit
#     number=number//10
# print(reverse)
# if(reverse==temp):
#     print(f'{reverse} is plaindrome.')
# else:
#     print(f'{reverse} is not palindrome.')
