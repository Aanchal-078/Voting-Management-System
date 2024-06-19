import re
import random
import mysql.connector as c
conn = c.connect(user="root", password="", database="voter_db")
# Fetching aadhar no. from voter_info table of all registered voters
sql = 'select aadhar from voter_info'
myc = conn.cursor(buffered=True)
myc.execute(sql)
r = myc.fetchall()
result_string = ([i[0] for i in r])

def sign_up():
    while True:
    # Validating the aadhar no. if it already exist or not
        aadhar = input("\nEnter you aadhar no.: ")
        if(aadhar in result_string):
            print("This aadhar already exist!!!")
        elif(len(aadhar)==12 and aadhar.isnumeric):
            break
        else:
            print("Incorrect aadhar no.")
    # Fetching user details
    firstname = input("Enter first name: ").upper()
    lastname = input("Enter last name: ").upper()
    gender = input("Enter your gender(M/F/Other): ").upper()
    while True:
    #Validating Date of Birth if its in correct syntax
        dob = input("Enter your date of birth(yyyy-mm-dd): ")
        d = re.compile(r"[0-2][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]")
        if re.fullmatch(d, dob):
            break
        else:
            print("Invalid DOB Syntax")
    while True:
    # Checking if the length of mobile no. is 10 or not
        contact = input("Enter your contact no.: ")
        if(len(contact)==10):
            break
        else:
            print("Incorrect contact no.")
    while True:
    # Checking if email address is valid or not
        email = input("Enter your email: ")
        d = re.compile(r"[A-Za-z0-9]+@gmail+\.com")
        if re.fullmatch(d, email):
            break
        else:
            print("Invalid Email Syntax")
    # Taking the user's address information
    print("\nEnter your permanent adress: ")
    house = input("Enter your house no.: ")
    locality = input("Enter your locality: ")
    landmark = input("Enter landmark: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    pincode = input("Enter pincode: ")
    while True:
        # taking user password and rechecking it
        password = input("Enter new password: ")
        repass = input("Enter password again: ")
        if(password==repass):
            break
        else:
            print("Both passwords doesn't match")
    # inserting all the data of new user in voter_info table
    sql = 'insert into voter_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    data = (aadhar, firstname, lastname, gender, dob, contact, email, house, locality, landmark, city, state, pincode, password)
    myc = conn.cursor()
    myc.execute(sql,data)
    conn.commit()
    print("Your account created successfully!!!")
    voter_id(firstname, lastname, aadhar, password)
    

def voter_id( firstname, lastname, aadhar, password):
    # Randomly generating voter Id
    id = firstname[:2]+lastname[0]+str(random.randint(100000,999999))
    # Inserting the voter Id, aadhar and password into login table to validate when user login
    sql = 'insert into login values(%s,%s,%s)'
    data = (id, aadhar, password)
    myc = conn.cursor()
    myc.execute(sql,data)
    conn.commit()
    print("Your voter ID is : ",id)
    print("Save it for future reference")
    main_menu()



def log_in():
    sql = 'select voter_id from login'
    myc = conn.cursor(buffered=True)
    myc.execute(sql)
    r = myc.fetchall()
    result_string = ([i[0] for i in r])
    while True:
        id = input("Enter your Voter ID: ")
        aadhar = input("Enter your Aadhar no.: ")
        password = input("Enter password: ")
        # Validating if voter Id exist or not
        if id not in result_string:
            print("Invalid voter ID")
        else:
            break
    while True:
        print("Choose any option: ")
        print("1. To update any information: ")
        print("2. To give vote")
        print("3. Go to main menu")
        print("4. Exit app")
        ch = int(input("Enter one option: "))
        if(ch==1):
            upd_info(aadhar)
        elif(ch==2):
            give_vote(id)
        elif(ch==3):
            main_menu()
        elif(ch==4):
            exit(0)
        else:
            print("Choose correct option: ")


def upd_info(aadhar):
    while True:
        # Updating user information whichever it will choose
        print("Which detail you want to change: ")
        print("1. Aadhar No. \n2. First Name \n3. Last Name \n4. Gender \n5.Date of birth \n6. Contact No. \n7. Email \n8. Address ")
        n = int(input("Enter your choice: "))
        if(n==1):
            ad = input("Enter new aadhar no.: ")
            sql = 'update voter_info set aadhar=%s where aadhar=%s'
            data = (ad,aadhar)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
            sql = 'update login set aadhar=%s where aadhar=%s'
            data = (ad,aadhar)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
        elif(n==2):
            fname = input("Enter first name: ")
            sql = 'update voter_info set fname=%s where aadhar=%s'
            data = (fname,aadhar)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
        elif(n==3):
            lname = input("Enter last name: ")
            sql = 'update voter_info set lname=%s where aadhar=%s'
            data = (lname,aadhar)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
        elif(n==4):
            gender = input("Enter your gender: ")
            sql = 'update voter_info set gender=%s where aadhar=%s'
            data = (gender,aadhar)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
        elif(n==5):
            dob = input("Enter your date of birth(yyyy-mm-dd): ")
            sql = 'update voter_info set dob=%s where aadhar=%s'
            data = (dob,aadhar)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
        elif(n==6):
            contact = input("Enter your contact no.: ")
            sql = 'update voter_info set contact=%s where aadhar=%s'
            data = (contact,aadhar)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
        elif(n==7):
            email = input("Enter your new email: ")
            sql = 'update voter_info set email=%s where aadhar=%s'
            data = (email,aadhar)
            myc = conn.cursor()
            myc.execute(sql,data)
            conn.commit()
        elif(n==8):
            while True:
            # Updating the user's address information
                print("Choose an option: ")
                print("1. Change house no")
                print("2. Change locality")
                print("3. Change landmark")
                print("4. Change City")
                print("5. Change State")
                print("6. Change pincode")
                ch = int(input("Enter an option: "))
                if(ch==1):
                    house = input("Enter your house no: ")
                    sql = 'update voter_info set house=%s where aadhar=%s'
                    data=(house,aadhar)
                    myc = conn.cursor()
                    myc.execute(sql,data)
                    conn.commit()
                elif(ch==2):
                    locality = input("Enter your locality: ")
                    sql = 'update voter_info set locality=%s where aadhar=%s'
                    data=(locality,aadhar)
                    myc = conn.cursor()
                    myc.execute(sql,data)
                    conn.commit()
                elif(ch==3):
                    landmark = input("Enter your new landmark: ")
                    sql = 'update voter_info set landmark=%s where aadhar=%s'
                    data=(landmark,aadhar)
                    myc = conn.cursor()
                    myc.execute(sql,data)
                    conn.commit()
                elif(ch==4):
                    city = input("Enter your new city: ")
                    sql = 'update voter_info set city=%s where aadhar=%s'
                    data=(city,aadhar)
                    myc = conn.cursor()
                    myc.execute(sql,data)
                    conn.commit()
                elif(ch==5):
                    state = input("Enter state: ")
                    sql = 'update voter_info set state=%s where aadhar=%s'
                    data=(state,aadhar)
                    myc = conn.cursor()
                    myc.execute(sql,data)
                    conn.commit()
                elif(ch==6):
                    pincode = input("Enter new pincode: ")
                    sql = 'update voter_info set pincode=%s where aadhar=%s'
                    data=(pincode,aadhar)
                    myc = conn.cursor()
                    myc.execute(sql,data)
                    conn.commit()
                else:
                    print("Choose correct option")
                n = int(input("Do you want to change other address information? If no enter 0 else enter 1: "))
                if(n==0):
                    break
        else:
            print("Choose correct option")
        ch = int(input("Do you want to change any other information? If no enter 0 else enter 1: "))
        if(ch==0):
            break
    main_menu()


def give_vote(id):
    sql = 'select voter_id from voting'
    myc = conn.cursor(buffered=True)
    myc.execute(sql)
    r = myc.fetchall()
    result_string = ([i[0] for i in r])
    if(id in result_string):
        # Checking if user had already given vote
        print("You have already given vote")
        main_menu()
    # Displaying the party information who are standing in election
    sql = 'select name, symbol from party'
    myc.execute(sql)
    r = myc.fetchall()
    for i in r:
        print(i[0]," : ",i[1])
    # Taking user input whom it want to give vote
    symbol = input("Enter the symbol of the party you want to vote: ").lower()
    sql = 'insert into voting values(%s,%s)'
    data=(id,symbol)
    myc = conn.cursor()
    myc.execute(sql,data)
    conn.commit()
    print("You have voted successfully!!!")
    main_menu()

def party():
    aadhar = input("Enter aadhar no.: ")
    if(aadhar not in result_string ):
        # Validating if party has already signed in or not
        print("You first need to sign up")
        ch = input("Do you want to sign up (Y/N): ").upper()
        if(ch=='Y'):
            sign_up()
        else:
            main_menu()
    # Taking party information along with its symbol
    name = input("Enter party name: ").upper()
    symbol = input("Enter your party symbol: ").lower()
    sql = 'insert into party values(%s,%s,%s)'
    data = (aadhar,name,symbol)
    myc = conn.cursor()
    myc.execute(sql,data)
    conn.commit()
    # Inserted data in the table of the new party
    print("Party created successfully!!!")
    main_menu()

def result():
    sql = 'select symbol from party'
    myc = conn.cursor(buffered=True)
    myc.execute(sql)
    r = myc.fetchall()
    result_string = ([i[0] for i in r])
    max_votes = 0
    winner = "none"
    # Comparing the votes of all parties and showing the result
    for i in result_string:
        sql = 'select * from voting where symbol=%s'
        myc = conn.cursor(buffered=True)
        myc.execute(sql, (i,))
        rows = myc.fetchall()
        votes = len(rows)
        if(votes>max_votes):
            max_votes = votes
            winner = i
    sql = 'select name from party where symbol=%s'
    data=(winner,)
    myc.execute(sql, data)
    r = myc.fetchall()
    name = ([i[0] for i in r])
    print("Winner party is  : ",name[0],"(",winner,") with", max_votes, "votes.")
    main_menu()


def main_menu():
    print("\nChoose any option")
    print("1. Sign Up (Doesn't have an voter ID)")
    print("2. Login In (Already have an voter ID)")
    print("3. Add new party")
    print("4. Show election results")
    print("5. Exit")
    n = int(input("Enter one option: "))
    if(n==1):
        sign_up()
    elif(n==2):
        log_in()
    elif(n==3):
        party()
    elif(n==4):
        result()
    elif(n==5):
        exit(0)
    else:
        print("Choose correct option")
        main_menu()

main_menu()