class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type} food")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")
    def set_number_served(self,number):
        self.number_served= number
    def increment_number_served(self,addtional):
        self.number_served +=addtional

a_restaurant = Restaurant('Gapyeong','Korean')

print(f"The restaurant name is {a_restaurant.restaurant_name}.")
print(f"This restaurant provides {a_restaurant.cuisine_type} food.")
a_restaurant.describe_restaurant()
a_restaurant.open_restaurant()
print(f"number of customers: {a_restaurant.number_served}")

a_restaurant.number_served=8
print(f"number of customers: {a_restaurant.number_served}")

a_restaurant.set_number_served(16)
print(f"number of customers served: {a_restaurant.number_served}")

a_restaurant.increment_number_served(15)
print(f"number of customers served in a day: {a_restaurant.number_served}")
print( )

b_restaurant = Restaurant('Sushi Mentai','Japanese')

print(f"The restaurant name is {b_restaurant.restaurant_name}.")
print(f"This restaurant provides {b_restaurant.cuisine_type} food.")
b_restaurant.describe_restaurant()
b_restaurant.open_restaurant()
print(f"number of customers: {b_restaurant.number_served}")

b_restaurant.number_served=10
print(f"number of customers: {a_restaurant.number_served}")

b_restaurant.set_number_served(13)
print(f"number of customers served: {b_restaurant.number_served}")

b_restaurant.increment_number_served(15)
print(f"number of customers served in a day: {b_restaurant.number_served}")
print( )

c_restaurant = Restaurant('Sederhana','Padang')

print(f"The restaurant name is {c_restaurant.restaurant_name}.")
print(f"This restaurant provides {c_restaurant.cuisine_type} food.")
c_restaurant.describe_restaurant()
c_restaurant.open_restaurant()
print(f"number of customers: {c_restaurant.number_served}")

c_restaurant.number_served=9
print(f"number of customers: {c_restaurant.number_served}")

c_restaurant.set_number_served(14)
print(f"number of customers served: {c_restaurant.number_served}")

c_restaurant.increment_number_served(15)
print(f"number of customers served in a day: {c_restaurant.number_served}")
print( )