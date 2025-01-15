motorcycles=['honda','yamaha','suzuki']
motorcycles[0]='ducati'
motorcycles.insert(0,'mercedes')
print(motorcycles)
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {popped_motorcycles.title()}.")