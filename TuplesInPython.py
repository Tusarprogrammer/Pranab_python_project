#Tuple => Built in data type , ordered but unchangable/we can not modify type data

# For List , we can change
list_data = ["Ram", "Shyam", "Madhu"]
list_data[0] = "Radha"
print(list_data[0])
print(list_data)

for list_item in list_data:
    print(list_item)


# For Tuple, We can not change
tuple_data = ("Tuple Ram", " Tuple Shyam", "Tuple Madhu")
print(tuple_data[0])
print(tuple_data)

#tuple_data[0] = "Pranab"
print(tuple_data)


for item in tuple_data:
    print(item)

tuple_converted_to_list = list(tuple_data) # Step 1 => convert tuple to list
tuple_converted_to_list[0] = "pranab" # Step 2 => make necessary changes
tuple_data = tuple(tuple_converted_to_list) # Step 3 => convert the list to tuple

print(tuple_data)

#Program 1
# define a tuple with all the numbers starting from 0 to 100
# Remove all the even nos in that tuple
# Display the tuple


# Program 2
# define a tuple with duplicate elements and count each element occurrances
tuple_with_duplicate_data = ("bbsr","bbsr", "ck", "ck","ck","bls","brm","brm","brm","brm")









