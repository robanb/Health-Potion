# ask user it's email address
email = input("Enter your email address: ").strip()
# slice out the username
username = email[:email.index("@")]

# slice the domain name
domain = email[email.index("@")+1:]

# format the message
message = '''Your username is {} and your domain is {}'''.format(username, domain)

# dispaly the output message
print(message)