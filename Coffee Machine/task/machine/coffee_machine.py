def remainder(resources):
    print("The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n"
          "{} of money".format(resources[0], resources[1], resources[2], resources[3], resources[4]))


def buy():
    espresso = [250, 0, 16, 1, 4]
    latte = [350, 75, 20, 1, 7]
    cappuccino = [200, 100, 12, 1, 6]

    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if choice == "1":
        make(espresso)
    elif choice == "2":
        make(latte)
    elif choice == "3":
        make(cappuccino)


def make(coffee):
    ingredients = ["water", "milk", "coffee beans", "cups"]
    for i in range(4):
        if resources[i] < coffee[i]:
            print("Sorry, not enough {}!".format(ingredients[i]))
            return
    print("I have enough resources, making you a coffee!")
    for i in range(4):
        resources[i] -= coffee[i]
    resources[4] += coffee[4]


def fill(resources):
    resources[0] += int(input("Write how many ml of water do you want to add:"))
    resources[1] += int(input("Write how many ml of milk do you want to add:"))
    resources[2] += int(input("Write how many grams of coffee beans do you want to add:"))
    resources[3] += int(input("Write how many disposable cups of coffee do you want to add:"))


def take(resources):
    print("I gave you ${}".format(resources[4]))
    resources[4] = 0


resources = [400, 540, 120, 9, 550]

action = input("Write action (buy, fill, take, remaining, exit):")
while action != "exit":
    if action == "buy":
        buy()
    elif action == "fill":
        fill(resources)
    elif action == "take":
        take(resources)
    elif action == "remaining":
        remainder(resources)
    action = input("Write action (buy, fill, take, remaining, exit):")


