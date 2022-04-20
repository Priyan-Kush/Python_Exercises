
# a= input_list = [1, 2, 2, 5, 8, 4, 4, 8] 
a = input("Enter a list\n")

empty_list = [] 

count = 0

for ele in a:
    if(ele not in a):
        count += 1
        a.append(ele) 

print("Count of unique values are:", count)
