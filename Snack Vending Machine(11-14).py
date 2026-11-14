#You build a snack vending machine that accepts coins one at a time, rejects invalid ones, stops once enough money is inserted, and calculates any change owed using a function.


def get_change(paid,price):
    return paid-price

print("===Welcome to the Snack Vending Machine! Snacks cost NPR50.===")

total = 0

while total < 50:
    coin = int(input("Insert coins (5, 10, 25):"))
    if coin == 5 or coin == 10 or coin == 25:
        total += coin
        print("Total coins inserted so far:",total)
    else:
        print("Invalid coin! The coin should be the given numbers 5,10,25! Please try again.")

print("Here is your snack ENJOY! Your change is:",get_change(total,50))
print("====Thank You for using the vending machine!====")