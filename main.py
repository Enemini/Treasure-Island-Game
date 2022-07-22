print('''
*******************************************************************************
               __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/'
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
cross_road = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'.\n")

if cross_road.lower() == "left":
  cross_lake = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
  if cross_lake.lower() == "wait":
    which_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    if which_door.lower() == "yellow":
      print("You Win")
    elif which_door.lower() == "red":
      print("Burned by fire. Game Over")
    elif which_door.lower() == "blue":
      print("Eaten by beasts. Game Over")
  else:
    print("Attacked by trout. Game Over")
else:
  print("Fall into a hole. Game Over")