comments = {}

class NormalUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def creat_normal_user(self):
        normal_user = {self.username, self.password}
        return normal_user

    def create_new_comment(self, author, comment):
        # self.author = author
        # self.comment = comment
        new_comment = comment[author] = comment
        return new_comment

    def remove_comment(self):
        del comments['author']


user = input("Enter username and password")
# user = NormalUser('mike','1234')

# print(user.creat_normal_user())
comments = input("Enter you comments : ")
print("Username and password is", :user)
print("comments are : ", comments)






