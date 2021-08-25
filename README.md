# Adventure
A sample python text adventure game that allow user move through rooms and locations in search of trials and tribulations to overcome (for fun and profit).

run program by following command
```
  python3 simulation.py conf/path.txt conf/item.txt conf/quest.txt
```
format:
```
  python3 simulation.py path_config item_config quest_config
```

## Tests
A brief testcase description is inside the **tests** folder  
Run following commnd to test the program
```
  bash test.sh
```

## Config file
sample config files are located in **conf** folder

**path_config** - the path of a file containing the list of all connections between rooms in the program.
Use this file to determine how many Room objects you have to create! Each line is of the form:
```
  START > DIRECTION > DESTINATION
```
**item_config** - the path of a file defining all the items to be found in the adventure on each line. Each
line is of the form
```
  item_name | shortname | skill_bonus | will_bonus
```
**quest_config** the path of a file defining all of the quests to be completed throughout the course of the
game. Each line is of the form:
```
Reward | quest action | quest description | before_text | after_text | requirements |
fail_message | pass_message | room
```

## Game command

### Quit
At any point, the user may end the simulation  
### Help
list all valid commands and their usage 
```
HELP - Shows some available commands.
LOOK or L - Lets you see the map/room again.
QUESTS - Lists all your active and completed quests.
INV - Lists all the items in your inventory.
CHECK - Lets you see an item (or yourself) in more detail.
NORTH or N - Moves you to the north.
SOUTH or S - Moves you to the south.
EAST or E - Moves you to the east.
WEST or W - Moves you to the west.
QUIT - Ends the adventure.
```
### Look or L
Displays the room that you are currently in
example:
```
>>> LOOK
+---------NN---------+
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    | 
+--------------------+
You are standing at the Entrance.
There is nothing in this room.
```
### QUESTS
show the list all quests in  the game
### INV
Shows a printout of the user's inventory
### CHECK
Allows the user to examine items. it will ask them for a second input, which can be an item's name or its short name
### NORTH or N | SOUTH or S | EAST or E | WEST or W
Moves the user to a connecting room in that specified direction


