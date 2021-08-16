import mysql.connector
from mysql.connector import errorcode

def login():
    cursor = mydb.cursor()
    query = ("SELECT user, pass from login ")
    cursor.execute(query)

    for user, password in cursor:
        user = user
        password = password
    flag = True
    while flag:
        user_input = input("Username : ")
        password_input = input("Password : ")
        if user_input == user and password_input == password:
            print('You are Successfuly login ')        
            flag = False
            return True
        else:
            print("Wrong user or pass!!   try again...")

def show_menu():
    print("+"*20)
    print(
        "welcome to menu \n"
        "1- show my records \n"
        "2- add new records \n"
        "3- edit records\n"
        "4- delete records \n"
        "5- Exit "
    )
    user_number = int(input("Select your choice: "))
    return get_user_choice(user_number)

def get_user_choice(user_number):
    switcher = {
		1: lambda: show_all_records(),
		2: lambda: create_records(),
		3: lambda: edit_records(),
		4: lambda: delete_records(),
		5: lambda: exit()
	}
    choice_func = switcher.get(user_number)
    choice_func()


def show_all_records():
    cursor = mydb.cursor()
    query = ("Select website, pass from mypass")
    cursor.execute(query)
    myresult = cursor.fetchall()
    for item in myresult:
        print(item)

def create_records():
    print("===== Create =====")
    website_input = input("Entert Website : ")
    password_input = input ("Enter password :")

    cursor = mydb.cursor()
    query = (" INSERT INTO mypass (website,pass)"
            f"values ('{website_input}','{password_input}')"
    )
    cursor.execute(query)
    print("well done")
    mydb.commit()

def edit_records():
    print(" =========== edit ============")

    cursor = mydb.cursor()
    name_record = input("Enter website for edit :")

    user_choice = input("website or pass ( w - p )")

    if user_choice == "w":
        changed = input ("Enter new name of website : ")
        query = f"UPDATE mypass SET website = '{changed}' where website = '{name_record}'"
        cursor.execute(query)
        mydb.commit()
        print("well done")
        return
    if user_choice == "p":
        changed = input("Enter new pass for this website : ")
        query = f"UPDATE mypass SET website = '{changed}' where website = '{name_record}'"
        cursor.execute(query)
        mydb.commit()
        print("well done")        
        return
    else:
        print("wrong input")
    
    
    cursor = mydb.cursor()


def delete_records():
    print("======= delete ======= ")
    web = input("Enter your website :")
    cursor = mydb.cursor()
    query = (f"DELETE FROM mypass WHERE website = '{web}'")
    cursor.execute(query)
    mydb.commit()
    print("record deleted ")


if __name__ == '__main__':
    try:
        mydb = mysql.connector.connect(user='root',database='myPassword')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print(" ++ Welcome to Lockbox ++ ")
        
    if login():
        while True:
            show_menu()

    