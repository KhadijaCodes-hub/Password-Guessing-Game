import random

easy = ["coins", "money", "apple","train","tiger"]
medium = ["python","bottle","monkey","planet","laptop"]
hard = ["elephant","diamond",'umbrella',"computer","mountain"]

print("Welcome To Password Guessing Game!")
playing = input("Do you want to play game? (yes / no)\n").strip().lower()
if playing=="no":
    quit()
else:
    print("Let's Start Playing...")
    print(f"Choose From Three Difficulty Levels (Easy / Medium / Hard)")

    level = input('Enter Difficulty Level\n').strip().lower() 
    if level == "easy": 
        secret = random.choice(easy)
    elif level == "medium":
        secret = random.choice(medium)
    elif level=="hard":
        secret = random.choice(hard) 
    else:
        print("Invalid Choice.Defaulting to Easy Level") 
        secret = random.choice(easy)
        
    print("Number of letters in password are ",len(secret))
    attempt = 0
    while True:
        guess = input("Guess the password: \n").strip().lower()
        attempt += 1

        if guess==secret:
            print(f"CONGRATULATIONS!..You guesses it in {attempt} attempts.")
            break

        hint =""
        for i in range(len(secret)):
            if i<len(guess) and guess[i]==secret[i]:
                hint += guess[i]
            else:
                hint += "_"  
        print(f"Hint : {hint}") 
    print("Game Over.")     




        





