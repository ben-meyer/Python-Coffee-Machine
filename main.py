import sys

# Define menu options
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Define resources available
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = int()

# The Coffee Machine is ON
On_Off = True


# Define all necessary functions:

# Function: Turn off Coffee Machine by entering "off"
def turn_off(choice):
    if choice == "off":
        sys.exit()
    else:
        pass


# Function: Deliver report of available resources
def deliver_report(choice):
    if choice == "report":
        print("Water: " + str(resources["water"]) + "ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print("Money: $" + str(round(money, 2)))
    else:
        pass


# Function: Check levels
def check_water_level(choice):
    if resources["water"] >= MENU[choice]["ingredients"]["water"]:
        return True
    elif resources["water"] < MENU[choice]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False


def check_coffee_level(choice):
    if resources["coffee"] >= MENU[choice]["ingredients"]["coffee"]:
        return True
    elif resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False


def check_milk_level(choice):
    if resources["milk"] >= MENU[choice]["ingredients"]["milk"]:
        return True
    elif resources["milk"] < MENU[choice]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False


def check_resources_sufficient(choice):
    if choice == "espresso":
        if check_water_level(choice) == True and check_coffee_level(choice) == True:
            return True
        else:
            return False

    elif choice == "latte" or choice == "cappuccino":
        if check_water_level(choice) == True and check_coffee_level(choice) == True and check_milk_level(
                choice) == True:
            return True
        else:
            return False

    else:
        return False


def process_coins():
    """Returns the sum of the coins inserted"""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    true_quarters = quarters * 0.25
    true_dimes = dimes * 0.1
    true_nickels = nickels * 0.05
    true_pennies = pennies * 0.01

    return float(true_quarters + true_dimes + true_nickels + true_pennies)


def calculate_change():
    choice_cost = MENU[choice]['cost']
    return money_inserted - choice_cost


def deduct_resources(choice):
    if choice == "espresso":
        resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
    elif choice == "latte" or choice == "cappuccino":
        resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
    else:
        pass


# BEGIN PROGRAM
while On_Off:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    deliver_report(choice)

    turn_off(choice)

    if check_resources_sufficient(choice):

        print("Please insert coins.")

        money_inserted = process_coins()

        if money_inserted > MENU[choice]['cost']:
            money = money + money_inserted
            change_given = round(calculate_change(), 2)
            money = money - change_given
            print(f"Here is ${change_given} in change.")
            deduct_resources(choice)
            print(f"Here is your {choice} ☕. Enjoy!")
        elif money_inserted == MENU[choice]['cost']:
            money = money + money_inserted
            deduct_resources(choice)
            print(f"Here is your {choice} ☕. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")