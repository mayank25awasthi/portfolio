import sqlite3,os

class Database:
	def __init__(self,db_name):
		self.db_name=db_name
		db_file_path=os.path.dirname(os.path.abspath(__file__))
		db_file_path=os.path.join(db_file_path,self.db_name)
		self.db_obj=sqlite3.connect(db_file_path)
		self.db_cursor=self.db_obj.cursor()
		self.utable='user'
		query=f"select count(*) from {utable}"
		resp=self.execute_query(query)[0][0]

	def execute_query(self,query):
		resp=(None,None)
		try:
			resp=self.db_cursor.execute(query).fetchall()
			self.db_obj.commit()
		except exception as fault :
			print('Something Went Wrong !!')

	def create_user(self,user_name,user_email,user_message):
		query="insert into %s (user_name,user_email,user_message) values(%s,%s,%s) ;" %(self.utable,user_name,user_email,user_message)
		self.execute_query(query)
		