import sys
import subprocess

scripts = [sys.executable,"sys_sample.py","exit.py"] #sys.executable gives you path to 'Python.exe'
code = subprocess.call(scripts)
print(code)