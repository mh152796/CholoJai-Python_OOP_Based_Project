import os


import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="mh152796",
    password="DIU53cse@2796",
    database="cholojai"
)
mycursor = mydb.cursor()
# Admin List-->
admin_list = []
# Customer list-->
list1 = []
# travel list dictionary-->
travel = {1: 'Barisal', 2: 'Chattrogram', 3: 'Dhaka', 4: 'Khulna', 5: 'Mymensingh', 6: 'Rajshahi', 7: 'Rangpur', 8: 'Sylhet',
          9: "Cox's Bazar", 10: 'Saint Martin'}

class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password


# Objects Of Admin-->
admin1 = Admin("Mosaraf Hossain", "2796")
admin2 = Admin("Anisur Rahman", "2825")
admin_list.append(admin1)
admin_list.append(admin2)


def adminpage(name):
    p = name
    print(f"Welcome {name}")
    print("----------------------------")
    print("1.Total Customers           |")
    print("2.Customers Information     | ")
    print("3.Manage Customers          |")
    print("4.Go Back To Log-In Page    |")
    print("----------------------------")
    sl = input("Please Select An Option: ")
    if sl == "1":
        mycursor.execute("SELECT * FROM customers")
        mycursor.fetchall()
        number_of_customers = mycursor.rowcount
        print(f"Total Customers: {number_of_customers}")
        ch = input("PRESS 'B' TO GO BACK: ")
        if ch.upper() == 'B':
            os.system('cls')
            adminpage(p)

    elif sl == "2":
        i = 1
        mycursor.execute("SELECT * FROM customers")
        customers = mycursor.fetchall()

        for customer in customers:
            print(f"{i}.{customer}")
            i = i + 1

        ch = input("PRESS 'B' TO GO BACK: ")
        if ch.upper() == 'B':
            os.system('cls')
            adminpage(p)
    elif sl == "3":
        i = 1
        mycursor.execute("SELECT * FROM customers")
        customers = mycursor.fetchall()

        for customer in customers:
            print(f"{i}.{customer}")
            i = i + 1

        print("1.Delete Customer")
        print("2.Go Back ")
        a = input("Please Select An Option: ")
        if a == '1':
            d = input("Enter the Username for deleting a customer : ")
            sql = f"DELETE FROM customers WHERE Username= '{d}' LIMIT 1"
            mycursor.execute(sql)
            mydb.commit()
            usr = f"DELETE FROM login WHERE Username= '{d}' LIMIT 1"
            mycursor.execute(usr)
            mydb.commit()

            print("Customer Deleted!!!")
            print("Press ENTER To Continue...")
            a = input()
            os.system('cls')
            adminpage(p)
        elif a == '2':
            os.system('cls')
            adminpage(p)

    elif sl == "4":
        os.system('cls')
        loginPage()
    else:
        print("Wrong Option Selected!!!")
        print("Press ENTER To Continue...")
        a = input()
        os.system('cls')
        adminpage(p)





class Information:
    def __init__(self, name, username, password, email, phonenumber, dob, address,fav):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.phonenumber = phonenumber
        self.dob = dob
        self.address = address
        self.fav3 = fav
    # noinspection PyMethodMayBeStatic
    def travel_info(self, location, destination):
        # Barisal
        if location == "Barisal" and destination == "Chattrogram":
            barisal_chattrogram = open("Barisal_Chattrogram.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(barisal_chattrogram.read())
            barisal_chattrogram.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Barisal" and destination == "Dhaka":
            barisal_dhaka = open("Barisal_Dhaka.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(barisal_dhaka.read())
            barisal_dhaka.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Barisal" and destination == "Khulna":
            barisal_khulna = open("Barisal_Khulna.txt.", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(barisal_khulna.read())
            barisal_khulna.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Barisal" and destination == "Mymensingh":
            barisal_mymensingh = open("Barisal_Mymensingh.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(barisal_mymensingh.read())
            barisal_mymensingh.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Barisal" and destination == "Rajshahi":
            barisal_rajshahi = open("Barisal_Rajshahi.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(barisal_rajshahi.read())
            barisal_rajshahi.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Barisal" and destination == "Rangpur":
            barisal_rangpur = open("Barisal_Rangpur.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(barisal_rangpur.read())
            barisal_rangpur.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Barisal" and destination == "Sylhet":
            barisal_sylhet = open("Barisal_Sylhet.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(barisal_sylhet.read())
            barisal_sylhet.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Barisal" and destination == "Cox's Bazar":
            barisal_cox = open("Barisal_Cox'sbazar.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(barisal_cox.read())
            barisal_cox.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Barisal" and destination == "Saint Martin":
            barisal_martin = open("Barisal_Saint-martin.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(barisal_martin.read())
            barisal_martin.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        # Dhaka
        if location == "Dhaka" and destination == "Chattrogram":
            dhaka_chattrogram = open("Dhaka_Chattrogram.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(dhaka_chattrogram.read())
            dhaka_chattrogram.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Dhaka" and destination == "Barisal":
            dhaka_barisal = open("Dhaka_Barisal.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(dhaka_barisal.read())
            dhaka_barisal.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Dhaka" and destination == "Khulna":
            dhaka_khulna = open("Dhaka_Khulna.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(dhaka_khulna.read())
            dhaka_khulna.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Dhaka" and destination == "Mymensingh":
            dhaka_mymensingh = open("Dhaka_Mymensingh.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(dhaka_mymensingh.read())
            dhaka_mymensingh.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Dhaka" and destination == "Rajshahi":
            dhaka_rajshahi = open("Dhaka_Rajshahi.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(dhaka_rajshahi.read())
            dhaka_rajshahi.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Dhaka" and destination == "Rangpur":
            dhaka_rangpur = open("Dhaka_Rangpur.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(dhaka_rangpur.read())
            dhaka_rangpur.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Dhaka" and destination == "Sylhet":
            dhaka_sylhet = open("Dhaka_Sylhet.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(dhaka_sylhet.read())
            dhaka_sylhet.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Dhaka" and destination == "Cox's Bazar":
            dhaka_cox = open("Dhaka_Cox'sbazar.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(dhaka_cox.read())
            dhaka_cox.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        if location == "Dhaka" and destination == "Saint Martin":
            dhaka_saint = open("Dhaka_Saint-martin.txt", "r")
            print("--------------------------------------------------------------------------------------------------")
            print(dhaka_saint.read())
            dhaka_saint.close()
            print("--------------------------------------------------------------------------------------------------")
            return
        # Chattrogram
        if location == "Chattrogram" and destination == "Dhaka":
            print("Happy Journey")
            return
        if location == "Chattrogram" and destination == "Barisal":
            print("Happy Journey")
            return
        if location == "Chattrogram" and destination == "Khulna":
            print("Happy Journey")
            return
        if location == "Chattrogram" and destination == "Mymensingh":
            print("Happy Journey")
            return
        if location == "Chattrogram" and destination == "Rajshahi":
            print("Happy Journey")
            return
        if location == "Chattrogram" and destination == "Rangpur":
            print("Happy Journey")
            return

        if location == "Chattrogram" and destination == "Sylhet":
            print("Happy Journey")
            return
        if location == "Chattrogram" and destination == "Cox's Bazar":
            print("Happy Journey")
            return
        if location == "Chattrogram" and destination == "Saint Martin":
            print("Happy Journey")
            return

        # Khulna
        if location == "Khulna" and destination == "Dhaka":
            print("Happy Journey")
            return
        if location == "Khulna" and destination == "Barisal":
            print("Happy Journey")
            return
        if location == "Khulna" and destination == "Chattrogram":
            print("Happy Journey")
            return
        if location == "Khulna" and destination == "Mymensingh":
            print("Happy Journey")
            return
        if location == "Khulna" and destination == "Rajshahi":
            print("Happy Journey")
            return
        if location == "Khulna" and destination == "Rangpur":
            print("Happy Journey")
            return
        if location == "Khulna" and destination == "Sylhet":
            print("Happy Journey")
            return
        if location == "Khulna" and destination == "Cox's Bazar":
            print("Happy Journey")
            return
        if location == "Khulna" and destination == "Saint Martin":
            print("Happy Journey")
            return

        # Mymensingh
        if location == "Mymensingh" and destination == "Dhaka":
            print("Happy Journey")
            return
        if location == "Mymensingh" and destination == "Barisal":
            print("Happy Journey")
            return
        if location == "Mymensingh" and destination == "Chattrogram":
            print("Happy Journey")
            return
        if location == "Mymensingh" and destination == "Khulna":
            print("Happy Journey")
            return
        if location == "Mymensingh" and destination == "Rajshahi":
            print("Happy Journey")
            return
        if location == "Mymensingh" and destination == "Rangpur":
            print("Happy Journey")
            return
        if location == "Mymensingh" and destination == "Sylhet":
            print("Happy Journey")
            return
        if location == "Mymensingh" and destination == "Cox's Bazar":
            print("Happy Journey")
            return
        if location == "Mymensingh" and destination == "Saint Martin":
            print("Happy Journey")
            return

        # Rajshahi
        if location == "Rajshahi" and destination == "Dhaka":
            print("Happy Journey")
            return
        if location == "Rajshahi" and destination == "Barisal":
            print("Happy Journey")
            return
        if location == "Rajshahi" and destination == "Chattrogram":
            print("Happy Journey")
            return
        if location == "Rajshahi" and destination == "Khulna":
            print("Happy Journey")
            return
        if location == "Rajshahi" and destination == "Mymensingh":
            print("Happy Journey")
            return
        if location == "Rajshahi" and destination == "Rangpur":
            print("Happy Journey")
            return
        if location == "Rajshahi" and destination == "Sylhet":
            print("Happy Journey")
            return
        if location == "Rajshahi" and destination == "Cox's Bazar":
            print("Happy Journey")
            return
        if location == "Rajshahi" and destination == "Saint Martin":
            print("Happy Journey")
            return

        # Rangpur
        if location == "Rangpur" and destination == "Dhaka":
            print("Happy Journey")
            return
        if location == "Rangpur" and destination == "Barisal":
            print("Happy Journey")
            return
        if location == "Rangpur" and destination == "Chattrogram":
            print("Happy Journey")
            return
        if location == "Rangpur" and destination == "Khulna":
            print("Happy Journey")
            return
        if location == "Rangpur" and destination == "Mymensingh":
            print("Happy Journey")
            return
        if location == "Rangpur" and destination == "Rajshahi":
            print("Happy Journey")
            return
        if location == "Rangpur" and destination == "Sylhet":
            print("Happy Journey")
            return
        if location == "Rangpur" and destination == "Cox's Bazar":
            print("Happy Journey")
            return
        if location == "Rangpur" and destination == "Saint Martin":
            print("Happy Journey")
            return

        # Sylhet
        if location == "Sylhet" and destination == "Dhaka":
            print("Happy Journey")
            return
        if location == "Sylhet" and destination == "Barisal":
            print("Happy Journey")
            return
        if location == "Sylhet" and destination == "Chattrogram":
            print("Happy Journey")
            return
        if location == "Sylhet" and destination == "Khulna":
            print("Happy Journey")
            return
        if location == "Sylhet" and destination == "Mymensingh":
            print("Happy Journey")
            return
        if location == "Sylhet" and destination == "Rajshahi":
            print("Happy Journey")
            return
        if location == "Sylhet" and destination == "Rangpur":
            print("Happy Journey")
            return
        if location == "Sylhet" and destination == "Cox's Bazar":
            print("Happy Journey")
            return
        if location == "Sylhet" and destination == "Saint Martin":
            print("Happy Journey")
            return

        # Cox's Bazar
        if location == "Cox's Bazar" and destination == "Dhaka":
            print("Happy Journey")
            return
        if location == "Cox's Bazar" and destination == "Barisal":
            print("Happy Journey")
            return
        if location == "Cox's Bazar" and destination == "Chattrogram":
            print("Happy Journey")
            return
        if location == "Cox's Bazar" and destination == "Khulna":
            print("Happy Journey")
            return
        if location == "Cox's Bazar" and destination == "Mymensingh":
            print("Happy Journey")
            return
        if location == "Cox's Bazar" and destination == "Rajshahi":
            print("Happy Journey")
            return
        if location == "Cox's Bazar" and destination == "Rangpur":
            print("Happy Journey")
            return
        if location == "Cox's Bazar" and destination == "Sylhet":
            print("Happy Journey")
            return
        if location == "Cox's Bazar" and destination == "Saint Martin":
            print("Happy Journey")
            return

        # Saint Martin
        if location == "Saint Martin" and destination == "Dhaka":
            print("Happy Journey")
            return
        if location == "Saint Martin" and destination == "Barisal":
            print("Happy Journey")
            return
        if location == "Saint Martin" and destination == "Chattrogram":
            print("Happy Journey")
            return
        if location == "Saint Martin" and destination == "Khulna":
            print("Happy Journey")
            return
        if location == "Saint Martin" and destination == "Mymensingh":
            print("Happy Journey")
            return
        if location == "Saint Martin" and destination == "Rajshahi":
            print("Happy Journey")
            return
        if location == "Saint Martin" and destination == "Rangpur":
            print("Happy Journey")
            return
        if location == "Saint Martin" and destination == "Sylhet":
            print("Happy Journey")
            return
        if location == "Saint Martin" and destination == "Cox's Bazar":
            print("Happy Journey")
            return



    def travel_page(self):
        print("-------------------")
        print("1.Barisal          |")
        print("2.Chattrogram      |")
        print("3.Dhaka            |")
        print("4.Khulna           |")
        print("5.Mymensingh       |")
        print("6.Rajshahi         |")
        print("7.Rangpur          |")
        print("8.Sylhet           |")
        print("9.Cox's Bazar      |")
        print("10.Saint Martin    |")
        print("-------------------")

        location = int(input("PLEASE CHOOSE YOUR LOCATION: "))
        destination = int(input("PLEASE CHOOSE YOUR DESTINATION: "))
        print("..................................................")
        print(f"Your Location: {travel.get(location,'Location not found')}")
        print(f"Your Destination: {travel.get(destination,'Destination not found')}")
        print("..................................................")
        self.travel_info(travel.get(location), travel.get(destination))
        print("1.DONE")
        print("2.GO BACK")
        o = input("Please Select An Option:")
        if o == '1':
            print("WISHING YOU A SAFE JOURNEY!!!")
            print("...............................")
            print("Press ENTER To Continue...")
            a = input()
            os.system('cls')
            self.firstPage()
        elif o == '2':
            os.system('cls')
            self.travel_page()
        else:
            print("Wrong Option Selected!!!")
            print("Press ENTER To Continue...")
            a = input()
            os.system('cls')
            self.firstPage()

    def destination_information_page(self):
        print("-------------------")
        print("1.Barisal          |")
        print("2.Chattrogram      |")
        print("3.Dhaka            |")
        print("4.Khulna           |")
        print("5.Mymensingh       |")
        print("6.Rajshahi         |")
        print("7.Rangpur          |")
        print("8.Sylhet           |")
        print("9.Cox's Bazar      |")
        print("10.Saint Martin    |")
        print("-------------------")

        destination = int(input("PLEASE CHOOSE YOUR DESTINATION: "))
        print("..............................................")
        print(f"You have chosen: {travel.get(destination,'Location not found')}")
        if destination > 10:
            print("Try Again!!")
            print("Press ENTER To Continue...")
            a = input()
            os.system('cls')
            self.destination_information_page()

        print("..............................................")
        print(f"Here's What You Need to Know about '{travel[destination]}':")
        print(" ------------------------------------------------------------")
        print("|            Information will be provided here.              |")
        print(" ------------------------------------------------------------")
        print("1.DONE")
        print("2.GO BACK")
        o = input("Please Select An Option:")
        if o == '1':
            print("Press ENTER To Continue...")
            a = input()
            os.system('cls')
            self.firstPage()
        elif o == '2':
            os.system('cls')
            self.destination_information_page()
        else:
            print("Wrong Option Selected!!!")
            print("Press ENTER To Continue...")
            a = input()
            os.system('cls')
            self.firstPage()

    def display(self):
        print(f"Name : {self.name}")
        print(f"Username : {self.username}")
        print(f"E-mail : {self.email}")
        print(f"Phone Number : {self.email}")
        print(f"Date of Birth : {self.dob}")
        print(f"Address : {self.dob}")
        print(f"Favourite Places {self.fav3}")


    def firstPage(self):
        print("Hello traveller!!! What do you want to do?")
        print("----------------------------")
        print("1.TRAVEL                    |")
        print("2.DESTINATION INFORMATION   |")
        print("3.PROFILE INFORMATION       |")
        print("4.BACK TO LOGIN PAGE        |")
        print("----------------------------")
        input_fp = input("SELECT YOUR OPTION: ")
        if input_fp == "1":
            os.system('cls')
            self.travel_page()
        elif input_fp == "2":

                os.system('cls')
                self.destination_information_page()
        elif input_fp == "3":
            print("")
            print(" ---------------------------")
            print("|****PROFILE INFORMATION****|")
            print(" --------------------------")
            print(f"Name : {self.name}")
            print(f"Username : {self.username}")
            print(f"E-mail : {self.email}")
            print(f"Phone Number : {self.email}")
            print(f"Date of Birth : {self.dob}")
            print(f"Address : {self.dob}")
            print(f"Favourite Places {self.fav3}")
            print(".........................................")
            ch = input("PRESS 'B' TO GO BACK : ")
            if ch.upper() == 'B':
                os.system('cls')
                self.firstPage()
        elif input_fp == "4":
            os.system('cls')
            loginPage()



class Customer(Information):
    def __init__(self, name, username, password, email, phonenumber, dob, address, fav):
        super().__init__(name, username, password, email, phonenumber, dob, address, fav)




def loginPage():
    if (mycursor.rowcount != 0):
        mycursor.execute("SELECT * FROM customers")
        myresult = mycursor.fetchall()
        for x in myresult:
            i = 0
            for y in x:
                if i == 0:
                    name = y
                    i = i + 1
                elif i == 1:
                    username = y
                    i = i + 1
                elif i == 2:
                    password = y
                    i = i + 1
                elif i == 3:
                    email = y
                    i = i + 1
                elif i == 4:
                    phonenumber = y
                    i = i + 1
                elif i == 5:
                    dob = y
                    i = i + 1
                elif i == 6:
                    address = y
                    i = i + 1
                elif i == 7:
                    str1 = str(y)
                    fav = list(str1.split())
            list1.append(Customer(name, username, password, email, phonenumber, dob, address,fav))

    print("----------------------------------------")
    print("| HEY THERE!!! WELCOME TO CHOLO-JAI 😍  |")
    print("----------------------------------------")
    print("1.Are you an USER???")
    print("2.Or do you want to start your journey with us???")
    print("3.Admin Panel")
    print("4.Exit")

    input_1 = input("Please select an option: ")
    if input_1 == '1':
        username = input("Enter Username : ")
        password = input("Enter Password : ")
        bool = False

        for customer in list1:
            if customer.username == username and customer.password == password:
                print("|------------------|")
                print("| Login Successful |")
                print("|------------------|")
                print("Press ENTER To Continue...")
                a = input()
                os.system('cls')
                bool = True
                customer.firstPage()

        if not bool:
            print("Invalid Username Or Password!!!")
            print("Press ENTER To Continue...")
            a = input()
            os.system('cls')
            loginPage()




    elif input_1 == '2':
        name = input("Enter Your Name : ")
        username = input("Enter Username : ")
        password = input("Enter Password : ")
        email = input("Enter Email : ")
        phonenumber = input("Enter Your Phone Number : ")
        dob = input("Date Of Birth: ")
        address = input("Address : ")
        print("FAVOURITE 3 PLACES:")
        fav = []
        print("..................")
        for i in range(0, 3):
            fav.append((input()))
            print("..................")
        Str = ' '.join([str(elem) for elem in fav])
       # list1.append(Customer(name, username, password, email, phonenumber, dob, address,fav))

        sqL="INSERT INTO customers (Name, Username,Password,Email,  Phonenumber,Dob, Address, FavoritePlaces) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (name, username, password, email, phonenumber, dob, address, Str)
        mycursor.execute(sqL, val)
        mydb.commit()


        print("......................................")
        print(".REGISTRATION COMPLETE!!!THANK YOU!!!.")
        print("......................................")
        print("Press ENTER To Continue...")
        a = input()
        os.system('cls')
        loginPage()


    elif input_1 == '3':
        print(f"Are you:-")
        print(f"1. {admin1.name}")
        print(f"2. {admin2.name}")
        name = input("Please Select An Option: ")

        if name == "1":
            password = input("Give Your Password: ")
            if admin1.password == password:
                print("|------------------|")
                print("| Login Successful |")
                print("|------------------|")
                print("Press ENTER To Continue...")
                a = input()
                os.system('cls')
                adminpage(admin1.name)

            else:
                print("Invalid Password!!")
                print("Press ENTER To Continue...")
                a = input()
                os.system('cls')
                loginPage()

        elif name == "2":
            password = input("Give Your Password: ")
            if admin2.password == password:
                print("|------------------|")
                print("| Login Successful |")
                print("|------------------|")
                print("Press ENTER To Continue...")
                a = input()
                os.system('cls')
                adminpage(admin2.name)
            else:
                print("Invalid Password!!")
                print("Press ENTER To Continue...")
                a = input()
                os.system('cls')
                loginPage()

        else:
            print("Wrong Option Selected!!!")
            print("Press ENTER To Continue...")
            a = input()
            os.system('cls')
            loginPage()
    elif input_1 == '4':
        exit()

    else:
        print("Wrong Option Selected!!!")
        print("Press ENTER To Continue...")
        a = input()
        os.system('cls')
        loginPage()

loginPage()
