car='subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

print("\nIs car == 'Subaru' with capital S? I predict False")
print(car.title() == 'subaru') #case sensitive

print("\nIs car equal to SUBARU kept in upper? I predict False")
print(car.upper() == 'subaru')

alien_color = ['green']

if 'green' in alien_color:
    print("\nYou win 5 Points!")
else:
    print("\nYou won 10 Points!")

if 'green' not in alien_color:
    print("\nYou won 10 Points!")
else:
    print("\nYou win 5 Points!")

if 'green' in alien_color: #print nothing
    ""

if 'green' in alien_color:
    print("\nYou win 5 Points!")
elif 'yellow' in alien_color:
    print("\nYou win 10 Points!")
elif 'red' in alien_color:
    print("\nYou win 15 Points!")

age=65
print("\n")
if age<2:
    print("It's a baby!")
elif 2<=age<4:
    print("It's a toddler!")
elif 4<=age<13:
    print("It's a kid!")
elif 13<=age<20:
    print("It's a teenager!")
elif 20<=age<65:
    print("It's an adult!")
else:
    print("It's an elder!")

admins = ['jordan', 'leo', 'luna', 'dad', 'mum', 'admin']
new_users = ['Leo', 'Luna', 'aunty', 'uncle', 'baby']
current_users = ['luna', 'aunty', 'mum', 'dad', 'fatty']

print("\n")
if admins:
    for admin in admins:
        if admin == 'admin':
            print("\nWelCoMe, god of the world!")
        else:
            print(f"\nWelcome to {admin.title()}'s account!")
else:
    print("We need to find some users!")

for new_user in new_users:
    if new_user.lower() in current_users:
        print("\nUsername is taken. Please choose a new username.")
    else:
        print(f"\nWelcome new user: {new_user.title()} to the club!")

numbering = [values for values in range(1,10)]
print("\n")
for values in numbering:
    if values == 1:
        print(f"{values}st")
    elif values == 2:
        print(f"{values}nd")
    elif values == 3:
        print(f"{values}rd")
    else:
        print(f"{values}th")