student_list = ["Rajesh", "Ajay", "Madhu", "Radhika"]

#student_one = "Rajesh"
#student_two = "Ajay"

print(student_list)

# List index starts from 0 onwards
print(student_list[0])
print(student_list[1])
print(student_list[2])
print(student_list[3])

student_list[0] = "Naveen"
print(student_list)

numbers_list = [2,3,5,8]

print(numbers_list[0]+numbers_list[1]+numbers_list[2]+numbers_list[3])

# Find the average marks for a student with marks list below, full marks for each subject is 100
#students_marks = [78, 67, 66, 79]

print(len(numbers_list))


student_list.append("Pranab")

print(student_list)

#student_list.clear()

print(student_list)

student_list.reverse()
print(student_list)

student_list.remove("Madhu")

print(student_list)

if "Radhika" in student_list:
    print("Radhika is Present")

name_list = ["Pranab" , "Kumar", "Dhal"]
# Display the full name

Family_members_name_list = ["Raghavendra", "Madhusudan", "Priyanka", "Isha"]
Family_members_role_list = ["Father", "GrandFather", "Mother", "Sister"]
# Display your family member and their name

list_one_data = ["Apple", "Orange", "Guava", "Grapes"]
list_two_data = ["Pineapple", "Watermelon", "Guava", "Grapes"]
list_three_data = ["Apple", "Orange", "Guava", "Grapes"]
list_four_data = ["Mango", "Banana", "Guava", "Grapes"]
#check if the above 4 lists are same or different

# check if both the lists having same elements or same data

if(list_one_data[0] == list_two_data[0] and  list_one_data[1] == list_two_data[1]
        and list_one_data[2] == list_two_data[2] and list_one_data[3] == list_two_data[3]):
    print("list_one_data and list_two_data are same")
else:
    print("list_one_data and list_two_data are NOT same")


if(list_one_data[0] == list_three_data[0] and  list_one_data[1] == list_three_data[1]
        and list_one_data[2] == list_three_data[2] and list_one_data[3] == list_three_data[3]):
    print("list_one_data and list_three_data are same")
else:
    print("list_one_data and list_three_data are NOT same")


employee_list = ["Narayan", "Padmanabha", "Vishnu", "Jagannath", "Krishna", "Gopi"]

#Check if Narayan is present in the list
#Check if Narayan and Vishnu both are present in the list
# Remove Gopi from the list

vegetable_list = ["Potato", "Tomato", "Spinach", "Beans", "Spinach", "Tomato", "Potato"]
# Reverse this list and check if the original is same as the reverse list
















