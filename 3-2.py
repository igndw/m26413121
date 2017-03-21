#!/usr/bin/python

class Critter(object):
 def __init__(self, name):
   print "Buat karakter baru"
   self.__name = name
 def __str__(self):
   rep = "Critter object\n"
   rep += "name : " + self.__name + "\n"
   return rep
 def talk(self):
   print "\n Hi, aku kelas critter\n"
 def get_name(self):
   return self.__name
 def set_name(self,new_name):
   if new_name == "":
      print "Kosong"
   else:
      self.__name = new_name
      print "Nama berubah"

crit1 = Critter("Dan")
crit1.talk()
crit2 = Critter("Andy")
crit2.talk()

print crit1
crit = Critter("Misal")
print crit.get_name()
crit4 = Critter("Yes")
print crit.set_name("")
print crit.set_name("Yes")
print crit.get_name()
