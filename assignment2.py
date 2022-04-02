class User():
    first_name = ''
    last_name = ''
    email_address = ''
    phone_number = ''
    gender = ''
    allergies = ''
    user_type = ''

    def __init__(self, first_name, last_name, email_address, phone_number, gender, allergies, user_type):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.gender = gender
        self.allergies = allergies
        self.user_type = user_type


# A meal item class
class MealItem():
    meal_name = ''
    meal_description = ''
    serving_sizes = ''
    meal_image = ''

    def __init__(self, meal_name, meal_description, serving_sizes, meal_image):
        self.meal_name = meal_name
        self.meal_description = meal_description
        self.serving_sizes = serving_sizes
        self.meal_image = meal_image


# An order class
class Order():
    order_details = ''
    quantity = ''

    def __init__(self, order_details, quantity):
        self.order_details = order_details
        self.quantity = quantity


# Instantiate a user as an EIT
user_as_eit = User('Somto', 'Chike-Nwaka', 'somteenwaka@gmail.com',
                   '+2348032418054', 'female', 'none', 'EIT')

# Instantiate a user as an Staff
user_as_staff = User('Grace', 'Boamah', 'Grace@gmail.com',
                     '+2341234567', 'female', 'none', 'STAFF')


# Instantiate a meal object
new_meal = MealItem('Yam and egg sauce with roast beef',
                    'yam and tomato egg sauce with chunks of roast beef', '1 serving', '')


# Instantiate an order object
new_order = Order('Yam and egg sauce with roast beef', 1)


print(user_as_staff.last_name)
print(user_as_eit.first_name)
print(new_meal.meal_name)
print(new_order.quantity)