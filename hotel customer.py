class HotelCustomer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

class PrimeCustomer(HotelCustomer):
    def __init__(self, name, email, rewards_points):
        super().__init__(name, email)
        self.rewards_points = rewards_points

    def display_details(self):
        super().display_details()
        print(f"Rewards Points: {self.rewards_points}")

class StaffProgram(HotelCustomer):
    def __init__(self, name, email, staff_id):
        super().__init__(name, email)
        self.staff_id = staff_id

    def display_details(self):
        super().display_details()
        print(f"Staff ID: {self.staff_id}")

customer = HotelCustomer("John Doe", "john@example.com")
prime_customer = PrimeCustomer("Jane Doe", "jane@example.com", 1000)
staff_member = StaffProgram("Bob Smith", "bob@example.com", "STAFF123")

print("Customer Details:")
customer.display_details()

print("\nPrime Customer Details:")
prime_customer.display_details()

print("\nStaff Member Details:")
staff_member.display_details()
