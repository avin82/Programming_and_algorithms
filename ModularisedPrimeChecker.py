# PROGRAM ModularisedPrimeChecker:

#########################
# Prime Checking Module #
#########################


def IsItPrime():
	num = int(input("Please input a number you want to be checked for being prime or not: \n"))
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
	return is_prime

# END IsItPrime.


################
# Main Program #
################

if IsItPrime():
# THEN
	print("It is a prime number.")
else:
	print("It is not a prime number.")
# ENDIF;

# END.
