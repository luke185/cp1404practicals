"""
Emails
Estimate: 15 minutes 00 seconds
Actual:   23 minutes 33 seconds
"""

email_to_name = {}

email = input('Email: ')
while email != '':
    email_name_original = email[:email.find('@')].title().split('.')
    email_name_joined = ' '.join(email_name_original)
    prompt = input(f'Is your name {email_name_joined}? (Y/n) ').upper()
    if prompt == 'Y' or prompt == '':
        name = email_name_joined
    else:
        name = input('Name: ')
    email_to_name[email] = name
    email = input('Email: ')

for email, name in email_to_name.items():
    print(f"{name} ({email})")
