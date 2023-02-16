
# Default parameters

def add_two_nos(first_no=100,second_no=200):
    print(first_no+second_no)

print("By passing values")
add_two_nos(10,20)

print("Using default parameters")
add_two_nos()

print("Using one default parameters")
add_two_nos(10)


def display_name(first_name="Rajesh",middle_name="Kumar", last_name="Panda"):
    print(first_name+" "+middle_name+" "+last_name)

display_name()
display_name("Pranab","Kumar","Dhal")

display_name("Pranab","Kumar")

# Arbitrary Arguments (*)

def add_nos(first_no, second_no, third_no):
    print(first_no+second_no+third_no)

add_nos(1,2,3)

def add_nos_using_arbitrary_arguments(*no): #astrick
    sum = 0
    for item in no:
        sum = sum+ item
    print("sum is", sum)

add_nos_using_arbitrary_arguments(1,3,4,5,6)

add_nos_using_arbitrary_arguments(1,3,4,5,6,4,5,6,7,8,9)

add_nos_using_arbitrary_arguments(1,3)


# naming based arguments

def sum_of_nos(first_number, second_number, third_number):
    print("first_number =",first_number,"second_number",second_number,"third number",third_number)
    print(first_number+second_number+third_number)

sum_of_nos( second_number=20,third_number=30,first_number=10 )


#args(*), kargs(**) - Keyword arguments

def sum_of_nos_using_kargs(**numbers): # double astrick
    sum = 0
    for item in numbers:
        sum = sum + numbers.get(item)
    print("sum =", sum)

sum_of_nos_using_kargs(first_number = 10, second_number= 20, third_number=40)

# write a program to display n numbers using arbitrary arguments
# Write a program to display full name using keyword arguments


# Next class topics

# First mock interview , Github account creation

# next to next CV Preparation and Linkedin Profile creation

# next to next second mock interview , DB Programming, JSON

# next to next third mock interview , lambda,file handling,OOPs

# 4th mock interview and a midium size project assignment

# 5th mock interview



#=================================

Inputs are :
data_items1 = [1,3,5,7]
data_items2 = [9,11,23,45,67]

data_items3 = []







