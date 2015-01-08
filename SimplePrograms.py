# 1 line: Output
print("# 1 line: Output") 
print("hello, world!")

# 2 lines: Input, assignment
print("# 2 lines: Input, assignment")
name = input("What is your name?\n")
print("Hi, %s!!" % name)

# 3 lines: For loop, built-in enumerate function, new style formatting
print("# 3 lines: For loop, built-in enumerate function, new style formatting") 
friends = ["john", "pat", "gary", "michael"]
for i, name in enumerate(friends):
    print("num {num} is {name}".format(num=i, name=name))
    
# 4 lines: Fibonacci, tuple assignment
print("# 4 lines: Fibonacci, tuple assignment") 
parents, babies = (1,1)
while babies < 100:
    print("this generation has {0} babies".format(babies))
    parents, babies = (babies, parents + babies)

    
# 5 lines: Functions
print("# 5 lines: Functions") 
def greet(name):
    print("Hello", name)
    
greet("jack")
greet("jill")
greet("bob")

# 6 lines: Import, regular expressions 
print("# 6 lines: Import, regular expressions")
import re
for string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', string):
        print(string, 'is a valid US local phone number')
    else:
        print(string, 'rejected')
        
        
# 7 lines: Dictionaries, generator expressions 
# print("# 7 lines: Dictionaries, generator expressions")
        
        