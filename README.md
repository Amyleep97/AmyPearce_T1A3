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


## [Source control repository](https://github.com/Amyleep97?tab=repositories)

## [Code style guide]()

# Installation
 - Type following into the terminal 
 1. ``` sudo apt-get install git```

 ![sudo step 1](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/c36dc706-c999-4285-96b9-02a468779470)


 2. ``` sudo apt-get install flex ```

![sudo step 2](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/b8c63fe0-8cea-43fe-9311-6979c97029f5)


- The terminal will ask you ``` Do you want to continue? [Y/n]``` type ```"y"``` and enter.

![sudo step 3](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/daf1d6c6-d63b-4b20-9e69-0fcb329bf76e)

3. Once that is installed copy ``` sudo apt-get install bison ```

4. Then ``` sudo apt-get install make ```

![sudo step 4](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/547eec67-6bd5-47e5-a36c-4b564c5b9e8d)



5. You now will need to download Git: [Download Git Here](https://git-scm.com/downloads) Once downloaded run the installation.

- [Step by step to install Git for windows](https://techdirectarchive.com/2020/05/23/how-to-clone-a-repository-and-install-software-from-github-using-the-terminal-for-windows-and-linux/) 

![download git 1](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/ae4810a4-3e86-4cb6-b8e9-9b67bf60ce81)

6. Once you have followed all the Git installation steps you should now download the zipfile from the github repository.

![download zip file from github](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/21f83559-fabe-46c5-b09d-1597d4751bfe)

7. Once saved you should Unzip the file, do this by extracting all. 

8. Open the file and click on main.py this will open up python terminal to start the application. 

![main py step](https://github.com/Amyleep97/AmyPearce_T1A3/assets/168613540/577dc2f4-0e58-4fe2-8d25-f52c36c62f9e)


# Intro to this application/Rules to play:

-  You will first be introduced to the game by being welcomed with the sentence " Hello! Welcome to Video Game Trivia!" It will then ask you "Are you ready to begin? Type 'yes' to start " You must type ``` "yes" ```for the questions to begin.

- There are 10 Questions to be answered each one is different.

- You must press the enter key after every answer in order to get a result. Always use Capitals at the start of each answer. (example: ``` counterstrike ```will error ```Counterstrike```will work.)

- The appplication will then give you a message depending on if your answer is correct or incorrect. 

- The game will tell you what the answer is if you didn't get it right. 

- At the half way mark the application sends a message saying "You're halfway!" to show your progress.

- After answering all 10 Questions you will see your score it will tell you how many you got Correct.

## Features:

- ``` question = input``` This function will ask the player a question.

- ``` if question == "1996": print("Correct! You're a wizard") score += 1 ``` This function gives the game a scoring system for each question if it is correct this will add 1 point.

- ``` else: print("Incorrect, sorry gamer :( The answer is 1996") ``` This function makes sure that if the answer is incorrect it does not tally a score and will tell you what the correct answer is. 


# Note: Ensure that your features above allow you to demonstrate your understanding of the following language elements and concepts:

- use of variables and the concept of variable scope

- loops and conditional control structures

- error handling


Consult with your educator to check your features are sufficient .


# Develop an implementation plan which:
- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

- Utilise a suitable project management platform to track this implementation plan.

- Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan. 

- checklists for each feature should have at least 5 items.



# Design help documentation which includes a set of instructions which accurately describe how to use and install the application.






- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application