name = 'Kristian Saunte'
age = 42 # not a lie
height = 190 # Centimeters
weight = 100 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Light Brown, with a spalsh of Viking'

us_height = height * 0.393701
us_weight = weight  * 2.2046226218
us_round_weight = round(us_weight)

print (f"Let's talk about {name}.")
print (f"He's {height} centimiters tall.")
print (f"He's {weight} Kg Heavy.")
print ("Actually that's not too heavy.")
print (f"He's got {eyes} eyes and {hair} hair.")
print (f"His teath are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print (f"If I add {age}, {height}, and {weight} I get {total}.") 
print (f"His height in inches is {us_height}.")
print (f"His weight in lbs is {us_round_weight}.")
