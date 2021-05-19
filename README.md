#Python Collections 

- Lists
- Dictionaries 
- Tuples
- Sets

The difference between a List and a Tuple is that Lists are mutable and Tuples are immutable (you cannot change or update them)

## What are data collections

```# Lists
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
print(shopping_list)``