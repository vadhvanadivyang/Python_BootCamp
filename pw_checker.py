username = input("Please enter your username: ")
password = input("Please enter your password: ")

pw_length = len(password)
hidden_pw = '*' * pw_length

print(f"Hey {username}, Your Password {hidden_pw} is {pw_length} characters long")
