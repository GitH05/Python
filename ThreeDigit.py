number = int(input("Enter a number:"))
count = 0
temp = number

# Check if the number is three digits.
if 100 <= number <= 999: print(f'The {number} is a {3} digit number')
else:
    # Calculate the number of digits using a loop.
    while number > 0:
        number = number // 10  # Reduce the number by removing the last digit.
        count += 1

    print(f'The {temp} is of {count} digit number')
