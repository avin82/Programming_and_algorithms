# PROGRAM Factorial:
num = int(input("Please input the number for which the factorial needs to be calculated: \n"))
temp = num
product = 1
while num != 0:
# DO
	product = product * num
	num = num - 1
# ENDWHILE;
print("The factorial of {} is {}\n".format(temp, product))
# END.
