# PROGRAM ModularisedCalcFibonacci:

#########################
# Calc Fibonacci Module #
#########################


def CalcFibonacci():
	position = int(input("Please input the position (i.e. positive integer value) for which you want to find the Fibonacci number in the Fibonacci series: \n"))
	first_num = 1
	second_num = 1
	if (position == 1) or (position == 2):
	# THEN
		return first_num
	# ENDIF;
	while position != 2:
	# DO
		fib = first_num + second_num
		first_num = second_num
		second_num = fib
		position = position - 1
	# ENDWHILE;
	return fib
# END CalcFibonacci.


################
# Main Program #
################

print("Fibonacci number at the inputted position is {}".format(CalcFibonacci()))
# END.
