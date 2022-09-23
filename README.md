# Project Overview
## Please check my [Github repository](https://github.com/lmh4686/Terminal_App) to view the codes.
## Please check my [Trello](https://trello.com/b/CeoQTkAx/terminal-app) to check project planning.
## [PEP8](https://peps.python.org/pep-0008/) style has been applied for this project.
## This farming game is inspired from [Minecraft](http://minecraft.net/minecraft).
## Systme requirements:
  - ### [Ubuntu](https://ubuntu.com/) for Windows users or [Xcode](https://developer.apple.com/xcode/) and [Homebrew](https://brew.sh/) for Mac users.
  - ### [Python3](https://www.python.org/downloads/)
## Applied packages and module
 - [PrettyTable_3.4.1](https://pypi.org/project/prettytable/)
    - Used for printing a table form.
 - [Colorama_0.4.5](https://pypi.org/project/colorama/)
    - Used for giving a background color, font color, style to printed texts.
 - [AsciiMagic_1.6](https://pypi.org/project/ascii-magic/)
    - Used for converting images to ascii art. 
 - [Random](https://docs.python.org/3/library/random.html)
    - Used for picking random objects, random number within certain range.
***

# Program features
## Porgram overview
There're three different types of locations that user can explore. 2 are fruit farm and grain farm, the other is home. The main goal is harvesting resources from the farms and cooking at the home. 
### Key componetns 
#### 1. Bag
 - Can contain harvested object from farms
 - 30 limited space
#### 2. Storage
 - No space limit but only accessible at home.
 - Automatically gets transferred all items from 'bag' on arrval to home.
#### 3. Recipes
 - Contain 4 dishes's recipe Apple porridge, Orange porridge, Plum porridge and Mixed porridge.
 - Each dish contains differrent required amount of items to cook.
***
## Features by locations
### Landing
![Landing](docs/landing_ex.png)  
### Read the provided options and type the number to make a decision.
### Fruit farm
![Fruit farm](docs/Fruit_farm_explain.png)  
### On arrival, a random harvestable object will appear that could be an 'Apple', 'Orange' and 'Plum'. Users have options as follows :

### (1)Harvest :
![Fruit farm harvest result](docs/fruit_farm_harvest.png)
 - Random amount(from 1 to 3) of harvested object will store to the 'bag'.
 - Shows available space of the 'bag' after harvest.
 - When bag gets full it will automatically take users to 'home':  
![Bag full result](docs/bag_full.png)
### (2)Skip :
![Fruit farm skip result](docs/fruit_farm_skip.png)
 - Skip the current object and show the next random object.

### (3)Check bag:
![Fruit farm check bag result](docs/Check_bag.png)
 - Show a table of item and amount for each.

### (4)Check recipes:
![Fruit farm check recipes result](docs/Check_recipes.png)
 - Show a table of recipes seperated by dish name and recipe for each.

### (5)Go to Grain farm:
![Grain farm result](docs/grain_farm_explanation.png)
 - Move to Grain farm
 - Further information is available in Grain farm article.

### (6)Go to home:
![Home result](docs/hom_explanation.png)
 - Move to Home
 - Further information is available in Home article.

### (7)Quit the game:
![Quit result](docs/Terminate_game.png)
 - Immediately terminates the program.
***
### Grain farm:
![Grain farm result](docs/grain_2.png)
### Shares same features with Fruit farm but different harvestable objects: 
 - Wheat
 - Corn
 - Oat
### Another difference is '(5) Go to Fruit farm' that takes user to 'Fruit farm'.
***
### Home:
### Home does not offer harvestable objects but users can cook. **On arrival, all items in the 'bag' will be transferred to 'storage' that has unlimited space.** 
### Then, program will check if there's enough grocery to cook by comparing items in the 'storage' with the 'recipes'.
### If there is not enough item to cook:
![Result for not enough food](docs/no_enough_food.png)  
Show updated storage and let users to choose to go to farm.
### If storage has enough item to cook that meet any of specific dish's recipe, it shows a list of available amount of dish to cook.
![options when cooking is available](docs/cook_available.png)  
*Note: Choice of (2) will prompt users to choose the farm and move to selected farm. Choice of (3) will terminate the program.*   
(1)Choose dish to cook:  
![Results of (1)](docs/choose_dish.png)  
User can select one of the available dish to cook.  
If user choose 'Apple porridge':    
![Next step after user's decision to cook](docs/food_choice.png)  
Asking user a number of dish to cook.  
If user enter '2':  
![Results for cook 2 dihses](docs/another_cook.png)  
It will show a number of dish that user cooked and updated storage after cook.  
User can choose another dish to cook or go to farm.   
If there's no more available dish to cook:  
![Results for not enough grocery after cook](docs/after_cook_no_food.png)  
User will get asked to go to farm.
# Error handling for inputs
### When user not type the provided number and :
#### **when Input reamins as string.**
![Results for input error](docs/str_input1.png)  
 - Raise and catch custom error 
 - returns users' input with error message and let users retry it.

#### **when Input converted to an integer and :**
 - user input integer but bigger than given option:  
![Results for bigger integer input error](docs/toobig.png)
   - Raise and catch custom error
   - Return allowed maximum amount 
 - user input is not integer or smaller than 1:  
![Result for input smaller than 1 or not integer](docs/wrongint.png)  
   - Catch ValueError or raise and catch custom error
   - Print error message
### For KeyboardInterrupt
Case 1  
![Result for keyboard interrupt](docs/key_int1.png)  
Case 2  
![Result for keyboard interrupt](docs/key_int2.png)  
Case 3  
![Result for keyboard interrupt](docs/key_int3.png)


# Installation guide
## This program 
## Guidance for Windows users
### 1. Install [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-au&gl=au)
### 2. Install [Ubuntu 22.04.1 LTS](https://apps.microsoft.com/store/detail/ubuntu-22041-lts/9PN20MSR04DW?hl=en-au&gl=au)
### 3. Enable the optional feature from PowerShell
```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
 - This will restrart your computer.
This guidance is originally posted on [HERE](https://janelbrandon.medium.com/a-guide-for-using-wsl-for-development-d135670313a6).
<!-- ### 3. Install [Python 3.10](https://www.python.org/downloads/)
#### In your ubuntu, apply this code one by one to install Python: -->
### 4. Install [Python 3](https://www.python.org/downloads/) by applying commands below to ubuntu.
```
sudo apt update
sudo apt install software-properties-commonsoftware-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10
```
 - This python installaion guide is originally from [here](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu).
### 5. Clone the files from [this repository](https://github.com/lmh4686/Terminal_App) by applying code below.
```
git clone https://github.com/lmh4686/Terminal_App.git
```
### 6. After installation, direct to [src](src) folder.
```
cd Terminal_App/src
```
### 7. Apply this code to excecute the program.
```
./farming_game.sh
```
### 8. Authorise the program to activate Virtualenv and download packages.
![farming_game.sh Initial screen](/docs/step_8.png)  
 - Enter `Y` to authorize.
 - This will create a virtual environment and download required packages.
### 9. Enjoy the game.
![farming_game.sh Initial screen](/docs/step_9.png)
***
## Guidance for Mac users
*Note: Step1 and 2 guidences are referenced from [here](https://edstem.org/au/courses/9040/lessons/24154/slides/170970).*
### 1. Go to your terminal and install xcode by running this command.
```
xcode-select --install
```
### 2. Click install and accept license agreement.
### 3. Install Homebrew.
*Note: Step3 ~ step5 guidences are referenced from [here](https://edstem.org/au/courses/9040/lessons/24154/slides/170971).*
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
 -Press enter to contiue when prompted.
 ### 4. Install tldr by running following command.
 ```
 brew install tldr
 ```
 ### 5. Go to Guidance for Windows users and follow the steps from 4.
 #### **Note: When 'ubuntu' is mentioned, apply the same command to your terminal.**
<!-- fruit farm: https://unsplash.com/photos/0zpoa3TacEo
grain farm:https://unsplash.com/photos/0zpoa3TacEo
house : https://unsplash.com/photos/Q27HmRKdHPQ
landing : 
 -->