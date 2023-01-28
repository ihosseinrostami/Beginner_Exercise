#Iterate the given list of numbers and print only those numbers which are divisible by 5

#creating an empty list
lst = []

#get number of elements from user
n = int(input("enter number of element:")) #define number of element


for i in range(0,n):
    element = int(input()) #define element
    lst.append(element) #get elements from user and add to list
print (lst)

num = lst
for num in lst:
    if num % 5 == 0:
        print(num)
        
        
        