from DB_funcs import *

if input("add new profile?(y/n)") == 'y':
    profile = input("Enter new profile name to continue: ")
    create_profile(profile)

display_databases()

profile_index = int(input("Enter profile Index: "))
db = select_profile(profile_index)
# -----------------------------------------
