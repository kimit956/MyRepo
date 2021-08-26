#This is used for save lists in .txt file
import json

#asks user for store's name
def askStoreName(storeNames):
    try:
        singleStoreName = input("Enter a store's name: ")
    except ValueError: #does not allow numbers to be entered as store names
        singleStoreName = input("Enter a valid store name: ")
    storeNames.append(singleStoreName) #will add each name to the storeNames list
    
#asks user for store's location
def askStoreLocation(storeLocations):
    try:
        singleLocation = input("Enter a store's location: ")
    except ValueError:
        singleLocation = input("Enter a valid store location: ") #does not allow numbers to be entered as a store location
    storeLocations.append(singleLocation) #adds each store locations entered to the store locations list


#asks the user how much money of each bill and coin is at the store
def storeMoney(currency):
    money = 0
    
    #hundreds
    money = int(input("How many 100 dollar bills are there for this store? "))
    currency.append(money)
    
    #fifties
    money = int(input("How many 50 dollar bills are there for this store? "))
    currency.append(money)        
    
    #twenties
    money = int(input("How many 20 dollar bills are there for this store? "))
    currency.append(money)        
    
    #tens
    money = int(input("How many 10 dollar bills are there for this store? "))
    currency.append(money)        
    
    #fives
    money = int(input("How many 5 dollar bills are there for this store? "))
    currency.append(money)        
    
    #ones
    money = int(input("How many 1 dollar bills are there for this store? "))
    currency.append(money)        
    
    #quarters
    money = int(input("How many quarters are there for this store? "))
    currency.append(money)        
    
    #dimes
    money = int(input("How many dimes are there for this store? "))
    currency.append(money)        
    
    #nickels
    money = int(input("How many nickels are there for this store? "))
    currency.append(money)        
    
    #pennies
    money = int(input("How many pennies are there for this store? "))
    
    #adds each dollar and coin to currency list which will be converted to actual money later
    currency.append(money)
    print()
    
    
#Converts coins to dollars and stores total for the store
def moneyConverter(currency,storeTotal):
    dollars = 0
    coins = 0 #this is to separate the coins from the dollars so it can convert the coins to dollars

    #hundreds
    dollars = currency[0] * 100
    
    #fifties
    dollars = (currency[1] * 50) + dollars
    
    #twenties
    dollars = (currency[2] * 20) + dollars
    
    #tens
    dollars = (currency[3] * 10) + dollars
    
    #fives
    dollars = (currency[4] * 5) + dollars        
    
    #ones
    dollars = currency[5] + dollars        
    
    #quarters
    coins = (currency[6] * 25) + coins    
    
    #dimes
    coins = (currency[7] * 10) + coins
    
    #nickels
    coins = (currency[8] * 5) + coins        
    
    #pennies
    coins = currency[9] + coins
        
    #coins to dollars
    dollars = dollars + round((coins / 100),2) #rounds to 2 decimal places
    
    storeTotal.append(dollars)



def main():
    store = open("SalesForAllStores.txt","w")
    storeNames = []
    storeLocations = []
    storeTotal = []
    
    #hundreds, fifties, tens, fives, ones, quarters, dimes, nickels, pennies
    currency = [] 
    
    #grand total variable
    grandTotal = 0
    
    #will ask the user how many stores they will be entering/keeping track of
    try:
        numStores = int(input("How many stores will you be entering? "))
    except ValueError:
        numStores = int(input("Enter a valid number: "))
        
        
    #will do for each store and print out info
    for a in range(numStores):
        askStoreName(storeNames)
        askStoreLocation(storeLocations)
        storeMoney(currency)
        moneyConverter(currency,storeTotal)
        currency = [] #resets the currency list so that the next store that is entered does not get messed up 
        print(storeNames[a], "is located at", storeLocations[a]) #prints the store name and location
        print(storeNames[a], "has a total of ${:,.2f}".format(storeTotal[a])) #prints the total for each store and formats it so there are commas in the correct places
        print()        
    
    
    #grand total of all stores    
    for b in range(numStores):
        grandTotal += storeTotal[b]
    

    #prints grand total
    print("The grand total for all stores is ${:,.2f}".format(grandTotal))
    
    print()
    
    save = input("Would you like to save this data? ")    
    
    #will add all the final data to a .txt file if the user answers yes
    save = save.lower()
    if save == "" or save == "y" or save == "yes":
        store.write(json.dumps(storeNames))
        store.write(json.dumps(storeLocations))
        store.write(json.dumps(storeTotal))
        store.write(str(grandTotal))
main()










