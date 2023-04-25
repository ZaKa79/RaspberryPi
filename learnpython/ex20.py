from sys import argv #importerer argv 

script, input_file = argv #fortæller at for at køre script skal vi have en input fil

def print_all(f): #Function
    print(f.read()) #

def rewind(f): #Function
    f.seek(0) #start på linje 0 

def print_a_line(line_count, f): #Function
    print(line_count, f.readline()) #print (linje nummer, læs linjen)

current_file = open(input_file) #variabel der åbner input_file

print("First let's print the whole file:\n") #printer

print_all(current_file) #kalder funktionen print_all, som læser current_file

print("Now let's rewind, kind of like a tape.") #mere print

rewind(current_file) #kalder funktionen rewind i filen current_file

print("let's print three lines:") # mere print 

current_line = 1 #variabel current_line med værdi 1
print_a_line(current_line, current_file) # kalder print_a_line

current_line = current_line + 1 #current line incrementeres med 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)