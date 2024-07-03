# Video Game Quiz
print("Hello! Welcome to Video Game Trivia!")

playing = input ("Are you ready to begin? Type 'yes' to start ")

if playing !="yes":
    quit()

playing = input("Question 1:")
score = 0

question = input("What year was the nintendo 64 released?")
if question == " 1996":
    print("Correct! You're a wizard")
    score += 1
else:
    print("Incorrect, sorry gamer :(")

playing = input("Question 2:")

question = input("What is one of Nintendos most popular games?")
if question == " Super Mario Bros":
    print("Correct! Nice work!")
    score += 1
else:
    print("Incorrect, Unlucky! :(")

playing = input("Question 3:")


question = input("Which console was the first to ever have a built in modem?")
if question == " Playstation":
    print("Correct!!")
    score += 1
else:
    print("Incorrect, sorry gamer :(")

playing = input("Question 4:")


question = input("Pacman was made by which video game company?")
if question == " Namco":
    print("Correct!!")
    score += 1
else:
    print("Incorrect :(")


playing = input("Question 5:")

question = input("Which video game is the best selling to this day?")
if question == " Minecraft":
    print("Correct! You're Insane!")
    score += 1
else:
    print("Incorrect, that was hard hey :(")

playing = input ("You're halfway! Let's go!")

playing = input("Question 6:")


question = input("Steam has a chart of games that are most played, out of the top current 100 which one is number 1?")
if question == " Counter Strike":
    print("Correct! You're still in this")
    score += 1
else:
    print("Incorrect, so close")


playing = input("Question 7:")

question = input ("There are a few letters missing from this game title 'N i _ t _ _ d _ g _'  What game is it? ")
if question == " Nintendogs":
    print("Correct! You're too skilled")
    score += 1
else:
    print("Incorrect :(")

playing = input("Question 8:")

question = input("Who won the game of the year awards in 2020?")
if question == " The Last of Us Part II":
    print("Correct! you got this win in the bag")
    score += 1
else:
    print("Incorrect, unlucky! :(")

playing = input("Question 9:")

question = input("Name 3 DLCS that have recently been released in 2024: ")
if question == " Elden Ring, Destiny 2, Final Fantasy XIV":
    print("Correct!!!")
    score += 1
else:
    print("Incorrect, maybe next time :(")

playing = input ("Finish Him!") 

playing = input("Question 10:")

question = input("What animal is Pikachu?")
if question == " Mouse-like creature":
    print("Correct! :D")
    score += 1
else:
    print("Incorrect :(")

print("Your score is " + str(score) + " Nice work!")

playing = input ("GG, Thanks for playing!")






    