import string 
import random

n = int(input("Enter the length of the string\n"))

r= "".join(random.choices(string.ascii_uppercase, k=n))
print(r)