numbers=[value**2 for value in range(1,11)]
print(numbers)

counting=[num for num in range(1,21)]
print (counting)

million=[millions for millions in range(1,1_000_001)]
print(million)
#all BELOW only works in temrinal window
min(million)
max(million)
sum(million)

threes=[three for three in range(3,31,3)]
print(threes)

cubed=[cubes**3 for cubes in range(1,11)]
for cubing in cubed:
    print(cubing)#if WANT print vertical list



squaress=[]
for abcd in range (1,11):
    abc=abcd**3
    squaress.append(abc)
print(squaress)

for squaredd in squaress: #looping gives vertical list
    print(squaredd)