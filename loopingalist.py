#Loop a List

data_items = ["Bhubaneswar", "Balasore" , "Cuttack", "Sambalpur" , "Rourkela",
              "Cuttack", "Cuttack","Jajpur","Berhampur", "Bhubaneswar"]

#Write a program to find the occurrance count for cities with name cuttack and Bhubaneswar

metro_list = ["New Delhi" , "Chennai", "Mumbai", "Kolkata", "Bangalore", "Hyderabad"]
#Display the metro city name with longest name


#Check if city name Berhampur present in the list and display it's index
i=0
for city in data_items:
    if(city == "Berhampur"):
        print("Berhampur is present and it's index is",i)
        break
    i =i+1

if(i==len(data_items)):
    print("Berhampur is not present")


print("Looping list using FOR loop")
i=0
for city in data_items:
    #print(i)
    print(i,city)
    i=i+1
print("Looping list using WHILE loop")
i=0
while i<len(data_items):
    print(i,data_items[i])
    i=i+1

#Sorting a list

data_items_numeric = [23,56,11,345,88,100,15]
print(data_items_numeric)
data_items_numeric.sort() # Ascending order of values
print(data_items_numeric)

data_items_numeric.sort(reverse=True) # descending order of values
print(data_items_numeric)

name_data = ["Ram", "Manav" ,"Hari", "Shiva"]
print(name_data)
name_data.sort() # Ascending order of values
print(name_data)
name_data.sort(reverse=True) # descending order of values
print(name_data)



data_items_numeric = [23,56,11,345,88,100,15, 1000, 40000, 3456]

#Find the max and min number from the list


data_items_numeric = [23,56,11,345,88,100,15, 1000, 40000, 3456]
#Find the max and min number from the list
#Sort this list
data_items_numeric.sort()
size_of_list = len(data_items_numeric)

min_number = data_items_numeric[0]
max_number = data_items_numeric[size_of_list-1]
print("Sorted List is below")
print(data_items_numeric)

print("minimum number",min_number)
print("maximum number",max_number)

newlist = [x for x in range(10)]

print(newlist)


#===========================================LOOP============================

print("Simple Loop Start")
for x in range(5):
    print(x)
    print("Hello")
    print("I am from Odisha")
print("Simple Loop End")




