from abc import ABC, abstractmethod
from datetime import datetime
from collections import deque
from enum import Enum


class Entity(ABC):
    def __init__(self, entity_id):
        self.entity_id = entity_id

    @abstractmethod
    def display_details(self):
        pass

class User(Entity):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id)
        self.name = name
        self.email = email
        self.password = password
        self.booking_history = []

    def display_details(self):
        print(f"User ID: {self.entity_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

class Movie(Entity):
    def __init__(self, movie_id, title, genre, director):
        super().__init__(movie_id)
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

class Review(Entity):
    def __init__(self, review_id, user_id, comment, rating):
        super().__init__(review_id)
        self.user_id = user_id
        self.comment = comment
        self.rating = rating

    def display_details(self):
        print(f"Review ID: {self.entity_id}")
        print(f"User ID: {self.user_id}")
        print(f"Comment: {self.comment}")
        print(f"Rating: {self.rating}")

class Theater(Entity):
    def __init__(self, theater_id, name, location):
        super().__init__(theater_id)
        self.name = name
        self.location = location
        self.showtimes = []

    def display_details(self):
        print(f"Theater ID: {self.entity_id}")
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")

class Showtime(Entity):
    def __init__(self, showtime_id, movie_id, start_time, end_time):
        super().__init__(showtime_id)
        self.movie_id = movie_id
        self.start_time = start_time
        self.end_time = end_time
        self.available_seats = deque()

    def display_details(self):
        print(f"Showtime ID: {self.entity_id}")
        print(f"Movie ID: {self.movie_id}")
        print(f"Start Time: {self.start_time}")
        print(f"End Time: {self.end_time}")

class Seat(Entity):
    def __init__(self, seat_id, theater_id, showtime_id, seat_number):
        super().__init__(seat_id)
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
    def __init__(self, booking_id, user_id, showtime_id, booked_seats, booking_date, payment_option):
        super().__init__(booking_id)
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
    CARD = "Card"
    UPI = "UPI"
    CASH_ON_DELIVERY = "Cash on Delivery"

class MobileTicketBookingApp:
    def __init__(self):
        self.users = []
        self.movies = []
        self.theaters = []
        self.bookings = []
        self.reviews = []

    def run(self):
        is_running = True
        while is_running:
            print("Welcome to the Mobile Ticket Booking App")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                print("Registration")
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                user_id = len(self.users) + 1
                new_user = User(user_id, name, email, password)
                self.users.append(new_user)
                print("Registration successful!")

            elif choice == "2":
                print("Login")
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                logged_in_user = self.login_user(email, password)
                if logged_in_user:
                    print("Login successful!")
                    self.show_movie_list()
                    self.book_movie(logged_in_user)
                else:
                    print("Invalid email or password. Please try again.")

            elif choice == "3":
                is_running = False
            else:
                print("Invalid choice. Please try again.")

        print("Thank you for using the Mobile Ticket Booking App!")

    def login_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None

    def show_movie_list(self):
        print("Movie List:")
        for movie in self.movies:
            movie.display_details()
            print()

    def book_movie(self, user):
        movie_id = input("Enter the ID of the movie you want to book: ")
        showtime_id = input("Enter the ID of the showtime you want to book: ")
        seat_numbers = input("Enter the seat numbers (separated by commas) you want to book: ")
        seat_numbers = seat_numbers.split(",")

        selected_showtime = None
        for theater in self.theaters:
            for showtime in theater.showtimes:
                if showtime.entity_id == showtime_id and showtime.movie_id == movie_id:
                    selected_showtime = showtime
                    break

        if selected_showtime:
            selected_seats = []
            for seat_number in seat_numbers:
                for seat in selected_showtime.available_seats:
                    if seat.seat_number == seat_number and seat.is_available:
                        seat.is_available = False
                        selected_seats.append(seat)
                        break

            if selected_seats:
                booking_id = len(self.bookings) + 1
                booking_date = datetime.now()
                payment_option = PaymentOption.CARD
                new_booking = Booking(booking_id, user.entity_id, selected_showtime.entity_id, selected_seats, booking_date, payment_option)
                self.bookings.append(new_booking)
                user.booking_history.append(new_booking)
                print("Booking successful!")
            else:
                print("Seats are not available.")
        else:
            print("Invalid movie or showtime ID.")

    # Add additional functions as per your requirements

app = MobileTicketBookingApp()
app.run()
