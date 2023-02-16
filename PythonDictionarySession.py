dictionary_data = {"key":"value"}
person_data = {
    "aadharno":"1232 4567 8967",
               "name" : "Rajesh Patnaik",
               "age":50 ,
               "Mobile No": 23424324,
    "bank accounts":[4324324324,234324324,124321412]

}


# []
# ()
# {}

print(person_data)

print(person_data["age"])
print(person_data.get("age"))
print(person_data["Mobile No"])

print(person_data["aadharno"])

print(person_data.keys())

print(person_data)
person_data["Mobile No"] = 5555555

print(person_data)

person_data.update({"whatsapp":"75767686"})
print(person_data)

print(person_data.values())
print(person_data.keys())

for item in person_data:
    print("Key is ", item," and it's value is " ,person_data[item])

data_items = [person_data, person_data]
print(data_items)

# Program to check a palindrome
string_data = "katak"
reversed_string_data = ""
length_of_string_data = len(string_data)

while(length_of_string_data>=1):
    reversed_string_data = reversed_string_data + string_data[length_of_string_data-1]
    length_of_string_data = length_of_string_data -1

if string_data == reversed_string_data:
    print(string_data ," is a palindrome as it is same as the reverse")
else:
    print(string_data, " is not a palindrome as it is same as the reverse")


# Analysis for a palindrome check


# "KATAK"

# length 5
# AB => NO
# AA => YES
# AAA => YES

# ABA => YES

# i = 0, j= length -1

# ith data , jth data ....i incrment , j decrement
















all_students_list=["ram","shyam","madhu","hari","radha", "meera"]
students_present=["shyam","madhu"]
students_absent = []

for each_present in all_students_list:
    if each_present in students_present:
        print(each_present, "is present")
    else:
        students_absent.append(each_present)

print(students_absent)








