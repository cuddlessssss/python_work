pizza_toppings = "What toppings would you like to have on your pizza?"
pizza_toppings += " Please enter here: "

while True:
    top=input(pizza_toppings)
    if top != "quit":
        print(f"\nWhat other toppings would you like? Enter 'quit' if all has"
          " been included.")
    else:
        break
print("\nThank you for your order. Kindly wait at the waiting counter while"
      " we prepare your food!")

ages = "Welcome to the cinema! What is your age? "
while True:
    age = input(ages)
    age = int(age)
    if age < 3:
        print("Your ticket is free of charge!")
    elif 3 <= age <= 12:
        print("Your ticket will be $10!")
    elif age > 12:
        print("Your ticket will be $15!")
    break


    



    


