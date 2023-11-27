def main():
    password = get_password()
    for i in password:
        print('*', end='')


def get_password():
    password = input("Password: ")
    while len(password) < 8:
        print("Password must be at least 8 characters!")
        password = input("Password: ")
    return password


main()
