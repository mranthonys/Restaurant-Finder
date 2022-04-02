optMenu = [["Joe's Gourmet Burgersa", "no", "no", "no"],
            ["Main Street Pizza Company", 'yes', 'no', 'yes'],
            ["Corner Cafe", 'yes', 'yes', 'yes'],
            ["Mama's fine Italian", 'yes', 'no', 'no'],
            ["The Chef's Kitcnen", 'yess', 'yes', 'yes']]
    
average = 0 

opt1 = input("Is anyone in your party a vegetarian? (yes/no)")
if opt1 == "yes":
    average = average + 1 

opt2 = input("Is anyone in your party a vegan? (yes/no)")
if opt2 == "yes":
    average = average + 1

opt3 = input("Is anyone in your party gluten-free? (yes/no)")
if opt3 == "yes":
    average = average + 1

choice = []

for i in range(len(optMenu)):
    found = 0
    if opt1 == "yes":
        found = found + 1
    if opt2 == "yes":
        found = found + 1 
    if opt3 == "yes":
        found = found + 1
    if average == found: 
        choice.append(optMenu[i][0])

    if len(choice) > 0:
        print("Here are your restaurant choice:")
        for i in range(len(choice)):
                    print(choice[i])
    else: 
        print("Be Hungry")

