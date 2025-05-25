#%%
#Shopping Cart

def display_menue():
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. Veiw cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def add_item(cart, prices):
    item_name = input("What item would yoou like to add?")
    item_price = float(input(f"What is the price of '{item_name}'?"))
    cart.append(item_name)
    prices.append(item_price)
    print(f"'{item_name}' has been added to the cart.")

def view_cart(cart, prices):
    if len(cart) == 0:
        print("Your shopping cart is empty.")
    else:
        print("The contents of the shopping cart are:")
        for i in range(len(cart)):
            print(f"{i+1}. {cart[i]} - ${prices[i]:.2f}")

def remove_item(cart, prices):
    if len(cart) == 0:
        print("Your shopping cart is empty.")
        return
    
    try:
        item_number = int(input("Which item would you like to remove? ")) - 1
        if 0 <= item_number < len(cart):
            removed_item = cart.pop(item_number)
            removed_price = prices.pop(item_number)
            print(f"'{removed_item}' has been removed from the cart.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")

def compute_total(prices):
    total = sum(prices)
    print(f"The total price of the items in the shopping cart is ${total:.2f}")

def main():
    cart = []
    prices = []
    
    print("Welcome to the Shopping Cart Program!")
    
    while True:
        display_menue()
        try:
            action = int(input("Please enter an action: "))
            if action == 1:
                add_item(cart, prices)
            elif action == 2:
                view_cart(cart, prices)
            elif action == 3:
                remove_item(cart, prices)
            elif action == 4:
                compute_total(prices)
            elif action == 5:
                print("Thank you. Goodbye.")
                break
            else:
                print("Invalid option. Please select again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()