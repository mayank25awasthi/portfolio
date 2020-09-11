import datetime
import pytz


class Accounts:
	def __init__(self,name,balance):
		self.__name=name
		self.__balance=balance
		print(f'Hi Accounts has been created for {self.__name} ')
		self.balance_log=[(Accounts._current_time(),self.__balance)]
		self.fn_show_balance()
	@staticmethod
	def _current_time():
		utc_time=datetime.datetime.utcnow()
		return pytz.utc.localize(utc_time)

	def fn_deposit(self,v_amount):
		if v_amount>0:
			self.__balance+=v_amount
			self.fn_show_balance()
		self.balance_log.append((self._current_time(),v_amount))

	def fn_withdraw(self,v_amount):
		if 0<v_amount<self.__balance:
			self.__balance-=v_amount
			self.fn_show_balance()
		else :
			print(f'Hi {self.__name} withdraw amount shoul be greater than zero and less than your balance amount')
			#self.fn_show_balance()
		self.balance_log.append((self._current_time(),-v_amount))

	def fn_show_balance(self):
		print(f'Your total Account Balance is {self.__balance}')

	def fn_trans_log(self):
		for time,blc in self.balance_log:
			if blc>0:
				tran_type='Deposit'
			else:
				tran_type='Withdrwan'
				blc*=-1
			print(f'{blc} {tran_type} on {time} local time was {time.astimezone()}')


'''v_client=Accounts('Mayank',10000)
v_client.fn_deposit(5000)
v_client.fn_show_balance()	
v_client.fn_withdraw(10000)
v_client.fn_trans_log()
v_client.fn_show_balance()'''

tarun=Accounts('tarun',10000)
tarun._balance=5000
tarun.fn_deposit(2000)
tarun.fn_withdraw(5000)
tarun.fn_trans_log()
tarun.fn_show_balance()
print(tarun.__dict__)
tarun._Accounts__balance=3000
tarun.fn_show_balance()