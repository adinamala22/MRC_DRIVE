
class User:
    def __init__(self,user_id,email,password):
        self.user_id=user_id
        self.email=email
        self.password=password
    def view(self):
        print(f"email:{self.email}")
class app:
    def __init__(self):
        self.users = []
    def run(self):
        while True:
            print("welcome to the app")
            print("1.register")
            print("1.login")
            choose = int(input("choose the option:"))
            if choose == 1:
                self.register()
            elif choose == 2:
                self.login_user()
    def register(self):
        email=input("enter the email:")
        password = input("enter the password:")
        userid = len(self.users)+1
        new_user= User(userid,email,password)
        self.users.append(new_user)
        print("regustration successful")
    def login_user(self):
        email=input("enter the email :")
        password = input("enter the password:")
        for user in self.users:
            if user.email == email and user.password == password:
                print("login successful")
                self.user_menu()
    def user_menu(self):
        print("welcome user")
        print("1.serach houses")
app = app()
app.run()        






