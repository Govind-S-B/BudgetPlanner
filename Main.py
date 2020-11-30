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

mycursor.execute('show databases')


for database in mycursor:
    if database[0] == 'budget_planner':
        mycursor.fetchall()  #to clear any extra stuff in the cursor, otherwise we cant execute anything else.
        break
else:
    mycursor.execute('CREATE DATABASE Budget_Planner')

mycursor.execute('USE Budget_Planner')
