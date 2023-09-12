class User:
    def __init__(self, user_id, name, email, mobile, aadhaar):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile = mobile
        self.aadhaar = aadhaar

class Owner:
    def __init__(self, owner_id, user_id):
        self.owner_id = owner_id
        self.user_id = user_id

class House:
    def __init__(self, house_id, locality, city, square_feet, house_type, rent, owner_id):
        self.house_id = house_id
        self.locality = locality
        self.city = city
        self.square_feet = square_feet
        self.house_type = house_type
        self.rent = rent
        self.owner_id = owner_id

class Request:
    def __init__(self, request_id, house_id, user_id, status):
        self.request_id = request_id
        self.house_id = house_id
        self.user_id = user_id
        self.status = status

class HouseRentalSystem:
    def __init__(self):
        self.users = {}
        self.owners = {}
        self.houses = {}
        self.requests = {}
        self.next_user_id = 1
        self.next_owner_id = 1
        self.next_house_id = 1
        self.next_request_id = 1

    def register_user(self, name, email, mobile, aadhaar):
        user_id = self.next_user_id
        user = User(user_id, name, email, mobile, aadhaar)
        self.users[user_id] = user
        self.next_user_id += 1
        return user_id

    def create_owner(self, user_id):
        owner_id = self.next_owner_id
        owner = Owner(owner_id, user_id)
        self.owners[owner_id] = owner
        self.next_owner_id += 1
        return owner_id

    def add_house(self, locality, city, square_feet, house_type, rent, owner_id):
        house_id = self.next_house_id
        house = House(house_id, locality, city, square_feet, house_type, rent, owner_id)
        self.houses[house_id] = house
        self.next_house_id += 1
        return house_id

    def create_request(self, house_id, user_id):
        request_id = self.next_request_id
        request = Request(request_id, house_id, user_id, "Pending")
        self.requests[request_id] = request
        self.next_request_id += 1
        return request_id

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_owner(self, owner_id):
        return self.owners.get(owner_id)

    def get_house(self, house_id):
        return self.houses.get(house_id)

    def get_request(self, request_id):
        return self.requests.get(request_id)

# Example usage
rental_system = HouseRentalSystem()

# Register a user
user_id = rental_system.register_user("Lucifer", "lucifer@gmail.com", "9876543210", "123412341234")

# Create an owner
owner_id = rental_system.create_owner(user_id)

# Add a house
house_id = rental_system.add_house("Kodambakkam", "Chennai", 798, "2BHK", 6000, owner_id)

# Create a request
request_id = rental_system.create_request(house_id, user_id)

# Retrieve user, owner, house, and request information
user = rental_system.get_user(user_id)
owner = rental_system.get_owner(owner_id)
house = rental_system.get_house(house_id)
request = rental_system.get_request(request_id)

# Print information
print("User:", user.name)
print("Owner:", owner.user_id)
print("House:", house.locality, house.city)
print("Request:", request.status)
