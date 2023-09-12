class User:
    def __init__(self,user_id,name,email,mobile,aadhar,password):
        self.user_id=user_id
        self.name=name
        self.email=email
        self.password=password
        self.mobile=mobile
        self.aadhar=aadhar
        self.booking_history = []

    """def hardCodedData(self):
        user_data.append(self)
        return user_data"""

    def view_details(self):
        print(f"user_id:{self.user_id}")
        print(f"name:{self.name}")
        print(f"mobile:{self.mobile}")
        print(f"aadhar:{self.aadhar}")
class Owner(User):
    def __init__(self,owner_id,user_id,name,email,mobile,aadhaar,password):
        super().__init__(user_id)


class Booking:
    def __init__(self, booking_id, house_id, user_id, owner_id, check_in_date, payment_method):
        self.booking_id = booking_id
        self.house_id = house_id
        self.user_id = user_id
        self.owner_id = owner_id
        self.check_in_date = check_in_date
        self.payment_method = payment_method

    def view_details(self, houses, users, owners):
        house = next((h for h in houses if h.house_id == self.house_id), None)
        user = next((u for u in users if u.user_id == self.user_id), None)
        owner = next((o for o in owners if o.owner_id == self.owner_id), None)

        if house and user and owner:
            print(f"Booking ID: {self.booking_id}")
            print("House Details:")
            house.view_details()
            print("User Details:")
            user.view_details()
            print("Owner Details:")
            owner.view_details()
            print(f"Check-in Date: {self.check_in_date}")
            print(f"Payment Method: {self.payment_method}")
        else:
            print("Booking details not found.")


class House:
    def __init__(self, house_id, locality, city, sqr_feet, type_name, rent, owner_id):
        self.house_id = house_id
        self.locality = locality
        self.city = city
        self.sqr_feet = sqr_feet
        self.type_name = type_name
        self.rent = rent
        self.owner_id = owner_id

    def view_details(self):
        print(f"house_id: {self.house_id}")
        print(f"locality: {self.locality}")
        print(f"city: {self.city}")
        print(f"square feet: {self.sqr_feet}")
        print(f"type of the house: {self.type_name}")
        print(f"rent of house: {self.rent}")

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password


class house_app:
    def __init__(self):
        self.users=[]
        self.owner_data=[]
        self.houses=[]
        self.bookings=[]
        self.admin = Admin("admin", "admin")

    def run(self):
        while True:
            print("Welcome to the House Rental App")
            print("1. Register")
            print("2. Login")
            print("3. Owner Login")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.admin_login()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

        print("Thank you for using the House Rental Booking App!")


    def register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        mobile = input("Enter your mobile number:")
        aadhaar = input("Entetr your aadhar number:")
        user_id = len(self.users) + 1
        new_user = User(user_id,name,email,mobile,aadhaar,password)
        self.users.append(new_user)
        print("Registration successful!")
        print()
        

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for user in self.users:
            if user.email == email and user.password == password:
                print("Login successful!")
                self.user_menu(user)
                break
        else:
            print("Invalid email or password. Please try again.")

    def admin_login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if self.admin.login(username, password):
            print("Admin login successful!")
            self.admin_menu()
        else:
            print("Invalid username or password. Please try again.")

    def user_menu(self, user):
        while True:
            print("User Menu")
            print("1. Search Houses")
            print("2. Book House")
            print("3.Booking History")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.search_houses()
            elif choice == "2":
                self.book_house(user)
            elif choice == "3":
                self.view_booking_history()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def admin_menu(self):
        while True:
            print("Admin Menu")
            print("1. Add House")
            print("2. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_house()
            elif choice == "2":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_house(self):
        
        lc = input("Enter the location: ")
        cty = input("Enter the city: ")
        squarefeet= input("enter square feet")
        typ=input("type of house:")
        rent=input("rent per  month :")
        ownid = input("enter owner id")
        houseid = len(self.houses) + 1
        new_house = house(houseid, lc, cty, squarefeet,typ,rent,ownid)
        self.houses.append(new_house)
        print(" house added successfully!")

    def search_houses(self):
        keyword = input("Enter a keyword to search houses: ")
        found_houses = []

        for house in self.houses:
            if keyword.lower() in house.city.lower() or keyword.lower() in house.rent.lower():
                found_houses.append(house)

        if found_houses:
            print("Search Results:")
            for house in found_houses:
                house.view_details()
                print()
        else:
            print("No houses found.")

    def book_house(self, user):
        print("1.contact owner")
        print("2.book house")
        print("3.back")
        Choose=int(input("enter your choice:"))
        if Choose == 1:
            print("owner details")
        if Choose == 2:
            house_id = int(input("Enter the house ID: "))
            owner_id = int(input("Enter the owner ID: "))
            check_in_date= input("Enter the date of checkin: ")
            print("choose the payment option:")
            print("1.card\n 2.upi\n 3.cash")
            choose_pay=int(input("choose the payment option:"))
            if choose_pay == 1:
                print("********CARD*********")
                crd=input("enter card number:")
                nm=input("enter name on card")
                cvv=input("enter cvv")
                print("otp sent")
                print("payment successfull")
                print("*********THANK YOU**********")
            elif choose_pay == 1:
                print("********UPI********")
                upid=input("enter upi id:")
                print("payment successfull")
                print("*********THANK YOU**********")
            elif choose_pay == 3:
                print("*******CASH********")
                print("payment successfull")
                print("*********THANK YOU**********")
            else:
                print("enter valid option")
        else:
            print("choose valid option")
    def view_booking_history(self, user):
        if user.booking_history:
            print("Booking History:")
            for booking in user.booking_history:
                booking.view_details(self.houses, self.users, self.owners)
                print()
        else:
            print("No booking history found.")
        


app = house_app()
app.run()