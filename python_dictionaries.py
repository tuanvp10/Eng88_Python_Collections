# What are dictionaries?
# Structure as KEY = VALUE
# VALUE could be string, int and list
# Syntax = {}

student_1 = {
    "name" : "Tuan",
    "key" : "value",
    "stream" : "Cyber Security", # strings
    "completed_lessons" : "3", # int
    "completed_lessons_name" : ["variables", "operators" ,"data_collections"] # list

}
# # print(student_1)
# print(student_1["name"])
# print(student_1["stream"])
# print(student_1["completed_lessons_name"])

# Display only OPERATORS from the list inside the dictionary
print(student_1["completed_lessons_name"][1])
print(student_1.keys())
print(student_1.values())