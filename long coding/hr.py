class User:
    def __init__(self, user_id, name, email, mobile, aadhar, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.mobile = mobile
        self.aadhar = aadhar
        self.booking_history = []

    def view_details(self):
        print(f"user_id: {self.user_id}")
        print(f"name: {self.name}")
        print(f"email: {self.email}")
        print(f"mobile: {self.mobile}")
        print(f"aadhar: {self.aadhar}")
class Owner(User):
    def __init__(self, owner_id, user_id, name, email, mobile, aadhar, password):
        super().__init__(user_id, name, email, mobile, aadhar, password)
        self.owner_id = owner_id


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


class HouseRentalApp:
    def __init__(self):
        self.users = []
        self.owners = []
        self.houses = []
        self.bookings = []
        self.admin = Admin("admin", "admin")
        #adding houses hardcoded
        self.houses.append(House(1, "T Nagar Colony", "Chennai", "1000", "Apartment", 5000, 1))
        self.houses.append(House(2, "Tambaram Colony", "Chennai", "1500", "Villa", 10000, 2))

        #adding owners hardcoded
        self.owners.append(Owner(1, 1, "owner1", "own1@gmail.com", "9876543210", "1234567890", "password1"))
        self.owners.append(Owner(2, 2, "owner2", "own2@gmail.com", "9876543211", "0987654321", "password2"))

    def run(self):
        while True:
            print("Welcome to the House Rental App")
            print("1. Register")
            print("2. Login")
            print("3. Owner Login")
            print("4. Admin Login")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.owner_login()
            elif choice == "4":
                self.admin_login()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

        print("Thank you for using the House Rental Booking App!")

    def register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        mobile = input("Enter your mobile number: ")
        aadhaar = input("Enter your Aadhar number: ")
        user_id = len(self.users) + 1
        new_user = User(user_id, name, email, mobile, aadhaar, password)
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

    def owner_login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for owner in self.owners:
            if owner.email == email and owner.password == password:
                print("Owner login successful!")
                self.owner_menu(owner)
                break
        else:
            print("Invalid email or password. Please try again.")
    def admin_login(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        if self.admin.login(username, password):
            print("Admin login successful!")
            self.admin_menu()
        else:
            print("Invalid admin username or password.")
    def admin_menu(self):
        while True:
            print("Admin Menu")
            print("1. View Booking History")
            print("2. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_booking_history()
            elif choice == "2":
                break
            else:
                print("Invalid choice. Please try again.")

    def user_menu(self, user):
        while True:
            print("User Menu")
            print("1. Search Houses")
            print("2. Book House")
            print("3. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.search_houses()
            elif choice == "2":
                self.book_house(user)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def owner_menu(self, owner):
        while True:
            print("Owner Menu")
            print("1. Add House")
            print("2. View Owner Details")
            print("3. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_house(owner)
            elif choice == "2":
                owner.view_details()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_house(self, owner):
        locality = input("Enter the location: ")
        city = input("Enter the city: ")
        sqr_feet = input("Enter square feet: ")
        type_name = input("Enter type of house: ")
        rent = input("Enter rent per month: ")
        house_id = len(self.houses) + 1
        new_house = House(house_id, locality, city, sqr_feet, type_name, rent, owner.owner_id)
        self.houses.append(new_house)
        print("House added successfully!")

    def search_houses(self):
        keyword = input("Enter a keyword to search houses: ")
        found_houses = []

        for house in self.houses:
            if keyword.lower() in house.city.lower() or keyword.lower() in house.locality.lower():
                found_houses.append(house)

        if found_houses:
            print("Search Results:")
            for house in found_houses:
                house.view_details()
                print()
        else:
            print("No houses found.")

    def book_house(self, user):
        house_id = int(input("Enter the house ID: "))
        owner_id = int(input("Enter the owner ID: "))
        check_in_date = input("Enter the date of check-in: ")
        payment_method = input("Choose the payment option (1. Card, 2. UPI, 3. Cash): ")

        booking_id = len(self.bookings) + 1
        new_booking = Booking(booking_id, house_id, user.user_id, owner_id, check_in_date, payment_method)
        self.bookings.append(new_booking)
        user.booking_history.append(new_booking)

        print("Booking successful!")
        print("Thank you for booking a house!")
    
    def view_booking_history(self):
        if self.bookings:
            print("Booking History:")
            for booking in self.bookings:
                booking.view_details(self.houses, self.users, self.owners)
                print()
        else:
            print("No booking history found.")

app = HouseRentalApp()
app.run()
