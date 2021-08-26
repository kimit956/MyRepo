
myFile = open("dayFile.txt", "w")

try:
    howDay = input("Are you having a good or bad day today? ")
except ValueError:
    howDay = input("Good or bad? ")
    
howDay = howDay.lower() #howDay stands for 'how is your day"

while (howDay != "good" and howDay != "bad"):
    howDay = input("Is it a good or bad day?: ")
myFile.write(howDay) #puts the user's input into the file
myFile.close() #must close the file and reopen it to read it after writing in it

myFile1 = open("dayFile.txt", "r")
if myFile1.read() == "good":
    print("Have a great rest of your day! : D")
else:
    print("I hope you have an excellent rest of the day!")

myFile1.close()
