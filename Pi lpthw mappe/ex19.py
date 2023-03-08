def cheese_and_crackers(cheese_count, boxes_of_crackers): #It's a function
    print(f"You have {cheese_count} cheeses!") #prints text and the variable cheese_count
    print(f"You have {boxes_of_crackers} boxes of crackers!")#prints text and the variable boxes_of_crackers
    print("Man that's enough for a party!") #print
    print("Get a blanket.\n") #print and a new line


print("We can just give the function numbers directly:") # print
cheese_and_crackers(20, 30) 


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math indise too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
