data_dict = {"student1":{"name":"Ram", "roll":"223134","class":"BTech"},
             "student2":{"name":"Ramesh", "roll":"2233334","class":"MCA"},
             "student3":{"name":"Raghu", "roll":"8889","class":"MBBS"}
             }

print(data_dict)

print(data_dict.get("student1"))

print(data_dict.get("student3").get("roll"))

# Display all the roll nos of data_dict
# Keep all the class values in this dictionary in a list and display them


employee_dict = {"emp1":{"name":"Ram", "empid":"223134","salary":20000},
             "emp2":{"name":"Ramesh", "empid":"2233334","salary":30000},
             "emp3":{"name":"Raghu", "empid":"8889","salary":40000},
"emp4":{"name":"Raghuram", "empid":"88669","salary":50000}
             }

# Average salary of employees in this dictionary
# Find the employe having the highest salary
# Find the employe having the second highest salary

print(len(employee_dict))

for each_data in employee_dict:
    print(each_data,employee_dict[each_data])

list_data = ["Ram", "Madhu","Ram", "Hari", "Jagannath", "Hari", "Shiva", "jagannath", "Sita","Sita"]
# Find the frequency of each data items in this list


list_data = [3,4,6,7,9,80]

# How to debug code

# Resume Preparation

# Linkedin profile creation

# Github commands

# Funtions, lambdas, File handling , DB Programming, JSON handling

# Next wednesday I will take your first interview, out of 10


original_string = "katak"
reverse_string = reversed(original_string)
print(original_string,reverse_string)
if original_string==reverse_string:
    print("Palindrome")
else:
    print("Not a palindrome")



data_dict = {"student1":{"name":"Ram", "roll":"223134","class":"BTech"},
             "student2":{"name":"Ramesh", "roll":"2233334","class":"MCA"},
             "student3":{"name":"Raghu", "roll":"8889","class":"MBBS"}
             }

for eachdist in data_dict:
    print(data_dict.get(eachdist).get("roll"))



# Keep all the class values in this dictionary in a list and display them

class_list = []
class_list2 = []
data_dict = {"student1":{"name":"Ram", "roll":"223134","class":"BTech"},
             "student2":{"name":"Ramesh", "roll":"2233334","class":"MCA"},
             "student3":{"name":"Raghu", "roll":"8889","class":"MBBS"}
             }

class_list.append(data_dict.get("student1").get("class"))
class_list.append(data_dict.get("student2").get("class"))
class_list.append(data_dict.get("student3").get("class"))

print(class_list)
#print(data_dict.get("student1").get("class"))
#print(data_dict.get("student2").get("class"))
#print(data_dict.get("student3").get("class"))


for data_item in data_dict:
    class_list2.append(data_dict.get(data_item).get("class"))

print("class_list2",class_list2)





