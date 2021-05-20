# # What are dictionaries?
# # Structure as KEY = VALUE
# # VALUE could be string, int and list
# # Syntax = {}
#
# student_1 = {
#     "name" : "Tuan",
#     "key" : "value",
#     "stream" : "Cyber Security", # strings
#     "completed_lessons" : "3", # int
#     "completed_lessons_name" : ["variables", "operators" ,"data_collections"] # list
#
# }
# # # print(student_1)
# # print(student_1["name"])
# # print(student_1["stream"])
# # print(student_1["completed_lessons_name"])  # Name of the dictionary followed by the key then the index of the value you want to retrieve
#
# # Display only OPERATORS from the list inside the dictionary
# print(student_1["completed_lessons_name"][1])
# print(student_1.keys())
# print(student_1.values())

# Sets are data collection but the difference is that they are unordered
# Syntax name = {}

car_parts = {"wheels", "doors", "engines"}
print(car_parts)

# Can we add any new parts?
car_parts.add("windows")
print(car_parts)

# Can we remove any parts?
car_parts.discard("doors")
print(car_parts)

# Frozen sets
frozen_set = ([1,3,5,6])
print(frozen_set)