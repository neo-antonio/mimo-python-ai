italian_food = [
    "pasta bolognese", 
    "pepperoni pizza", 
    "margherita pizza",
    "lasagna"
]

indian_food = [
    "curry",
    "chutney",
    "samosa",
    "naan"
]

def find_meal(food_name, menu):
    return food_name if food_name in menu else None

def select_meal(food_name, food_type):
    if food_type == "italian":
        return find_meal(food_name, italian_food)
    if food_type == "indian":
        return find_meal(food_name, indian_food)
    else:
        return None

def display_available_meals(food_type):
    if food_type == "italian":
        print("\nAvailable Italian Meals:\n")
        for food in italian_food:
            print(food)
        return True
    elif food_type == "indian":
        print("\nAvailable Indian Meals:\n")
        for food in indian_food:


            print(food)
        return True
    else:
        print("\nInvalid Food Type")
        return False

def create_summary(food_name, amount, food_type):
    order = select_meal(food_name, food_type)
    if order:
        return f"\nYou successfully ordered {amount} of {food_name}.\n Please wait for your order!"
    else:
        return f"\nMeal not found!"

print("Welcome to the Food Order System!")
print('\nPlease select "italian" or "indian" to display the menu in that food group.')

menu_input = input("Enter the type of menu: ")

if display_available_meals(menu_input):
    food_name_input = input("\nPlease enter the EXACT name and spacing of the food you'd like to order: ")
    amount_input = int(input("\nHow many would you liked to order: "))
    result = create_summary(food_name_input, amount_input, menu_input)
    print(result)
