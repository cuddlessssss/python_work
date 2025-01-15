bicycles=['trek','cannondale','redline','specialized']
print(f"My first bicycle was a {bicycles[0].title()}.")

names=['tristan', 'megan', 'beatriz']
print(f"{names[-1].title()} is my wife.")

print(f"Hello, {names[2].title()}. How was your exam?")
print(f"{names[0].title()}, You're the goat!")
print(f"Love you, {names[2].lower()}")

vehicles=['motorcycle','bicycle','car']
brands=['Mercedes','Honda','BMW']
print(f"I would like to own a {brands[1]} {vehicles[0]}.")

#practice 3.4
dinner_list=['mum','dad','kor','popo','jenny']
a=f"{dinner_list[0]} {dinner_list[1]}, Dinner at 12?"
b=f"{dinner_list[2]}, you're invited too!"
c=f'{dinner_list[4]}, are you free for lunch?'
d=f'{dinner_list[3]}, po ni yao yi qi chi wu can ma?'

#3-5
print(dinner_list[4])
busy=dinner_list.pop()
dinner_list.append('chye poh')
e=f'{dinner_list[-1].title()}, {busy} could not make it. Would you like to join for lunch?'
print(a)
print(b)
print(c)
print(d)
print(e)
dinner_list.insert(0,"baby")
dinner_list.insert(4,"ling ling")
dinner_list.append("wen sen")
print(dinner_list)
f=f'Good morning, {dinner_list[4].title()} and {dinner_list[-1].title()}, are you free later for lunch?'
g=f'{dinner_list[0].title()}, did you sleep well? lunch together? yippieee'
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

h=f'Sorry I can only invite 2 people to dinner cause of sudden space issues.'
i=dinner_list.pop()
j=dinner_list.pop(4)
print(f"Hi! {i.title()} and {j.title()}, sorry the restaurant did not record your reservations. Can we have lunch another time?")
k=dinner_list.pop()
print(f"Sorry lunch need to cancel cause restaurant did not record slots. Next time can? To {k.title()}")
l=f"{dinner_list.pop(1).title()} {dinner_list.pop(1).title()} {dinner_list.pop(1).title()}"

print(f"{l}, Sorry end up the place only have 3 slots so I eat with popo and my wife okay? Thanks!")
m=f"{dinner_list[0].title()}"
n=f"{dinner_list[-1].title()}"
print(f"{m}, only us and my grandma will come eat cause only 3 slots in the restaurant in the end...")
print(f"{n}, zhi you ni, wo, he wo nv peng you qu chi wu can. ying wei zhi you 3 ge wei zhi. zai jian!")
del dinner_list[0] 
del dinner_list[0]
print (dinner_list)