
class db_init:
	def  __init__(self,db_cursor):
		self.db_cursor=db_cursor

	def create_table(self):
		self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS FLASK_PROJECT_DATA
										(USER_NAME TEXT,
										 USER_EMAIL TEXT,
										 USER_MESSAGE TEXT ); ''')