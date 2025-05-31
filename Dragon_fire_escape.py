print(r'''
                      ___====-_  _-====___
                _--^^^#####//      \\\\#####^^^--_
             _-^##########// (    ) \\\\##########^-_
            -############//  |\\^^/|  \\\\############-
          _/############//   (@::@)   \\\\############\\_
         /#############((     \\\\//     ))#############\\
        -###############\\\\    (oo)    //###############-
       -#################\\\\  / "" \\  //#################-
      -###################\\\\/  (_) \\/###################-
     _#/|##########/\\######(   "/"   )######/\\##########|\\#_
     |/ |#/\\#/\\#/\\/  \\#/\\##\\  ! ' !  /##/\\#/  \\/\\#/\\#/\\| \\ 
     ||/  V  V '     V  \\\\#\\   ===   /#/  V     '  V  V  \\||
     ||| \\ \\|  |  | |  |\\\\\\|  (___)  |/||  | | |  |  | |/ || 
     |||  |_|_|_|_|_|_|__||_________|_||__|_|_|_|_|_|_|__||| 
     ||\\_/                            /_/                 |||
     ||        D R A G O N   F I R E        ESCAPE        |||
     ||___________________________________________________|||
     |_____________________________________________________|
==================== INSTRUCTIONS ====================

Welcome, brave hero!

You have awakened inside a mysterious dungeon guarded by
a fearsome dragon. To escape, you must choose wisely
at every turn. Your fate depends on your decisions!

>> HOW TO PLAY:
 - You will be presented with choices (1, 2, etc.).
 - Type the number of your choice and press Enter.
 - Some paths lead to safety... others to doom.

>> OBJECTIVE:
 - Escape the dungeon alive.
 - Avoid the dragon’s wrath.
 - Solve puzzles and make the right choices.

>> CONTROLS:
 - Enter 1 or 2 when prompted.
 - Read carefully before choosing.
 - There is no going back!

Good luck, warrior. May your choices lead you to freedom!

=======================================================
               
      ''')

print(" You wake up inside a cold," \
"dark dungeon. ")
choice1 = input('You\' see two doors in front of you.\n' \
'1. Open the wooden door\n' \
'2. Open the metal door\n' \
'type "1" or "2".\n')

if choice1 == "1":
    print(" You slowly open the creepy wooden door ..." \
    "Inside, you find a giant dragon sleeping!")
    choice2 = input("What will you do next?\n"
                "1. Attack the dragon with a broken sword\n"
                "2. Sneak past the dragon\n" 
                "Enter your choice (1 or 2): ")


    if choice2 == "2": # type: ignore
        print(" You tiptoe quietly...\n" \
        "The dragon snores loudly but doesn't wake up.\n" \
        "You find a glowing key and a hidden passage.\n" \
        "You ESCAPE safely. 🗝️ 🎉\n")

    else:
        print("You charge at the dragon with the broken sword...\n" \
        "Its eyes open. It roars and breathes fire!\n" \
        "You are burned to ashes. GAME OVER. 💀\n")

else:
    print(" A loud beep sounds. Poisonous gas fills the room...\n" \
    " You cough and fall to the floor. GAME OVER. 💀 \n")