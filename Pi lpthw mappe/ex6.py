types_of_people = 10 #variabel
x = f"There are {types_of_people} types of people." #variabel der indeholder en f-string med en variabel inden i

binary = "binary" #variabel
do_not = "don't" #variabel
y = f"Those who know {binary} and those who {do_not}." #variabel der indeholder en f-string med to variabler i

print(x) # print
print(y)

print(f"I said: {x}") # print f-string med variabel X inden i
print(f"I also said: '{y}'")

hilarious = False # en variabel med en bool
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) #print joke variabel med bool værdien

w = "This is the left side of..." #variabel
e = "a string with a right side."

print(w + e) # printer 2 variabler