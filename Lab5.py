# Course: IT1114/Section 01
# Student Name: Garrett Cook
# Assignment Number: Lab5
# Due Date: 02/27/2024
# Purpose:Write a program that will prompt the user for a starting number and an ending number,
# and will print all the prime numbers between the starting number and ending number
# inclusively
#Sources for help Module 4 exercises ,https://www.programiz.com/python-programming/examples/prime-number-intervals


x = int(input("Starting Number:"))
y = int(input("Ending Number: "))
is_prime=True
#the range selected by the user will be tested in the formula before if the numbers within are prime or not.
#If they are then they get printed only "prime = true"

for i in range(x,y+1):#needed to look up some examples chceking if a number is prime.
 #if it's one number range then we can just use "range(2,int(x/2)+2)":
#Since we needed to check every number inbetween we looked up some examples and studied programs in module 4 exercises.
#start at 0 so we can include 1
   if i > 0:
#indention is very important
    for num in range(2,i):
         if (i % num) ==0:
            is_prime=False
            break
    else:
        print(i,"Is prime ")
