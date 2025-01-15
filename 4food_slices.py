my_foods=["ice cream","cheesecase",'toffee nut','pizza']
owned_foods=my_foods[:]

my_foods.append("meal prep")
owned_foods.append("ice cream")

print("My owned foods are:")
print(owned_foods)

print("\nMy favourite foods are:")
print(my_foods)

print("\nThe first 3 foods I own are")
print(my_foods[:3])

print("\n The middle 3 foods I own are:")
print(my_foods[1:4])

print("\nThe last 3 foods I own are:")
print(my_foods[-3:])

print("The foods I enjoy include:")
for foody in my_foods:
    print(foody)

print("\nThe foods I own include:")
for fodd in owned_foods:
    print(fodd)

tuple_foods=('pizza','pasta',"chicken nugget",'chicken paste','spaghetti')

print('\nTasty foods in this restaurant include:')
for foodles in tuple_foods:
    print(foodles)

# tuple_foods[0]=pan #REJECT cause tuple CANNOT modify a tuple

tuple_foods=('eggs','pasta','chicken nugget','chicken paste','beef')
print("\nThe revised menu for this restaurant is:")
for fodins in tuple_foods:
    print(fodins)