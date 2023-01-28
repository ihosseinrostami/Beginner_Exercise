#Write a program to accept a string from the user
#and display characters that are present at an even index number.

string = input ("enter string: ")
length = len(string)

print ('only even index')
for i in range(0, length-1, 2):
    print('index[', i ,']',string[i])
