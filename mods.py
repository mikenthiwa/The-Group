import datetime

class Moderators():
	"""a moderator can only edit their own comment"""
	def __init__(self):
		pass

	def new_moderator(self, username, password):
		self.username = username
		self.password = password

	def add_comment(self, author, comment):
		self.author = author
		self.comment = comment

	def delete_comment(self,author, comments):
		self.commment = comment
		self.author = author
		c = comment comments[author][commment]
		del c
		return comments

	def login(self, timestamp,):
		self.timestamp = datetime