the_count = [1, 2, 3, 4, 5]
fruits =['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
    
# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")
    
# we can also build lists, first start with an empty one
elements = [i for i in range(0, 6)]

print(f"Adding {i} to the list.")
# append is a function that lists understand
# To add an item to the end of the list, use the append() method:
elements.append(i)

# The insert() method inserts an item at the specified index:
elements.insert(2, 'mellon')

# To append elements from another list to the current list, use the extend() method.
elements.extend(fruits)


# now we can print them out too
for i in elements:
    print(f"Element was: {i}")