from os.path import exists
import json
import random


if exists("save.json") == False:
  Name = input("What is your name? = ")
  Class = input("Hi! "+Name+" What class would you like to be?\narcher\nknight\nmage\n").lower()
  if Class == "knight":
    hand = "Sword"
    offhand = "Shield"
  if Class == "archer":
      hand = "Bow"
  offhand = ""
  if Class == "mage":
    hand = "Staff"
    offhand = ""
    
  data = {
  "Name" : Name,
  "Class" : Class,
  "Hand" : hand,
  "Offhand": offhand,
}
  def firstsave():
  
      with open("save.json", "w") as write_file:
          json.dump(data, write_file)
  firstsave()
  






print("Welcome", Name, "I dont really know what this is lol")

ans = input ("there are two trolls, they are talking and you over hear their names one is called  Matthew and one Mackenzie\nWhat do you do?")

if ans == "attack":
  dmg = random.randint(0,11)
  print("you dealt",dmg, "damage with your",hand)
  
if dmg <= 2:
  dmg = random.randint(0,11)
  print("The troll didn't even flinch!", "and attacks you for", dmg, "hp")
if dmg >= 7:
  dmg = random.randint(0,11)
  print("the troll stumbles backwards", "but attacks back for", dmg, "hp")
  
  


