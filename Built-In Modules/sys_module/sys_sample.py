import sys 

print(sys.argv)
print(sys.executable) #Path to Python Interpreter.
# Exit from Python.
# sys.exit(0) # Zero is considered as successful termination.
print()
print("Paths to modules")
print(sys.path)
sys.path.append("Users/shahzaibnoor/Documents/Projects/python_babysteps/")
print()
print("New Paths")
print(sys.path)
sys.path.pop()
print()
print("Paths restored.")
print(sys.path)

def check_platform(sys_module):
   print(f"Platform on which Python is running: {sys_module.platform}")
   if sys_module.platform == "darwin":
       print(f"Platform is darwin, so lets dance!")

check_platform(sys)