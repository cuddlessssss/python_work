wife = {'first_name':'luna','last_name':'briones','age':69,
        'city':'small village'}
print(wife['first_name'].title())

numbers = {'luna':28, 'me':7, 'dad':401, 'mum':1969, 'bro':2807}

meanings = {'.pop':'pop out a number which can be used if stored in variable',
         'for_in_':'looping',
         '.get(_,_)':'first value is what we want, second is if not found',
         'set(_)':'DISTINCT values only from the things in the brackets',
         'list(_)':'creates a list',
         '.append()':'add a new item to the list',
         'len(_)':'count the number of elements in the list',
         '.remove(_)': 'remove item from list by value',
         'del _':'remove item from list by position',
         '_.insert(_,_)': 'add in which position and what item',
         }
print(f"\n.pop means to{meanings['.pop']}.")
print(f"\nfor_in_ means to do {meanings['for_in_']}.")
print(f"\n.get(_,_) inputs the {meanings['.get(_,_)']}.")
print(f"\nset(_) filters out the {meanings['set(_)']}.")
print(f'\nlist(_) {meanings['list(_)']}.')

for key, value in meanings.items():
        print(f"\nThe command {key} means to {value}.")

rivers = {'ganges': 'india', 'nile': 'egypt', 'mississipii': 'united states'}

print(f"\nThe river names in the list include:")
for key in rivers.keys():
        if key != "mississipii":
                print(key.title())
        else:
                print(f"and the {key.title()}")