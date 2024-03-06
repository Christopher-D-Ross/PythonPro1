
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

quarter = .25
dime = .10
nickle = .05
penny = .01


def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")


def add_funds(funds):
    resources["money"] += funds


def deduct_resources(item):
    if item == "espresso":
        resources["water"] -= MENU[item]["ingredients"]["water"]
        resources["coffee"] -= MENU[item]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[item]["ingredients"]["water"]
        resources["milk"] -= MENU[item]["ingredients"]["milk"]
        resources["coffee"] -= MENU[item]["ingredients"]["coffee"]


def check_resources(item):
    if item == "espresso":
        if resources["water"] < MENU[item]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        if resources["coffee"] < MENU[item]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
    else:
        if resources["water"] < MENU[item]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            return False
        if resources["milk"] < MENU[item]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        if resources["coffee"] < MENU[item]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
    return True


def transact(q, d, n, p):
    paid = 0
    paid += q * quarter
    paid += d * dime
    paid += n * nickle
    paid += p * penny
    return paid


def get_change(amount_paid, item):
    if amount_paid >= MENU[item]["cost"]:
        add_funds(MENU[item]["cost"])
        print(f"Here is ${round(amount_paid - MENU[item]["cost"], 2)} in change.")
        return amount_paid - MENU[item]["cost"]
    else:
        print("Sorry that is not enough money. Money refunded.")
        return -1


def turn_off():
    return


def coffee_machine_order():
    item = input("What would you like? (espresso/latte/cappuccino): ")

    if item != "off" and item != "report":
        if check_resources(item):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            if get_change(transact(quarters, dimes, nickles, pennies), item) != -1:
                deduct_resources(item)
                print(f"Here is your {item}, Enjoy!")
                coffee_machine_order()
            else:
                coffee_machine_order()
        else:
            coffee_machine_order()

    if item == "off":
        turn_off()

    if item == "report":
        report()
        coffee_machine_order()


coffee_machine_order()
