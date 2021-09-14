import os
# -*- coding: utf-8 -*-


#Question 1: color of the sky
def question1(questions):
    questions.append(input("What color is the sky (when standing on Earth)? "))
    
    #if option
    #option a: purple
    #option b: green
    #option c: red
    #option d: Black


#Question 2: mac and cheese and spork
    
    
    
    
#Question 3: burnt chocolate should NOT get water



#Question 4: 
    
    
    



#Question 5: guess that pokemon: Cacnea | Grass | 119


    
print(f"For the next 5 questions you will have to Guess That Pokemon! :)")
print("P.S. They will be from Gen 3 (Hoenn); the numbers will NOT be referring to the National Pokédex number")

#Question 6: guess that pokemon: Cacnea | Grass | 119
def q6(question,attempt,score,allAttempts,correct):
    attempt = 0 #resets every question
    score = 0 #resets every question; 1 is correct
    question = input("What is the Pokémon with the Pokédex entry of 119? ").lower()
    
    #does the question as long as the amount of attempts is not 10
    while attempt != 10 and question != "cacnea":
        if question == "cacnea":
            score += 1
        else:
            print("Incorrect")
            attempt += 1
            
        #after 3 attempts, asks user if they would like a hint
        if attempt == 3:
            
            #will ask the user if they want a hint
            hint = input("Would you like a hint (Y|N)? ").lower()
            
            if hint == "y" or hint == "yes":
                print("This Pokémon is a grass type, evolves into Cacturne, and looks like a small cactus.")
            else:
                print("Ok. You have " + str(10-attempt) + "attempt(s) left.")
            
    if question == "cacnea":
        print("Correct!")
    else:
        print("You ran out of attempts. Moving to next question...")
        
    correct.append(score)
    allAttempts.append(attempt)    
    
    os.system("cls" if os.name == "nt" else "clear") #should clear the screen before the next question
        
    
    
    
    
    
    
    
#Question 7: guess that pokemon: Crobat | Poison, Flying | 065
    
    
    
#Question 8: guess that pokemon: Huntail | Water | 177
    
    
    
#Question 9: guess that pokemon: Breloom | Grass, Fighting | 035
    
    
    
#Question 10: guess that pokemon: Marshtomp | Water, Ground | 008





question = ""
score = 0 #this will see how many questions the user answers correctly within the given attempts
correct = []
attempt = 0 #this will keep track of how many guesses it took for the user to answer the question correctly with max of 10 attempts
allAttempts = []

q6(question,attempt,score,allAttempts,correct)



#questions.append(int(input("What year is it?")))
#options.append(2021)
#options.append(2020)
#options.append(2022)
#options.append(6546)

#print(options)
