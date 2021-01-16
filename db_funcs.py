from datetime import date
import sqlite3 as sq

def create_expenses_table(db):
    cursor = db.cursor
    cursor.execute('CREATE TABLE Expenses (ID INTEGER PRIMARY KEY, Expenditure INT NOT NULL, Date DATE NOT NULL, Info VARCHAR(100) NOT NULL, Essential BIT NOT NULL)')
    connection.commit()

def get_next_id(db):
    cursor = db.cursor()
    cursor.execute("select ID from Expenses")
    return max([i[0] for i in cursor.fetchall()])+1


def clear_all(db):
    cursor = db.cursor()
    cursor.execute('DELETE FROM Expenses')
    connection.commit()


def insert(db, expenditure, info='', essential=False):
    cursor = db.cursor()

    cursor.execute("INSERT INTO Expenses VALUES({},{},{},{},{})".format(get_next_id(db), expenditure, f"'{date.today()}'", f"'{info}'", int(essential)))
    connection.commit()


def get_monthly_expenditure(db, essential=None):
    cursor = db.cursor()
    first_of_cur_month = date.strftime(date.today(), "%Y-%m-01")

    sql_text = f'SELECT SUM(Expenditure) FROM EXpenses WHERE Date >= {first_of_cur_month}'

    if essential is True:
        sql_text += ' AND Essential = 1'
    elif essential is False:
        sql_text += ' AND Essential = 0'
    print(sql_text)
    cursor.execute(sql_text)

    return cursor.fetchall()[0][0]


'''
connection = sq.connect('test.db')
cursor = connection.cursor()
insert(connection, 100, 'fdf', False)
print(get_monthly_expenditure(connection,False))




connection.commit()
'''