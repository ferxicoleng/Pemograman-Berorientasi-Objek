class User :
    def __init__(self,first_name,last_name,date_of_birth,address):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.login_attempts = 0
    def describe_user(self):
        print(f"Name : {self.first_name} {self.last_name}")
        print(f"Date of birth : {self.date_of_birth}")
        print(f"Address : {self.address}")
    def greet_user(self):
        print(f"Hello, {self.first_name} welcome.")
    def increment_login_attempts(self):
        self.login_attempts +=1
    def reset_login_attempts(self):
        self.login_attempts =0

my_name = User('Muhammad','Nabil','12-01-2000','Garuda street Number 3')
my_name.describe_user()
my_name.greet_user()
my_name.increment_login_attempts()
my_name.increment_login_attempts()
my_name.increment_login_attempts()
print(f"number of login attempts: {my_name.login_attempts}")
my_name.reset_login_attempts()
print(f"number of login attempts: {my_name.login_attempts}")
print( )

b_name = User('Budi','Setiawan','12-01-2004','Nila street Number 4')
b_name.describe_user()
b_name.greet_user()
b_name.increment_login_attempts()
b_name.increment_login_attempts()
b_name.increment_login_attempts()
print(f"number of login attempts: {b_name.login_attempts}")
b_name.reset_login_attempts()
print(f"number of login attempts: {b_name.login_attempts}")
print( )

a_name = User('Anto','Kurnia','12-01-2000','Garuda street Number 3')
a_name.describe_user()
a_name.greet_user()
a_name.increment_login_attempts()
a_name.increment_login_attempts()
a_name.increment_login_attempts()
print(f"number of login attempts: {a_name.login_attempts}")
a_name.reset_login_attempts()
print(f"number of login attempts: {a_name.login_attempts}")
print( )

c_name = User('Imam','Shaleh','12-01-2000','Garuda street Number 3')
c_name.describe_user()
c_name.greet_user()
c_name.increment_login_attempts()
c_name.increment_login_attempts()
c_name.increment_login_attempts()
print(f"number of login attempts: {c_name.login_attempts}")
c_name.reset_login_attempts()
print(f"number of login attempts: {c_name.login_attempts}")
print( )

