def isprime(num):
    if num == 2 or num == 3:
      return True
    if num < 2 or num%2 == 0:
      return False
    if num < 9:
      return True
    if num%3 == 0:
      return False

e = int(input("Enter the number\n"))    
print(isprime(e))
