#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

previous_num = 0

#creat a loop to count from 1 to 10
for i in range(1,10):
    sum = previous_num + i
    print ("current num", i, "previous_num", previous_num, "sumation", sum)
    previous_num = i