from abc import ABC, abstractmethod
from datetime import datetime
from collections import deque
from enum import Enum

class Entity:
    def __init__(self, entity_id):
        self.entity_id = entity_id

class User(Entity):
    def __init__(self, entity_id, name, email, password):
        super().__init__(entity_id)
        self.name = name
        self.email = email
        self.password = password
        self.booking_history = []

class Movie(Entity):
    def __init__(self, entity_id, title, genre, director):
        super().__init__(entity_id)
        self.title = title
        self.genre = genre
        self.director = director
        self.rating = 0.0
        self.reviews = []

    def display_details(self):
        print(f"Movie ID: {self.entity_id}")
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Director: {self.director}")
        print(f"Rating: {self.rating}")

class Theater(Entity):
    def __init__(self, entity_id, name, location):
        super().__init__(entity_id)
        self.name = name
        self.location = location
        self.showtimes = deque()

    def display_details(self):
        print(f"Theater ID: {self.entity_id}")
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")

class Showtime(Entity):
    def __init__(self, entity_id, movie_id, start_time, end_time):
        super().__init__(entity_id)
        self.movie_id = movie_id
        self.start_time = start_time
        self.end_time = end_time
        self.available_seats = []

    def display_details(self):
        print(f"Showtime ID: {self.entity_id}")
        print(f"Movie ID: {self.movie_id}")
        print(f"Start Time: {self.start_time}")
        print(f"End Time: {self.end_time}")

class Seat(Entity):
    def __init__(self, entity_id, theater_id, showtime_id, seat_number):
        super().__init__(entity_id)
        self.theater_id = theater_id
        self.showtime_id = showtime_id
        self.seat_number = seat_number
        self.is_available = True

    def display_details(self):
        print(f"Seat ID: {self.entity_id}")
        print(f"Theater ID: {self.theater_id}")
        print(f"Showtime ID: {self.showtime_id}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Is Available: {self.is_available}")

class Booking(Entity):
    def __init__(self, entity_id, user_id, showtime_id, booked_seats, booking_date, payment_option):
        super().__init__(entity_id)
        self.user_id = user_id
        self.showtime_id = showtime_id
        self.booked_seats = booked_seats
        self.booking_date = booking_date
        self.payment_option = payment_option

    def display_details(self):
        print(f"Booking ID: {self.entity_id}")
        print(f"User ID: {self.user_id}")
        print(f"Showtime ID: {self.showtime_id}")
        print(f"Booked Seats:")
        for seat in self.booked_seats:
            seat.display_details()
        print(f"Booking Date: {self.booking_date}")
        print(f"Payment Option: {self.payment_option}")

class PaymentOption(Enum):
    CARD = 1
    UPI = 2
    CASH_ON_DELIVERY = 3

class MobileTicketBookingApp:
    def __init__(self):
        self.users = []
        self.movies = []
        self.theaters = []
        self.bookings = []
        self.admin = Admin("admin", "admin")

    def run(self):
        while True:
            print("Welcome to the Mobile Ticket Booking App")
            print("1. Register")
            print("2. Login")
            print("3. Admin Login")
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

        print("Thank you for using the Mobile Ticket Booking App!")

    def register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user_id = len(self.users) + 1
        new_user = User(user_id, name, email, password)
        self.users.append(new_user)
        print("Registration successful!")

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
            print("1. Search Movies")
            print("2. Book Movie")
            print("3. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.search_movies()
            elif choice == "2":
                self.book_movie(user)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def admin_menu(self):
        while True:
            print("Admin Menu")
            print("1. Add Movie")
            print("2. Add Theater")
            print("3. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_movie()
            elif choice == "2":
                self.add_theater()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_movie(self):
        title = input("Enter the movie title: ")
        genre = input("Enter the movie genre: ")
        director = input("Enter the movie director: ")
        movie_id = len(self.movies) + 1
        new_movie = Movie(movie_id, title, genre, director)
        self.movies.append(new_movie)
        print("Movie added successfully!")

    def add_theater(self):
        name = input("Enter the theater name: ")
        location = input("Enter the theater location: ")
        theater_id = len(self.theaters) + 1
        new_theater = Theater(theater_id, name, location)
        self.theaters.append(new_theater)
        print("Theater added successfully!")

    def search_movies(self):
        keyword = input("Enter a keyword to search movies: ")
        found_movies = []

        for movie in self.movies:
            if keyword.lower() in movie.title.lower() or keyword.lower() in movie.genre.lower():
                found_movies.append(movie)

        if found_movies:
            print("Search Results:")
            for movie in found_movies:
                movie.display_details()
                print()
        else:
            print("No movies found.")

    def book_movie(self, user):
        movie_id = int(input("Enter the movie ID: "))
        showtime_id = int(input("Enter the showtime ID: "))
        num_seats = int(input("Enter the number of seats to book: "))

        movie = self.get_movie_by_id(movie_id)
        showtime = self.get_showtime_by_id(showtime_id)

        if movie and showtime:
            available_seats = self.get_available_seats(showtime, num_seats)

            if available_seats:
                booked_seats = []
                for seat in available_seats:
                    seat.is_available = False
                    booked_seats.append(seat)

                booking_id = len(self.bookings) + 1
                booking_date = datetime.now()
                payment_option = self.select_payment_option()

                new_booking = Booking(booking_id, user.entity_id, showtime.entity_id, booked_seats, booking_date, payment_option)
                self.bookings.append(new_booking)

                print("Booking successful!")
                print("Booking Details:")
                new_booking.display_details()
            else:
                print("No available seats for the selected showtime.")
        else:
            print("Invalid movie ID or showtime ID.")

    def get_movie_by_id(self, movie_id):
        for movie in self.movies:
            if movie.entity_id == movie_id:
                return movie
        return None

    def get_showtime_by_id(self, showtime_id):
        for theater in self.theaters:
            for showtime in theater.showtimes:
                if showtime.entity_id == showtime_id:
                    return showtime
        return None

    def get_available_seats(self, showtime, num_seats):
        available_seats = []
        for seat in showtime.available_seats:
            if seat.is_available:
                available_seats.append(seat)
                if len(available_seats) == num_seats:
                    break
        return available_seats

    def select_payment_option(self):
        print("Select a payment option:")
        print("1. Card")
        print("2. UPI")
        print("3. Cash on Delivery")

        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                return PaymentOption.CARD
            elif choice == "2":
                return PaymentOption.UPI
            elif choice == "3":
                return PaymentOption.CASH_ON_DELIVERY
            else:
                print("Invalid choice. Please try again.")

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password

app = MobileTicketBookingApp()
app.run()
