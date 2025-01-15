def get_formatted_name(first_name, last_name, middle_name=''):
    # If middle name is provided, include it in the full name
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' at any time to quit")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    m_name = input("Middle name (press Enter to skip): ")
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name, m_name)
    print(f"\nHello, {formatted_name}!")
#good code




#code fixed
def get_formatted(fir_name,la_name,midd_name=''): #middle name without default be at the end
    if midd_name:
        fu_name = f"{fir_name} {midd_name} {la_name}"
    else:
        fu_name = f"{fir_name} {la_name}"
    return fu_name.title()

while True:
    print("\nPlease enter your full name: ")
    print("Type 'q' at any point to end the program.")
    fir_name=input("\nFirst name: ")
    if fir_name=="q":
        break

    midd_name=input("\n(If none, please leave this blank) Middle Name: ")
    if midd_name=='q':
        break

    la_name=input("\nLast name: ")
    if la_name=='q':
        break

    final_name = get_formatted(fir_name,la_name,midd_name)
    print(f"\nWelcome to Thailand, {final_name}!")

