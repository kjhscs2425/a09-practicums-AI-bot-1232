import turtle
from turtle import *

P1 = str("costumes") 
P2 = str("Scennery")
P3 = str("Lighting") 
P4 = str("Sound") 

def choose_practicum():
 option = input ("which practium are you choosing")

 if option == P1:
  return("success, you slected {P1}")
 elif option == P2:
  return("success, you selected {P2}")
 elif option == P3:
  return("success, you selected {P3}")
 elif option == P4:
  return("success, you selected {P4}")
 else: 
  choose_practicum()
  print("Invalid choice. Please try again.")
  return choose_practicum()
 
def main_function():
  name = str ("what is your name")
  choose_practicum (str("which practium are you signing with"))
  print ("congragrlation")
print("great job/ congragulation")





def square():
    for I in range():
        forward(100)
        right(90)

square(1000)