import random 

n = random.randint(1,9)
a= input("Enter your Number\n")


if(a%8==0 and a%5==0):

    print("Your guess is inCorrect!")
    
else:
    print("Your guess is wrong!")
    
    print(f"The correct number was {n}")

