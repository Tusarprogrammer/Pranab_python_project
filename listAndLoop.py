print("Simple Loop Start")
for x in range(5):
    print(x)
    print("Hello")
    print("I am from Odisha")
print("Simple Loop End")

for index in range(51):
    print(index)

data_list = [1,4,6,90,100,456,76576,888]
print("================================================")
for data in data_list:
    print(data)

item_index = 0
print("+++++++++++++++++++++++++++++++++++++++++++++++")
while item_index < len(data_list):
    print(data_list[item_index])
    item_index = item_index+1
print("##################################")
i = 1
while i<5:
    print("I am happy Today")
    if(i==2):
        break
    i = i+1


# Write a program to find the sum of 1 to 50 in Python
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
sum = 0
for data in range(51):
    sum = sum+data

print("Sum of 1 to 50 is ",sum)

no = 1
whilesum = 0
while no<=50:
    whilesum = whilesum + no
    no = no+1

print("Sum of 1 to 50 using while is ",whilesum)

#1, 2, 3, 4, 5,......50

list_for_range = []
for data in range(10):
    if data % 2 !=0:
        list_for_range.append(data)

print(list_for_range)


# List Comprenhension => Very important Topic
# Short hand code to create a  list from a list

original_list = [23,55, 33,44, 24, 100, 50, 10]

# Create a list from original_list which will contain only the even numbers

even_nos_list = []
for item in original_list:
    if(item %2 ==0):
        even_nos_list.append(item)

print("original_list",original_list)
print("even_nos_list",even_nos_list)

even_nos_list_using_list_comprehnesion = [item for item in original_list if item%2==0]

print("even_nos_list_using_list_comprehnesion",even_nos_list_using_list_comprehnesion)

#new_list = [Expression loop filter]

city_names_list = ["Bhubaneswar", "Balesore", "jajpur", "Rourkela"]

city_names_list_in_upper_case =  [city.upper() for city in city_names_list]

city_names_list_in_upper_case_having_letter_B =  [city.upper() for city in city_names_list if "B" in city]

print("city_names_list",city_names_list)
print("city_names_list_in_upper_case",city_names_list_in_upper_case)

print("city_names_list_in_upper_case_having_letter_B",city_names_list_in_upper_case_having_letter_B)














