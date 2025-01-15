favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

take_pls = ['baby', 'kenn', 'leo', 'jen', 'edward']

for undertakers in take_pls:
    if undertakers in favourite_languages.keys():
        print(f"Thank you {undertakers.title()} for your participation" 
              "in the survey!")
    else:
        print(f"Good afternoon {undertakers.title()}!"
             "Stand a chance to win $50 Starbucks Gift Card when you"
             "help us with this survey! Please share your exprience of SCSM24!"
             "It will be much appreciated! https://abc.com/scsm2024")
#remember to indent + "" for each NEW LINE in F string ->
#Otherwise, will have unterminated string literal!uy