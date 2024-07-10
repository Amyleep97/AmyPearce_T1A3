# Video Game Trivia 

# Requirements to use this application 

### 1.  [Link to Install Python 3.12.4](https://www.python.org/downloads/)

- Once on this page click on Download Python 3.12.4

![python install step 1](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/491bce61-d6a3-45b4-b174-b575685614d9)

- Requirements:
Windows 7/10,
Mac OS X 10.11 or higher, 64-bit, Linux: RHEL 6/7, 64-bit, Ubuntu, x86 64-bit CPU, 4 GB RAM, 5 GB free disk space. 
([Source](https://support.enthought.com/hc/en-us/articles/204273874-Enthought-Python-Minimum-Hardware-Requirements))

2. Open the download and Install Python.

![Python instaqllation steps](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/51ba37c0-712c-4d17-a0da-5ed8dbb2b14e)

3. Install wsl/linux if you don't have it installed already. Open up Powershell/CMD and copy and paste the following.

``` wsl --install ```

- If you're unsure of which version you are running you might need to run:

``` wsl -l -v ``` 

![install wsl step](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/1ae75787-c8d5-43a0-86aa-ba20a39ce385)

## [A link to help you set up wsl/linux for windows](https://learn.microsoft.com/en-us/windows/wsl/install)


4. You now will need to download Git: [Download Git Here](https://git-scm.com/downloads) Once downloaded run the installation.

- [Step by step to install Git for windows](https://techdirectarchive.com/2020/05/23/how-to-clone-a-repository-and-install-software-from-github-using-the-terminal-for-windows-and-linux/) 

![download git 1](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/ae4810a4-3e86-4cb6-b8e9-9b67bf60ce81)

 - Type following into the terminal 
 5. ``` sudo apt-get install git```

 ![sudo step 1](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/c36dc706-c999-4285-96b9-02a468779470)


 6. ``` sudo apt-get install flex ```

![sudo step 2](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/b8c63fe0-8cea-43fe-9311-6979c97029f5)


- The terminal will ask you ``` Do you want to continue? [Y/n]``` type ```"y"``` and enter.

![sudo step 3](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/daf1d6c6-d63b-4b20-9e69-0fcb329bf76e)

7. Once that is installed copy ``` sudo apt-get install bison ```

8. Then ``` sudo apt-get install make ```

![sudo step 4](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/547eec67-6bd5-47e5-a36c-4b564c5b9e8d)


## [Source control repository](https://github.com/Amyleep97?tab=repositories)

## [Code style guide](https://www.cs.swarthmore.edu/~adanner/cs21/python_codestyle.php)

# Installation
 ### Option 1:

1. Download the zipfile from the github repository.

![download zip file from github](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/21f83559-fabe-46c5-b09d-1597d4751bfe)

2. Once saved you should Unzip the file, do this by extracting all. 


![main py step](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/577dc2f4-0e58-4fe2-8d25-f52c36c62f9e)

3. Open the file and click on main.py this will open up the terminal to start the application. 

## Option 2:

- In the terminal git clone: 
 ``` git clone git@github.com:Amyleep97/AmyPearce_T1A3.git ```
- Go into the directory
```cd AmyPearce_T1A3 ```

- type ``` ls ```

- Type ```python3 main.py ```

![cd_into_file_video_game_trivia](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/a5ef8693-5852-4096-8357-caf242e9ab13)


# Intro to this application/Rules to play:

-  You will first be introduced to the game by being welcomed with the sentence " Hello! Welcome to Video Game Trivia!" It will then ask you "Are you ready to begin? Type 'yes' to start " You must type ``` "yes" ```for the questions to begin.

- The first question will apear it should look like this:

![video_game_trivia_question_1](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/3b44c158-a76c-4e2d-bc29-27bb39fbf15c)


- There are 10 Questions to be answered each one is different.

- You must press the enter key after every answer in order to get a result. Always use Capitals at the start of each answer. (example: ``` counterstrike ```will error ```Counterstrike```will work.)

- The appplication will then give you a message depending on if your answer is correct or incorrect. 

- The game will tell you what the answer is if you didn't get it right. 


- At the half way mark the application sends a message saying "You're halfway!" to show your progress.

![questions_trivia](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/29f5f939-d8da-4070-b75c-9a5613d9881a)

- After answering all 10 Questions will see your score it will tell you how many you got Correct.

![end_of_trivia](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/72b43ba7-c3a0-4834-9b9c-8e08389a6f5c)


## Features:

- ``` question = input``` This function will ask the player a question.

- ``` if question == "1996": print("Correct! You're a wizard") score += 1 ``` This function gives the game a scoring system for each question if it is correct this will add 1 point.

- ``` else: print("Incorrect, sorry gamer :( The answer is 1996") ``` This function makes sure that if the answer is incorrect it does not tally a score and will tell you what the correct answer is. 

# Packets


# Implementation plan:
- Trello planning:
![Trello final peice](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/95d129d7-c8e2-4ae0-9eb1-bdb83acdbd8b)

- These first three cards are the brain storming part before I could even start my coding/assement
![brain storming 1](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/ddc7f672-9e50-4dfa-bd7c-8503334b15db)

![brain stroming 2](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/2d4a7467-a184-4e58-9186-f625b884d3bd)


![brain storming 3](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/c681ceb9-1030-4d8f-b922-c87279254c33)
