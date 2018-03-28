users = {"njeri":"123", "kelvin":"were"}
moderators = {"serah":"123","mike":"123"}
admin = {"steve":"456"}

print("HELLO, WELCOME!")

user_type = input()

if user_type == "user":
    print("I am a user")
    username = input("username:")
    password = input("password:")
    
    
    if username in users:
        my_user = Users()
        if (password  == users[username]):
            command = input("add, edit, delete comment?")
            if command == "add":
                comment = input("enter comment")
                my_user.add_comment("comment")
            if command == "edit":
                comment = input("Enter your changes")
                my_user.edit_comment()
            if command == "delete":
                comment == input("Enter timestamp:")
                my_user.delete_comment(comment)
            else: 
                print("invalid command!")
        else:
            print("invalid password")
    else:
        print("username doesn't exist")
    

if user_type == "moderator":
    username = input("username:")
    password = input("password:")
        
    if username in moderators:
        my_moderator = Moderators()
        if (password  == users[username]):
            command = input("delete comment?")
            
            else: 
                print("invalid command!")
        else:
            print("invalid password")
    else:
        print("username doesn't exist")

if user_type == "admin":
	print("I am an admin")