# PROGRAM PrimeChecker:
num = int(input("Please input a number you would want to be checked for being prime or not: \n"))
divisor = num - 1
is_prime = True
while divisor != 1:
# DO
	if num % divisor == 0:
	# THEN
		is_prime = False
	# ENDIF;
	divisor = divisor - 1
# ENDWHILE;
if is_prime:
# THEN
	print(num, "is a prime number")
else:
	print(num, "is not a prime number")
# ENDIF;
# END.
