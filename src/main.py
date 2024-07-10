# Video Game Trivia
print("Hello! Welcome to Video Game Trivia!")

playing = input ("Are you ready to begin? Type 'yes' to start ")

if playing !="yes":
    quit()
     
question = input("Question 1: What year was the nintendo 64 released?")
score = 0

if question == "1996":
    print("Correct! You're a wizard")
    score += 1
else:
    print("Incorrect, sorry gamer :( The answer is 1996")

question = input("Question 2: What is Nintendos most popular game?")

if question == "Super Mario Bros":
    print("Correct! Nice work!")
    score += 1
else:
    print("Incorrect, Unlucky! The answer was Super Mario Bros")

question = input("Question 3: Which console was the first to ever have a built in modem?")
if question == "Playstation":
    print("Correct!!")
    score += 1
else:
    print("Incorrect, sorry gamer :( The Answer is Playstation")


question = input("Question 4: Pacman was made by which video game company?")
if question == "Namco":
    print("Correct!!")
    score += 1
else:
    print("Incorrect :( The Answer is Namco")


question = input("Question 5: Which video game is the best selling to this day?")
if question == "Minecraft":
    print("Correct! You're Insane! You're halfway!")
    score += 1
else:
    print(" Incorrect, that was hard hey :( The answer is Minecraft. You're halfway!" )


question = input("Question 6: Steam has a chart of games that are most played, out of the top current 100 which one is number 1?")
if question == "Counter Strike":
    print("Correct! You're still in this.")
    score += 1
else:
    print("Incorrect, so close! The correct answer is Counter Strike.")


question = input ("Question 7: There are a few letters missing from this game title 'N i _ t _ _ d _ g _'  What game is it? ")
if question == "Nintendogs":
    print("Correct! You're too skilled")
    score += 1
else:
    print("Incorrect :( The Correct answer is Nintendogs")

question = input("Question 8: Who won the game of the year awards in 2020?")
if question == "The Last of Us Part II":
    print("Correct! you got this win in the bag")
    score += 1
else:
    print("Incorrect :( The correct answer was The Last of Us Part II")


question = input("Question 9: Name 3 DLCS that have recently been released in 2024: ")
if question == "Elden Ring, Destiny 2, Final Fantasy XIV":
    print("Correct!!! Finish Him!")
    score += 1
else:
    print("Incorrect, the correct answer was Elden Ring, Destiny 2, Final Fantasy XIV")


question = input("Question 10: What animal is Pikachu?")
if question == "Mouse":
    print("Correct! :D")
    score += 1
else:
    print("Incorrect, the correct answer was Mouse")

print("Your score is " + str(score) + " Nice work!")

playing = input ("GG, Thanks for playing!")






    





