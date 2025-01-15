unconfirmed_users=["andrew", "candace", "leo"]
confirmed_users=[]

while unconfirmed_users:
    checked = unconfirmed_users.pop()
    confirmed_users.append(checked)
    print(f"Verifying user: {checked.title()}")

print("\nHere is the list of confirmed users:")
for confirmed_user in confirmed_users:
    print(f"{confirmed_user.title()}")


polling_active = True
dictionaries = {}
while polling_active:
    name = input("What's your name? ")
    ice_cream = input("What's your favourite ice cream flavour? ")
    dictionaries[name] = ice_cream

    more_people = input("Do you wish to key in another input? (yes/no) ")
    if more_people == "no":
        polling_active = False