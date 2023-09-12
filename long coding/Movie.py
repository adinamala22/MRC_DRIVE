from datetime import datetime

class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.booking_history = []

class Movie:
    def __init__(self, movie_id, title, genre, director):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.director = director
        self.rating = 0.0
        self.reviews = []

class Review:
    def __init__(self, review_id, user_id, comment, rating):
        self.review_id = review_id
        self.user_id = user_id
        self.comment = comment
        self.rating = rating

class Theater:
    def __init__(self, theater_id, name, location):
        self.theater_id = theater_id
        self.name = name
        self.location = location
        self.showtimes = []

class Showtime:
    def __init__(self, showtime_id, movie_id, start_time, end_time):
        self.showtime_id = showtime_id
        self.movie_id = movie_id
        self.start_time = start_time
        self.end_time = end_time
        self.available_seats = []

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

class PaymentOption:
    CARD = 'CARD'
    UPI = 'UPI'
    CASH_ON_DELIVERY = 'CASH_ON_DELIVERY'

class MobileTicketBookingApp:
    def __init__(self):
        self.users = []
        self.movies = []
        self.theaters = []
        self.bookings = []

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

                is_logged_in = False
                logged_in_user = None
                for user in self.users:
                    if user.email == email and user.password == password:
                        is_logged_in = True
                        logged_in_user = user
                        break

                if is_logged_in:
                    print("Login successful!")
                else:
                    print("Invalid email or password. Please try again.")

            elif choice == "3":
                is_running = False
            else:
                print("Invalid choice. Please try again.")

        print("Thank you for using the Mobile Ticket Booking App!")

if __name__ == "__main__":
    app = MobileTicketBookingApp()
    app.run()
