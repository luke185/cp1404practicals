password = input("Password: ")
while len(password) < 8:
    print("Password must be at least 8 characters!")
    password = input("Password: ")
for i in password:
    print('*', end='')
