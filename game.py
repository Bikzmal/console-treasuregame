# Required modules for this program to work
import os
import sys
import time
import random

# Install and import keyboard module
imported = False
for _ in range(5):
    try:
        import keyboard
        imported = True
        break
    except:
        if os.name in ('nt', 'dos'):
            os.system(f"py -{sys.version_info.major}.{sys.version_info.minor} -m pip install keyboard")
        else:
            os.system(f"sudo py -{sys.version_info.major}.{sys.version_info.minor} -m pip install keyboard")

# Exit program if import failed
if not imported:
    print("Import failed! Please try running again.")
    exit()

# Get player input for customizing the game
player = input("Player head: ")
playerwin = input("Player head when win: ")
goal = input("Goal character: ")
tile = input("Tile character: ")
while True:
    try:
        size = int(input("Field size: "))
        if size < 3 or size > 10:
            print("Size must be between 3 and 10")
        else:
            break
    except:
        print("Please enter an integer value.")

# Initializing the player coords and the goal coords
playerx = 0
playery = 0
goalx = random.randint(2, size-1)
goaly = random.randint(2, size-1)

# Function for printing the field
def printfield(matrix):
    for i in matrix:
        for j in i:
            print(j, end='')
        print()

# Initializing the field
field = [[tile for i in range(size)] for i in range(size)]
field[goaly][goalx] = goal

# Clear command for clearing console every loop
clearcommand = "cls" if os.name in ('nt', 'dos') else "clear"

# Main game loop
while True:
    # Moves player to their coords
    field[playery][playerx] = player
    
    printfield(field)

    # Checking if keys are being pressed
    if keyboard.is_pressed('d'):
        # Moving the player if player is not at border
        if playerx != len(field[0])-1:
            field[playery][playerx] = tile
            playerx += 1
            time.sleep(0.15)
    if keyboard.is_pressed('a'):
        if playerx != 0:
            field[playery][playerx] = tile
            playerx -= 1
            time.sleep(0.15)
    if keyboard.is_pressed('s'):
        if playery != len(field[0])-1:
            field[playery][playerx] = tile
            playery += 1
            time.sleep(0.15)
    if keyboard.is_pressed('w'):
        if playery != 0:
            field[playery][playerx] = tile
            playery -= 1
            time.sleep(0.15)
    
    # Checks if player is on the goal
    if playerx == goalx and playery == goaly:
        field[playery][playerx] = playerwin
        os.system(clearcommand)
        printfield(field)
        break
    
    # Clears console
    os.system(clearcommand)

# Win dialogue
print("You win!")
input()