# check the number is prime or not 
'''
def fn_print_prime(v_input):
	if v_input>=1:
		if (v_input%2)==0:
			print('Not Prime')
		else :
			print('Prime number')
fn_print_prime(2)'''


# program to to check palindrone string

def fn_check_string(v_str):
	if v_str.upper()==v_str[::-1].upper():
		print('palindrome String')
	else:
		print('Not a palindrome')
fn_check_string('CIVI')