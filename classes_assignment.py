class User():
    firstName = ''
    lastName = ''
    userId = ''
    phoneNumber = ''
    userEmail = ""
    allergies = []
    dietaryRequirements = []
    
class Order():
    orderId = ''
    userId = ''
    menu = ''
    serving_size = ''
    allergens = []
    isTakeOut = False
      
class MenuItem:
    menuItems = []
    dayoftheWeek = ""
    mealType = ""
    mealDescription = ""
    mealImage = ""

class Purchase():
    isTakeOut = True 
    amount = ""
    quantity = ""
    vat = ""
    totalPrice = ""
    

