# PROGRAM FindFibonacciNumber:
position = int(input("Please input the position (i.e. positive integer value) for which you want to find the Fibonacci number in the Fibonacci series: \n"))
temp_pos = position
first_num = 1
second_num = 1
if (position == 1) or (position == 2):
# THEN
	print("Fibonacci number at the position {} is {}".format(position, first_num))
else:
	while position != 2:
	# DO
		fib = first_num + second_num
		first_num = second_num
		second_num = fib
		position = position - 1
	# ENDWHILE;
	print("Fibonacci number at the position {} is {}".format(temp_pos, fib))
# ENDIF;
# END.
