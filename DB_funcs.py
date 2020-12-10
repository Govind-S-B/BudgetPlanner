import sqlite3
import glob
import os

# TODO: add a way to delete profiles

def create_profile(profile_name: str) -> None:
    os.chdir(r'Profiles')  # this changes working dir to database folder

    sqlite3.connect(profile_name + '.db')  # creates the .db file
    open(profile_name + '.txt', 'w')

    os.chdir(r'..\\')  # Setting Back working dir to project folder

def get_databases() -> list:
    os.chdir(r'Profiles')  # this changes working dir to database folder

    database_list = glob.glob('*.db')  # gets a list of all files with a .db extension in \Profiles

    os.chdir(r'..\\')
    return database_list
# a plan is a table with an associated budget.
# each plan can have categories each with their own budgets and subcategories

def select_profile(profile_index: int):
    db_list = get_databases()

    os.chdir(r'Profiles')  # this changes working dir to database folder

    db = sqlite3.connect(db_list[profile_index])

    os.chdir(r'..\\')
    return db

def display_databases() -> None:
    database_list = get_databases()
    print("Currently Active profiles:")
    for i in range(len(database_list)):
        database = database_list[i]
        print(f'[{i}]' + database.replace('.db', ''))