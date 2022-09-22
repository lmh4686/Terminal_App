## Project Overview
### [Github repository](https://github.com/lmh4686/Terminal_App)
### [PEP8](https://peps.python.org/pep-0008/) style has been applied for this project.
### Main features
 1. `def cook()`
***
###
## Game introdution 
### This farming game is inspired from [Minecraft](http://minecraft.net/minecraft).
***
## Installation guidance
## This program is designed for windows users only.
### 1. Install [Window Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-au&gl=au)
### 2. Install [Ubuntu 22.04.1 LTS](https://apps.microsoft.com/store/detail/ubuntu-22041-lts/9PN20MSR04DW?hl=en-au&gl=au)
### 3. Enable the optional feature from PowerShell
```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
 - This will restrart your computer.
This guidance is originally posted on [HERE](https://janelbrandon.medium.com/a-guide-for-using-wsl-for-development-d135670313a6).
<!-- ### 3. Install [Python 3.10](https://www.python.org/downloads/)
#### In your ubuntu, apply this code one by one to install Python: -->
### 4. Install [Python 3](https://www.python.org/downloads/) by applying code below to ubuntu.
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
### 6. Direct to [src](src) folder.
```
cd Terminal_App/src
```
### 7. Excecute the program.
```
./farming_game.sh
```
### 8. Authorise the program to activate Virtualenv and download packages.
![farming_game.sh Initial screen](/docs/step_8.png)  
 - Enter `Y` to authorize.
 - This will create a virtual environment and download required packages.
### 9. Enjoy the game.
![farming_game.sh Initial screen](/docs/step_9.png)  
<!-- fruit farm: https://unsplash.com/photos/0zpoa3TacEo
grain farm:https://unsplash.com/photos/0zpoa3TacEo
house : https://unsplash.com/photos/Q27HmRKdHPQ
landing : 
 -->