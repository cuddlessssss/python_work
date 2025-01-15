def get_formatted_name(first_name,last_name,middle_name=''): #middle name without default be at the end
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

my_name=get_formatted_name('leonel','lim')
her_name=get_formatted_name('beatriz','briones','francisco')

print(my_name)
print(her_name)


def build_person(f_name,l_name):
    person={"first name":f_name,"last name":l_name}
    return person #dictionary cannot use title() !! because not individual string!!

singer = build_person("lady","gaga")
print(singer)

#like line 1-9 but with user input + quitting with while loops!!
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


    la_name=input("\nLast name: ")
    if la_name=='q':
        break

    midd_name=input("\nMiddle Name (Press Enter to skip): ") #MUST be in order of the above tooooo!
    if midd_name=='q':
        break
   
    final_name = get_formatted(fir_name,la_name,midd_name)
    print(f"\nWelcome to Thailand, {final_name}!")





