#!/usr/bin/python
print "Tuple\n"
inventory = ()

if not inventory:
 print "You are empty handed"
raw_input("\nPress the enter key to continue.")

inventory = ("apples", "blueberry", "helmet", "potion")

print "\n the tuple inventory is : \n", inventory

print "\nYour item is here : "
for item in inventory:
 print item

print "You have", len(inventory), "items\n"
if "potion" in inventory:
 print "There is potion\n"
else:
 print "No potion\n"
if "drugs" in inventory:
 print "Drunken\n"
else:
 print "Super B\n"

raw_input("\n Press enter key to exit : ")
