class CoffeeMachine():
  def __init__(self):
      self.resources = [400, 540, 120, 9, 550]
      self.espresso = [250, 0, 16, 1, 4]
      self.latte = [350, 75, 20, 1, 7]
      self.cappuccino = [200, 100, 12, 1, 6]


  def remainder(self):
      print("The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n"
            "{} of money".format(self.resources[0], self.resources[1], self.resources[2], self.resources[3], self.resources[4]))


  def make(self, coffee):
      ingredients = ["water", "milk", "coffee beans", "cups"]
      for i in range(4):
          if self.resources[i] < coffee[i]:
              print("Sorry, not enough {}!".format(ingredients[i]))
              return
      print("I have enough resources, making you a coffee!")
      for i in range(4):
          self.resources[i] -= coffee[i]
      self.resources[4] += coffee[4]


  def buy(self):
      choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
      if choice == "1":
          self.make(self.espresso)
      elif choice == "2":
          self.make(self.latte)
      elif choice == "3":
          self.make(self.cappuccino)


  def fill(self):
      self.resources[0] += int(input("Write how many ml of water do you want to add:"))
      self.resources[1] += int(input("Write how many ml of milk do you want to add:"))
      self.resources[2] += int(input("Write how many grams of coffee beans do you want to add:"))
      self.resources[3] += int(input("Write how many disposable cups of coffee do you want to add:"))


  def take(self):
      print("I gave you ${}".format(self.resources[4]))
      self.resources[4] = 0


  def action(self):
      action = input("Write action (buy, fill, take, remaining, exit):")
      while action != "exit":
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.remainder()
        action = input("Write action (buy, fill, take, remaining, exit):")
        
CoffeeMachine().action()
