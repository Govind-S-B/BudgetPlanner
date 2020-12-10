import sqlite3
import glob
import os


def profile(func):  # wrapper for functions that go into profiles directory
    with open('absolute_path.txt', 'r') as f:
        path = f.read()

    def wrapper(*args, **kwargs):
        cwd = os.getcwd()
        os.chdir(path)
        os.chdir(r'Profiles')  # this changes working dir to database folder
        return_value = func(*args, **kwargs)
        os.chdir(cwd)  # Setting Back working dir
        return return_value

    return wrapper


def set_absolute_path():
    with open('absolute_path.txt', 'w') as f:
        f.write(os.getcwd())


# TODO: add a way to delete profiles


@profile
def create_profile(profile_name: str) -> None:
    sqlite3.connect(profile_name + '.db')  # creates the .db file
    open(profile_name + '.txt', 'w')


@profile
def get_databases() -> list:
    database_list = glob.glob('*.db')  # gets a list of all files with a .db extension in \Profiles
    return database_list


@profile
def select_profile(profile_index: int):
    db_list = get_databases()
    db = sqlite3.connect(db_list[profile_index])
    return db


def display_databases() -> None:
    database_list = get_databases()
    print("Currently Active profiles:")
    for i in range(len(database_list)):
        database = database_list[i]
        print(f'[{i}]' + database.replace('.db', ''))
