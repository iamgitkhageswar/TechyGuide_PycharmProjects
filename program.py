# Ask the user to enter the number
number = int(input("Enter the integer number: "))

# Initiate value to null
revs_number = 0

# Reverse the integer number using the while loop
while number > 0:
    # Logic
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10

    print("The reverse number is:{}".format(revs_number))

