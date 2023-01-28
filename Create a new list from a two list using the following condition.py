#Create a new list from a two list using the following condition
#Given a two list of numbers
#write a program to create a new list such that the new list should contain
#odd numbers from the first list
#and even numbers from the second list.

#creating an empty list
lst1 = []
lst2 = []
#get number of elements from user
n = int(input("enter number of element:")) #define number of element
print ("enter your list1 number :")

for i in range(0,n):
    element1 = int(input()) #define element
    lst1.append(element1) #get elements from user and add to list
list1 = lst1
print (list1)

m = int(input("enter number of element:")) #define number of element
print ("enter your list2 number :")

for j in range(0,m):
    element2 = int(input()) #define element
    lst2.append(element2) #get elements from user and add to list
list2 = lst2
print (list2)

merge_list = []
for element1 in list1:
    if element1 % 2 != 0:
        # add odd number to result list
        merge_list.append(element1)
        
for element2 in list2:        
    if element2 % 2 == 0:
        merge_list.append(element2)

print(merge_list)


        