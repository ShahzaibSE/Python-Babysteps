print("Hello World");  # Hello World 
'''
 This is multiline comment.
 Semi colon doesn't generate error.
'''
# Print("Hello World") # This generates error.
#
'''
~~~  Working with variables ~~~
'''
#
# We don't need declaration keyword for variables.
name = "Shahzaib Noor" # At runtime it's type will be determined as string.
print(name) #Simply printing name.
print("My name is"+" "+name) # String concatenation.
print(f"My name is {name}") #String Interpolation.
#-------------------#
# Ways to declare variables.
# $myname="Bruce Wayne" #Wrong declaration.
# print($myname)
#
# Note: Python is dynamically typed.
# country-of-origin = "Pakistan" #Wrong declaration.

# =========================================== Variable Numbers ===================================================#
mynum = 150
print()
print("=========================================== Variable Numbers =================================================")
print("My Number")
print(mynum + 150)
# lets try to try to add two variables one with string and other with number.
firstnum = "100"
secondnum = 200
print()
print("lets try to try to add two variables one with string and other with number")
# print(firstnum+secondnum) # TypeError: can only concatenate str (not "int") to str
