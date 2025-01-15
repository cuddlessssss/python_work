#parrot
message = input('Tell me something, and I will repeat it back to you: ')
print(message)

name = input('Please enter your name: ')
print(f'Hello, {name}!')

rental_query = input('What type of rental car would you like? ')
print(f"Let me see if I can find you a {rental_query}.")

dinner_group = input('How many people do we have dining here today? ')
dinner_group = int(dinner_group)
if dinner_group > 8:
    print("Please wait to be seated, the restaurant is currently full.")
else:
    print("Your table is ready! Please head on in. :)")

multten = input("Whats the number? I'll check if its divisible by 10! ")
multten = int(multten)
if multten % 10 == 0:
    print("Bingo! Your number is divisible by 10!")
else:
    print("Boink! Number indivisible by 10!")