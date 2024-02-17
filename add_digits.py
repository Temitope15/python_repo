"""
Write a program that takes a two-digit number from the user and adds the digits
"""
num = input("Put in any two digit number: ")
sum_digits = int(num[0]) + int(num[1])
print("The sum of the individual digits of " + num + " is " + str(sum_digits) )