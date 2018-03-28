import datetime

class Moderators():
	"""a moderator can only edit their own comment"""
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def new_moderator(self, username, password):
		self.username = username
		self.password = password
		return users.update(user)

	def add_comment(self, author, comment):
		self.author = author
		self.comment = comment
		return comments.update()

	def delete_comment(self,author, comment):
"""this method accesses the comments dictionary that maps
   users comments contained in a dictionary also 
   example >>Comments_dict = {user1:{comments}, user2:{comments} """
		self.commment = comment
		self.author = author
		c = comments[author][commment]
		del c
		return comments

	def login(self,  timestamp,):
		self.timestamp = datetime