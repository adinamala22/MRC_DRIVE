class User:
    def __init__(self,user_id,user_name,phn_no,address,aadhar_id):
        self.user_id = user_id
        self.user_name = user_name
        self.phn_no = phn_no
        self.address = address
        self.aadhar_id = aadhar_id
        self.users = []
        self.users.append(User(1,'adithya','8179983189','chennai','5165198631651'))

    def view_details(self):
        print(f"user id :{self.user_id}")
        print(f"user name:{self.user_name}")
        print(f"phn number :{self.phn_no}")
        print(f"address:{self.address}")
        print(f"aadhar id :{self.aadhar_id}")
    

    
class Service:
    def __init__(self,service_id):
        self.service_id= service_id
        self.types_of_services = ['cleaning','electrical','appliance repair','plumbers','carpenters']
    def view_details():
        print(f"service id :{self.service_id}")


class Booking:
    def __init__(self,Booking_id,scheduled_date,scheduled_time,booking_status,cancel_book):
        
        self.Booking_id = Booking_id
        self.scheduled_date = scheduled_date
        self.scheduled_time = scheduled_time
        self.cancel_book = cancel_book
    def view_details():
        print(f"booking id :{self.Booking_id}")
        print(f"scheduled_date :{self.scheduled_date}")
        print(f"scheduled time :{self.scheduled_time}")
        print(f"booking status:{self.booking_status}")


class Rating:
    def __init__(self,Rating_id,rating,review):
        self.Rating_id = Rating_id 
        self.rating = rating
        self.review = review    


class House_service_app:
    def __init__(self):
        self.seriveees=Service(1)
        self.services = ['cleaning','electrical','appliance repair','plumbers','carpenters']
        self.booked_list = []
       
    
    def main(self):
        while True:   
            print("welcome to the house services app")
            print("1.user\n2.service provider\n3.exit")
            choose = int(input("choose the option"))
            if choose == 1:
                print("welcome user")
                self.user_menu()
            elif choose == 2:
                print("welcome service provider")
                self.service_provider_menu()
            elif choose == 3:
                break
            else:
                print("enter valid option")    

    def user_menu(self):
        while True:
            print("welcome user")
            print("1.select the services\n2.book the service\n3.view details\n4.logout")
            choose = int(input("choose the option"))
            if choose == 1:
                print(self.services)
            if choose == 2:
                self.book()   
            if choose == 3:
                User.view_details()
            if choose == 4:
                break
    def service_provider_menu(self):
        while True:
            print("welcome service provider")
            print("1.list of booking\n2.accept the service\n3.view booking details\n4.logout")
            choose = int(input("choose the option"))
            if choose == 1:
                print(f"current bookings:{self.booked_list}") 
            elif choose == 2:
                print("are you accepting the order or not")
                print("1.yes\n2.no")
                choose = int(input())
                if choose == 1:
                    print("its accepted")
                elif choose == 2:
                    print("its rejected")
                else:
                    print("invalid")
            elif choose == 3:
                Booking.view_details()
            elif choose == 4:
                break
            else:
                print("invalid option")
        

                    
 
    def book(self):
        Serv = input("enter the serice id : ")
        typ = input("enter the type of service:")
        date = input("enter the scheduled date :")
        time = input("enter the scheduled time :")
        booking_status = 'requested'
        cancel_book = False
        book_id = len(self.booked_list)+1
        booked = Booking(book_id,date,time,booking_status,cancel_book)
        self.booked_list.append(booked)
        print("booking request is send go and check status")
        #booked.view_details()



app = House_service_app()
app.main()
