#Write a Program to extract each digit from an integer in the reverse order

num = int(input("enter your number :"))

reverse_num = 0 #create an empty place to make reverse of input num
while num > 0:
        reminder = num % 10
        num = num // 10
        print (reminder , end=" ")