# []
# ()
# {"key":"value"}
# set => {"val1","vel2"}

list_data = ["ram","hari", "ram"] # we can have duplicate values
print(list_data)


data_set = {"ram","hari", "ram"} # We will have only unique values

print(data_set)

my_set = {False, True, False, True, True, False}

print(my_set)

my_set_data = {1, 2, 3, 4, 5, 6, 7,8}
print(my_set_data)
print(my_set_data)
print(my_set_data)
print(my_set_data)
print(my_set_data)

my_set_data1 = {"mango", "apple", "Orange", "Banana", "Cusard Appale", "Lemon", "Pineapple","Grape"}


print(my_set_data1)
print(my_set_data1)
print(my_set_data1)
print(my_set_data1)
print(my_set_data1)



# Function ==== Method
# f(x) =  x + 2
# f(1) = 1+2 = 3
# f(2) = 2+2 = 4
# Here x is input and x+2 is output


print(1+2)

# Line no 46 -47 is called method definition
def display(x):
    print("Hi I am here",x)
    print("Hi I am here also", x)
    print("Hi I am happy", x)


#Line no 51 to 53 called function call
display(10)
display(100)
display(10000)


# Add 2 nos using method in python

def add2Nos(x, y):
    print(x+y)

add2Nos(10,20)
add2Nos(10,200)
add2Nos(100,20)


def add2NosMethod2(x=100, y=200):
    return x+y

print("hiiii")
print(add2NosMethod2(10))
print(add2NosMethod2())

# Write methods in python to add 5 nos,
# Write methods in python to multiply 3 nos
# Write methods in python to divide 2 nos
# Write methods in python to subtract 2 nos



# Default parameters




class_I_details = "vdsfsfsfdsf"
class_II_details = "2nd standard"
entered_class_details = "II"

if("class_I_details" == "class_"+entered_class_details+"_details"):
    print(class_I_details)
elif("class_II_details" == "class_"+entered_class_details+"_details"):
    print(class_II_details)


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



















