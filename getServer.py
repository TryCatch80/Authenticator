import sys
username = sys.argv[1]
password = sys.argv[2]

if not password:
     print("Missing secret: " + username)
elif password == 'secret':
    print('Authenticated')
else:
    print("Login failed!")
