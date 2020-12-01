import sqlite3 # Instead of sql , we usesqlite its more or less the same as sql

#-----------------------------------------
# To obtain list of .db files

import glob
import os

os.chdir(r'.\Databases') #this changes working dir to database folder 
DatabaseList = glob.glob('*.db')
#-----------------------------------------
# Profile Choosing Or Creatiion [I should make a dlete function but thats for later]

if len(DatabaseList)== 0 :
    print("No Profiles Created")
    Profile = input("Enter new profile name to continue\n")+ ".db" 
else :
    print("Currently Active Profiles\n",DatabaseList)
    
    Tempvar1 = input("Enter Profile Index ,to make new profile type +\n") # just a temp variable that ill del later
    if Tempvar1 == "+":
        Profile = input("Enter new profile name to continue\n")+ ".db" 
    else:
        Profile = DatabaseList[int(Tempvar1)]
        
    del Tempvar1 # Deleting Temp Variable 

db = sqlite3.connect(Profile)

#-----------------------------------------

os.chdir(r'..\\') # Setting Back working dir to project folder

mycursor = db.cursor()


