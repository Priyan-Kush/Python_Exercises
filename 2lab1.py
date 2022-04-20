def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str


a=input("Enter a string \n")
print(reverse(a))
