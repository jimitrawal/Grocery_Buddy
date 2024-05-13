'''
The grocery store allows the user to buy grocery items from various departments of the store, including Fruits & Vegetables, Bakery, Dairy, and Canned Foods. The user can select their items and its amount from the departments. Then, the user could further add more items and checkout. If the total bill of the grocery items is more than $50, the user has an opportunity to automatically-register into a lucky-draw where they can win a 10% discount to total bill. 
'''

import random
# Open all four files for reading distinct items of each department
fileA = open("fruits_vegetables.txt")
fileB = open("bakery.txt")
fileC = open("dairy.txt")
fileD = open("canned_foods.txt")

record = []  # Empty list which would book-keep items bought and their prices


def grocery_store(
    subtotal):  # Function to select a random item from the grocery store
  items_fruits_veggies = {  # Dictionary of grocery items and their prices
      'Apple': 2.00,
      'Banana': 1.75,
      'Grapes': 2.25,
      'Mango': 4.00,
      'Spinach': 3.00,
      'Tomato': 1.75,
      'Potato': 3.50
  }
  items_bakery = {
      'Cake': 8.00,
      'Bread': 2.50,
      'Tortilla': 3.75,
      'Cupcake': 4.00
  }
  items_dairy = {'Milk': 6.00, 'Cheese': 5.50, 'Yogurt': 4.25, 'Butter': 4.25}
  items_canned_foods = {
      'Soup': 3.25,
      'Noodles': 4.00,
      'Beans': 3.75,
      'Pasta': 4.00,
      'Sauce': 4.00
  }

  print("Welcome to JR's Grocery Store!\n")
  print("Select from the number of departments of groceries:\n")
  print("1)Fruits and Vegetables\n2)Bakery\n3)Dairy\n4)Canned Foods\n5)Exit\n")
  print(
      "*You can participate in a LUCKY DRAW and get a 10% discount if your total bill is greater than $50.00.*\n"
  )

  continue_shop = True  # Flag condition
  while continue_shop:  # Enters while loop until user selects 5 to exit
    department_selection = input(
        "Which department would you like to buy from?: "
    )  # Asks user to select department
    if department_selection == '5':
      bill(subtotal)
      break
    if department_selection not in [
        '1', '2', '3', '4'
    ]:  # Checks if the user inputs anything but 1-4
      print("Please enter a valid department number.")
      continue
    if department_selection == '1':
      print(fileA.read(120))  # Reads the first file
      add_to_cart(items_fruits_veggies, subtotal)
      break
    elif department_selection == '2':
      print(fileB.read(59))  # Reads the second file
      add_to_cart(items_bakery, subtotal)
      break
    elif department_selection == '3':
      print(fileC.read(59))  # Reads the third file
      add_to_cart(items_dairy, subtotal)
      break
    elif department_selection == '4':
      print(fileD.read(79))  # Reads the fourth file
      add_to_cart(items_canned_foods, subtotal)
      break

  # Closes all four files which read distinct items of each department
  fileA.close()
  fileB.close()
  fileC.close()
  fileD.close()


def add_to_cart(
    items, subtotal
):  # Helper function for selecting item, amount of items, and displays total price of items
  global record
  item_selection = input(
      "Select the item you would like to buy from the department:\n"
  ).capitalize()  # Asks for user input
  if item_selection in items:
    price = items[
        item_selection]  # Assigns price to the value of grocery items dictionary
    record.append(
        (item_selection, price))  # Appends the item and its price as a tuple
    print(f"{item_selection} would cost ${price:.2f}")
    while True:
      try:
        amount_selection = int(  # Tries to convert user input to an integer
            input(f"How many {item_selection}(s) would you like to buy?: "))
        subtotal += price * amount_selection  # Calculates the subtotal price of items
      except ValueError:  # Throws the print statement below if there is a ValueError
        print("Please enter a valid number.")
      else:
        break
    continue_buying = input("Do you want to shop more items? (y/n): ")
    while True:
      if continue_buying == 'n':
        return bill(subtotal)  # Returns the sub-total and exits the program
      elif continue_buying == 'y':
        return grocery_store(subtotal)  # Call back to the main function
      else:
        print("Invalid Input")
        continue_buying = input("Do you want to shop more items? (y/n): ")

  else:
    print("Item not sold in this department")
    add_to_cart(items, subtotal)  # Recalls the function


def bill(
    subtotal
):  # Helper function for calculating the total, subtotal, chances of discount, and overall bill
  with open("bill.txt", "w") as bill_file:  # Writing to a file
    print(f"Your subtotal is ${subtotal:.2f}")
    print(f"\nYou bought {record}")
    if subtotal > 50:  # If subtotal is greater than 50, add a discount if disount is equal to True
      discount = random.choice([True, False])  # Implements random discount
      if discount:
        print("Lucky, you qualify for a 10% discount!")
        total = subtotal - subtotal * 0.1
        print(f"Your final bill is {total:.2f}")
        bill_file.write(f"Your final bill is {total:.2f}")
      else:
        print(f"Your final bill is ${subtotal:.2f}")
        bill_file.write(f"Your final bill is {subtotal:.2f}") # Writes final total to the file
    else:
      print(f"Your final bill is ${subtotal:.2f}")
      bill_file.write(f"Your final bill is {subtotal:.2f}") # # Writes final total to the file

  print("\nThank you for shopping with JR's Grocery Store!")


grocery_store(0)  # Calls the function
