#Write a program to check if the given number is a palindrome number.
#A palindrome number is a number that is same after reverse.
#For example 545, is the palindrome numbers.

num = int(input("enter your number :"))

# reverse the given number
reverse_num = 0 #create an empty place to make reverse of input num
while num > 0:
        reminder = num % 10
        reverse_num = (reverse_num * 10) + reminder
        num = num // 10
if num == reverse_num:
        print("Given number palindrome")
else:
        print("Given number is not palindrome")