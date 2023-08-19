import mysql.connector

class Database:
	def __init__(self):
		self.connection = mysql.connector.connect(
			host='localhost',
			user='root',
			password='adminuser',
			database='Todo_List_app_db')
		self.cursor = self.connection.cursor()

	def get_task(self):
		query = 'SELECT ID, task FROM tasks'
		self.cursor.execute(query)
		tasks = self.cursor.fetchall()
		return tasks

	def insert_task(self, task):
		query = 'INSERT INTO tasks (task) VALUES (%s)'
		self.cursor.execute(query, (task,))
		self.connection.commit()

	def delete_task(self, task_id):
		query = 'DELETE FROM tasks where id = %s'
		self.cursor.execute(query, (task_id,))
		self.connection.commit()

	def search_tasks(self, query):
		query_string = "SELECT * FROM tasks WHERE task LIKE %s"
		self.cursor.execute(query_string, (f"%{query}%",))
		tasks = self.cursor.fetchall()
		print("search results:", tasks)
		return tasks

		
	def __del__(self):
		self.cursor.close()
		self.connection.close()