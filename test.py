# Creating a String and Print it into Console.

name = "Tony Stark"
# print(name)

# Output:Tony Stark

# Accessing Characters in a String:

message = "I am IronMan"
# print(message[0])
# print(message[1])
# print(message[2])
# print(message[3])
# print(message[4])
# print(message[5])
# print(message[6])
# print(message[7])
# print(message[8])
# print(message[9])
# print(message[10])
# print(message[11])
# print(message[12])


# Output:
# I
#
# a
# m
#
# I
# r
# o
# n
# M
# a
# n


# String Slicing:

Movie_name = "Avengers:The End Game"
# print(Movie_name[0:8])
# Output:Avengers


# String Concatenation:

First_name = "Tony"
Last_name = "Stark"
Full_name = First_name + " " + Last_name
# print(Full_name)
# Output :Tony Stark


# String Formatting:

Name = "Tony Stark"
Age = 40
Message = "My name is {} and i am {} years old".format(Name, Age)
# print(Message)

# Output: My name is Tony Stark and i am 40 years old

# Common String Methods:

text = 'I am Ironman'
# print("\nConverted String:")
# print(text.upper())

# print("\nConverted String:")
# print(text.lower())

first_string = 'I am Ironman'
second_string = first_string.replace('Ironman', 'Hulk')
# print("\nConverted String:")
# print(second_string)

string = 'I am IronMan'
string_split = string.split(' ')
# print("\nConverted String:")
# print(string_split)

my_string = "   I am IronMan  "
stripped_string = my_string.strip()
# print("\nConverted String:")
# print(stripped_string)

# Output:
# Converted String:
# I AM IRONMAN
#
# Converted String:
# i am ironman
#
# Converted String:
# I am Hulk
#
# Converted String:
# ['I', 'am', 'IronMan']
#
# Converted String:
# I am IronMan
#


# Range Function and For Loop in Python
# Example:1 (Iterating Over a Range of Numbers Using a For Loop)
for i in range(10):
   print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

#Example-2

# for j in range(1,10,2):
#     print("\n",j)
#
# Output:
#  1
#
#  3
#
#  5
#
#  7
#
#  9

# Logical Operaters (and,or,not)

#Example-1

a=25
b=30
c=35
# if a>b and a>c:
#     print(" a is greater")
# elif b>a and b>c:
#     print("b is greater")
# else:
#     print("c is greater")

# Output: c is greater

x=25
y=40

if x<y or x==y:
    print("1st condition is true")
else:
    print("2nd condtion is true")

# Output: 1st condtion is true

password=input("Enter Your Password: \n")
if not password =="password123":
    print("incorrect password")
else:
    print("Correct Password")

#OutPut:Correct password

