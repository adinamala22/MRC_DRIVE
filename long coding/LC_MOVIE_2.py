from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum


class PaymentOption(Enum):
    CARD = 1
    UPI = 2
    CASH_ON_DELIVERY = 3


class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password


class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    def add_movie(self, movies, movie):
        movies.append(movie)

    def add_theater(self, theaters, theater):
        theaters.append(theater)


class Movie:
    def __init__(self, movie_id, title, genre, director):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.director = director
        self.rating = 0.0


class Theater:
    def __init__(self, theater_id, name, location):
        self.theater_id = theater_id
        self.name = name
        self.location = location


class Showtime:
    def __init__(self, showtime_id, movie_id, start_time, end_time):
        self.showtime_id = showtime_id
        self.movie_id = movie_id
        self.start_time = start_time
        self.end_time = end_time


class Seat:
    def __init__(self, seat_id, theater_id, showtime_id, seat_number):
        self.seat_id = seat_id
        self.theater_id = theater_id
        self.showtime_id = showtime_id
        self.seat_number = seat_number
        self.is_available = True


class Booking:
    def __init__(self, booking_id, user_id, showtime_id, booked_seats, booking_date, payment_option):
        self.booking_id = booking_id
        self.user_id = user_id
        self.showtime_id = showtime_id
        self.booked_seats = booked_seats
        self.booking_date = booking_date
        self.payment_option = payment_option


class MobileTicketBookingApp:
    def __init__(self):
        self.users = []
        self.movies = []
        self.theaters = []
        self.bookings = []

    def register(self):
        print("Registration")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user_id = len(self.users) + 1
        user = User(user_id, name, email, password)
        self.users.append(user)
        print("Registration successful!")

    def login(self):
        print("Login")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = self.find_user(email, password)
        if user:
            print("Login successful!")
            return user
        else:
            print("Invalid email or password. Please try again.")

    def find_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None

    def search_movies(self):
        keyword = input("Enter a keyword to search movies: ")
        matching_movies = [movie for movie in self.movies if keyword.lower() in movie.title.lower()]
        if matching_movies:
            print("Search Results:")
            for movie in matching_movies:
                print(f"Movie ID: {movie.movie_id}\tTitle: {movie.title}\tGenre: {movie.genre}\tDirector: {movie.director}")
        else:
            print("No movies found.")

    def book_movie(self, user):
        movie_id = input("Enter the movie ID: ")
        showtime_id = input("Enter the showtime ID: ")
        movie = self.get_movie(movie_id)
        showtime = self.get_showtime(showtime_id)
        if movie and showtime:
            print("Booking Details:")
            booking_id = len(self.bookings) + 1
            booking_date = datetime.now()
            payment_option = self.select_payment_option()
            booked_seats = self.select_seats(showtime)
            booking = Booking(booking_id, user.user_id, showtime.showtime_id, booked_seats, booking_date, payment_option)
            self.bookings.append(booking)
            print("Booking successful!")
            self.display_booking_details(booking)
            self.process_payment(payment_option)
        else:
            print("Invalid movie ID or showtime ID.")

    def get_movie(self, movie_id):
        for movie in self.movies:
            if movie.movie_id == movie_id:
                return movie
        return None

    def get_showtime(self, showtime_id):
        for showtime in self.showtimes:
            if showtime.showtime_id == showtime_id:
                return showtime
        return None

    def select_payment_option(self):
        print("Payment Options:")
        for option in PaymentOption:
            print(f"{option.value}. {option.name}")
        while True:
            choice = input("Select a payment option: ")
            if choice.isdigit() and int(choice) in range(1, len(PaymentOption) + 1):
                return PaymentOption(int(choice))
            else:
                print("Invalid choice. Please try again.")

    def select_seats(self, showtime):
        num_seats = int(input("Enter the number of seats to book: "))
        available_seats = [seat for seat in showtime.available_seats if seat.is_available]
        if len(available_seats) < num_seats:
            print("Not enough seats available.")
            return []
        else:
            booked_seats = []
            print("Available Seats:")
            for index, seat in enumerate(available_seats, start=1):
                print(f"{index}. Seat Number: {seat.seat_number}")
            for _ in range(num_seats):
                while True:
                    choice = input("Select a seat number: ")
                    if choice.isdigit() and int(choice) in range(1, len(available_seats) + 1):
                        seat_index = int(choice) - 1
                        seat = available_seats.pop(seat_index)
                        seat.is_available = False
                        booked_seats.append(seat)
                        break
                    else:
                        print("Invalid choice. Please try again.")
            return booked_seats

    def display_booking_details(self, booking):
        print("Booking Details:")
        print(f"Booking ID: {booking.booking_id}")
        print(f"User ID: {booking.user_id}")
        print(f"Showtime ID: {booking.showtime_id}")
        print("Booked Seats:", ", ".join([seat.seat_number for seat in booking.booked_seats]))
        print(f"Booking Date: {booking.booking_date}")
        print("Payment Option:")
        print(booking.payment_option.name)

    def process_payment(self, payment_option):
        print("Processing payment...")
        if payment_option == PaymentOption.CARD:
            print("Payment processed using Card.")
        elif payment_option == PaymentOption.UPI:
            print("Payment processed using UPI.")
        elif payment_option == PaymentOption.CASH_ON_DELIVERY:
            print("Payment processed using Cash on Delivery.")
        print("Payment completed!")


# Main Program
app = MobileTicketBookingApp()

# Add some sample data
admin = Admin(1, "Admin", "admin@example.com", "admin123")
app.users.append(admin)

movie1 = Movie(1, "The Avengers", "Action", "Joss Whedon")
movie2 = Movie(2, "The Shawshank Redemption", "Drama", "Frank Darabont")
app.movies.extend([movie1, movie2])

theater1 = Theater(1, "Cineplex", "New York")
theater2 = Theater(2, "PVR Cinemas", "Los Angeles")
app.theaters.extend([theater1, theater2])

showtime1 = Showtime(1, 1, datetime(2023, 6, 25, 18, 0), datetime(2023, 6, 25, 20, 30))
showtime2 = Showtime(2, 2, datetime(2023, 6, 26, 14, 0), datetime(2023, 6, 26, 16, 30))
app.showtimes.extend([showtime1, showtime2])

seat1 = Seat(1, 1, 1, "A1")
seat2 = Seat(2, 1, 1, "A2")
seat3 = Seat(3, 1, 1, "B1")
seat4 = Seat(4, 1, 1, "B2")
seat5 = Seat(5, 2, 2, "C1")
seat6 = Seat(6, 2, 2, "C2")
seat7 = Seat(7, 2, 2, "D1")
seat8 = Seat(8, 2, 2, "D2")
app.seats.extend([seat1, seat2, seat3, seat4, seat5, seat6, seat7, seat8])

user = None

while True:
    print("Welcome to the Mobile Ticket Booking App")
    print("1. Register")
    print("2. Login")
    print("3. Search Movies")
    print("4. Book Movie")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        app.register()
    elif choice == "2":
        user = app.login()
    elif choice == "3":
        app.search_movies()
    elif choice == "4":
        if user:
            app.book_movie(user)
        else:
            print("Please login first.")
    elif choice == "5":
        print("Thank you for using the Mobile Ticket Booking App!")
        break
    else:
        print("Invalid choice. Please try again.")
