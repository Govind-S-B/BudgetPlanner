import mysql.connector

try:  #checks if password and username have been given before
    with open('password.txt','r') as file:
        info = dict(user=file.readline(), passwd=file.readline())


except FileNotFoundError:  #if the username and password has not been given yet
    with open('password.txt', 'w') as file:

        username = input('enter SQL username: ')
        password = input('enter SQL password: ')

        file.write(username + '\n')

        file.write(password)
        info = {
            'user': username,
            'passwd': password
        }

db = mysql.connector.connect(
    host="localhost",
    user=info['user'],
    passwd=info['passwd'],
)

mycursor = db.cursor()
print('it fucking worked? what?')