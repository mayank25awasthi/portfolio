import requests
import hashlib
import sys
def fn_pwd_api_response(pwd):
	url='https://api.pwnedpasswords.com/range/'+pwd
	rqst=requests.get(url)
	if rqst.status_code!=200:
		raise RuntimeError(f'Error while fetching URL {rqst.status_code}, change the uRL and try again')
	return rqst

def fn_calc_pwd_hacked(v_first5_char,v_tail):
	response=fn_pwd_api_response(v_first5_char).text.splitlines()
	for i in response:
		m,n=i.split(':')
		if m==v_tail:
			return n
	return 0

def fn_hash_convert(v_string):
	v_hash_pwd=hashlib.sha1(v_string.encode('utf-8')).hexdigest().upper()
	v_first5_char,v_tail=v_hash_pwd[0:5:],v_hash_pwd[5::]
	return fn_calc_pwd_hacked(v_hash_pwd[0:5:],v_tail)

def fn_main(args):
	for pwd in args:
		pwd_hack_count=fn_hash_convert(pwd)
		if pwd_hack_count:
			print(f'Hi Your Password was hacked {pwd_hack_count} times, You should probably change your password!!')
		else:
			print(f'Hi your has not been hacked,Carry on!!!')

#print(fn_hash_convert('hello')):
if __name__ == '__main__':
	fn_main(sys.argv[1:])