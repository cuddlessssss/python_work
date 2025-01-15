sandwich_orders = ["ham", "tuna", "pastrami","mayo","pastrami","pastrami"]
finished_sanwiches = []

print("The deli has ran out of pastrami... Sorry!\n")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    orders = sandwich_orders.pop()
    print(f"I made your {orders.title()} sandwich!")
    finished_sanwiches.append(orders)

print("\nThe sandwiches made include:")
for san in finished_sanwiches:
    print(f"{san.title()}")

poll_active = True #usage of flag + user inputs into dictionaries!
places = {}
while poll_active:
    name = input("\nWhat's your name? ")
    dream_vacation = input("\nWhere would you like to go for a dream vacation? ")

    places[name] = dream_vacation
    repeat = input('\nAre there any more respondants? (yes/no) ')
    if repeat == "no":
        poll_active = False