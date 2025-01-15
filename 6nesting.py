#list of dictionaries -- just print :( sadly will have the brackets and all!
#can i remove the brackets and all somehow without being tedious?
baby = {'first_name':'luna','last_name':'briones','age':69,
        'city':'small village'}
mum = {'first_name':'betty','last_name':'khoo','age':55,
        'city':'singapore'}
dad = {'first_name':'kenn','last_name':'lim','age':59,
        'city':'singapore'}
people = [baby, mum, dad]

for humans in people:
    print(humans)

favourite_places = {"leo":['chiang mai', 'china'],
                    "mum":['office', 'home'],
                    "bro":['gym', 'machinese']}

#double looping for dictionary with lists
for keys,values in favourite_places.items():
    print(f"\n{keys.title()}'s favourite places to go include:")
    for places in values:
        print(f'{places.title()}')

numbers = {'luna':[28, 69], 'me':[7, 2207], 'dad':[401, 1969],
            'mum':[1969], 'bro':[2807]}

for nom, valuess in numbers.items():
    print(f"\n{nom.title()} likes:")
    for valx in sorted(valuess):
        print(f'{valx}')

#dictionaries in dictionary
cities = {
        'singapore':{
                'prices':'very expensive',
                'living standard':'amazing',
                },
        'chiang mai':{
                'prices':'affordable',
                'living standard':'comfortable',
                },
        'x-traversee':{
                'prices':'expensive',
                'living standard':'amazing',
                },
                }

for dict, dicts in cities.items():
    print(f"The city {dict.title()} is {dicts['prices']} to live in and"
          f" has a {dicts['living standard']} living standard.")

        

