import sqlite3 # Instead of sql , we usesqlite its more or less the same as sql
import glob # To obtain list of .db files
import os


os.chdir(r'.\Databases') #this changes working dir to database folder 
database_list = glob.glob('*.db')  #gets a list of all files with a .db extension in \Databases

# profile Choosing Or Creation
# TODO: add a way to delete profiles

if len(database_list)== 0:  # checks if a database already exists
    print("No profiles Created")
    profile = input("Enter new profile name to continue\n")+ ".db"
else:
    print("Currently Active profiles:")
    for i in range(len(database_list)):
        database = database_list[i]
        print(f'[{i}]'+database.replace('.db',''))
    
    profile_choice = input("Enter profile Index ,to make new profile type +\n") # just a temp variable that ill del later
    if profile_choice == "+":
        profile = input("Enter new profile name to continue\n")+ ".db"
    else:
        profile = database_list[int(profile_choice)]
        
    del profile_choice # Deleting Temp Variable

db = sqlite3.connect(profile)  # creates the .db file

os.chdir(r'..\\') # Setting Back working dir to project folder
#-----------------------------------------
# from here is normal SQL
cursor = db.cursor()


