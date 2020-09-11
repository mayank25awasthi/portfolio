class PlayerCharacter(object):
	membership=True
	def __init__(self, name,age):
		if self.membership:
			self.name=name
			self.age=age
	def fn_shout(self):
		print(f'Hi My Name is {self.name}')

	def fn_run(self):
		print(f'Hi My Name is {self.name}')

player1=PlayerCharacter('Mayank',30)
player2=PlayerCharacter('Tarun',30)

player2.fn_run()
player1.fn_run()
print(player1.membership)