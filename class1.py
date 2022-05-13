import sqlite3 
class Sql:
	def __init__(self):
		self.connection = sqlite3.connect('class1.db')
		self.cursor = self.connection.cursor()

	def yaratish(self):
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(
			id integer,
			username varchar(15),
			firstname varchar(15)
			)""")

	def qoshish(self,idi,username,firstname):
		self.cursor.execute("INSERT INTO user (id,username,firstname) VALUES (?,?,?)", (idi,username, firstname))
		return self.connection.commit()

	def id_user(self,idi):
		self.cursor.execute(f'SELECT id FROM user WHERE id = {idi}')
		data = self.cursor.fetchone()
		return data

	def aluser(self,idi):
		self.cursor.execute(f'SELECT COUNT (id) FROM user')
		data2 = self.cursor.fetchall()
		return data2



