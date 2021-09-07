def priceChecker(numOfPeople,names,foodCost,average):
    for a in range(numOfPeople):
        
        #if they are under the average
        if foodCost[a] < average:
            print(names[a],"is under the average price by $","{0:.2f}".format(average - foodCost[a]))
        
        #if they are over the average
        elif foodCost[a] > average:
            print(names[a],"is above the average price by $","{0:.2f}".format(foodCost[a] - average))
        
        #if they are equal to the average
        elif foodCost[a] == average:
            print(names[a],"is equal to the average")


names = []
foodCost = []

try:
    numOfPeople = int(input("How many people will you be entering? "))
except ValueError:
    numOfPeople = int(input("Enter the number of people you will be entering: "))
    
print()
    
for i in range(numOfPeople):
    names.append(input("Enter person's name: "))
    try:
        foodCost.append(float(input("Enter this person's price of their food: ")))
    except ValueError:
        foodCost.append(float(input("Enter a valid price of their food: ")))
    print()

average = sum(foodCost) / numOfPeople
print("\nThe average of all the food is {0:.2f}".format(average))


priceChecker(numOfPeople,names,foodCost,average)


    