#Python Collections 

- Lists
- Dictionaries 
- Tuples
- Sets

The difference between a List and a Tuple is that Lists are mutable and Tuples are immutable (you cannot change or update them)

## What are data collections


# Lists
```
# Syntax ["London"]
# CRUD = Create, Read, Update and Delete

shopping_list = ["juice", "strawberries", "yoghurt", "chicken", "raspberries", "butter"]
            #       0           1             2          3            4            5
print(shopping_list)
print(type(shopping_list))

print(shopping_list[2]) # = yoghurt

# If we need to replace an item from the list
shopping_list[5] = "oats"
print(shopping_list)

shopping_list.append("Mangoes") # .append adds a item to the end of the list
print(shopping_list)

# To remove something from your shopping list we have a method called .remove
shopping_list.remove("oats")
print(shopping_list)

shopping_list.pop() # pop() removes the last item on the list 
print(shopping_list)
```

## Tuples
```
# Tuples are IMMUTABLE
# Syntax ()
# Uses cases

essentials = ("eggs", "milk", "bread")
print(essentials)
print(type(essentials))
# Replace bread with yoghurt
```

## Dictionaries 

``` # What are dictionaries?
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
# print(student_1)
print(student_1["name"])
print(student_1["stream"])
print(student_1["completed_lessons_name"])

# Display only OPERATORS from the list inside the dictionary
print(student_1["completed_lessons_name"][1])
print(student_1.keys())
print(student_1.values())
```
# Sets
are data collection but the difference is that they are unordered
- Syntax name = {}
```
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
```