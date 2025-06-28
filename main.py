# This program is a game where the user chooses their own path
# Author: Waed Yasser
# Date: 22/11/2019
# verison 1.0

# Importing modules
from tkinter import *
from tkinter import messagebox 
from playsound import playsound
import random
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Creating a class to store all the similar functions in
class Application():

    # Creating an initialize function that starts without getting called
    def __init__(self , master):

        # Creating the first frame
        frame = Frame(master)
        frame.grid()

        # Setting variables 
        self.health = 2
        self.shovelOn = 0
        self.phoneOn = 0
        self.visible = True
        self.seconds = 0
        self.umbrellaOn = 0
        self.kniveOn = 0
        self.path = 1
        self.shotgunOn = 0
        self.hit = 0
        self.characterError = True
        self.path3 = 0

        openingFrame = Button(frame , image = welcome , command = self.welcome).grid()

    #This function represents the character in the bottom middle of the screen and the items on the bottom left
    def sprite(self):

        bottomFrame = Frame(root)
        bottomFrame.grid(columnspan = 2 , row = 3)

        # Create the canvas to draw the character, rectangles and items in
        canvas = Canvas(bottomFrame, width = 700 , height=50 , bg = "black")
        canvas.grid() 
 
        #gets the variable of thr radio buttons, to draw the character
        char = self.spriteVar.get()

        if char == "1":
            image = canvas.create_image(350, 30,  image = male)

        elif char == "2":
            image = canvas.create_image(350, 30,  image = female)
        
        elif char == "3":
            image = canvas.create_image(350, 30,  image = female2)

        elif char == "4":
            image = canvas.create_image(350, 30,  image = character)
        else:
            messagebox.showwarning("Error" , "Please choose a Character") #If a character is not shown a error message is shown
            self.welcome()

        x = 20 #The rectangle position on the screen (x-axis)
        y = 45 #The rectangle position on the screen (y-axis)
        width = 50 #The width of the rectangle
        height = 15 #The height of the rectangle

        #The positions of the items on the screen
        itemsPosX = 35 
        itemsPosY = 30

        #inventory
        #First a rectangle is drawn, then a torch is added on top of it
        rectangle = canvas.create_rectangle(x , y , width , height , width = 2 , outline = "#FFFF00" )
        torch1 = canvas.create_image(itemsPosX , itemsPosY , image = torch)

        """There are 3 different paths that can collect more than one item, to arrange the items beside each other 
        , not on top of each other, I created variables for path and each time the user crosses a path, the variable increases"""


        if self.path == 1:
            if self.kniveOn == 1:
                knive = canvas.create_image(itemsPosX + 70, itemsPosY , image = kniveImg)
                rectangle = canvas.create_rectangle(x + 100 , y  , width , height , width = 2 , outline = "#FFFF00" )

            if self.umbrellaOn == 1:
                umbrella = canvas.create_image(itemsPosX + 35 , itemsPosY , image = umbrellaImg)
                rectangle = canvas.create_rectangle(x + 65 , y  , width , height , width = 2 , outline = "#FFFF00" )


            if self.phoneOn == 1:
                phone = canvas.create_image(itemsPosX + 35 , itemsPosY , image = phoneImg)
                rectangle = canvas.create_rectangle(x + 65 , y  , width , height , width = 2 , outline = "#FFFF00" )

            if self.shovelOn == 1:
                shovel = canvas.create_image(itemsPosX + 35 , itemsPosY , image = shovelImg)
                rectangle = canvas.create_rectangle(x + 65 , y  , width , height , width = 2 , outline = "#FFFF00" )

            if self.shotgunOn == 1:
                shotgun = canvas.create_image(itemsPosX + 35 , itemsPosY , image = shotgunImg)
                rectangle = canvas.create_rectangle(x + 65 , y  , width , height , width = 2 , outline = "#FFFF00" )

        if self.path == 2:
            if self.kniveOn == 1:
                knive = canvas.create_image(itemsPosX + 105, itemsPosY , image = kniveImg)
                rectangle = canvas.create_rectangle(x + 135 , y  , width , height , width = 2 , outline = "#FFFF00" )

            if self.umbrellaOn == 1:
                umbrella = canvas.create_image(itemsPosX + 70 , itemsPosY , image = umbrellaImg)
                rectangle = canvas.create_rectangle(x + 100, y  , width , height , width = 2 , outline = "#FFFF00" )


            if self.phoneOn == 1:
                phone = canvas.create_image(itemsPosX + 35 , itemsPosY , image = phoneImg)
                rectangle = canvas.create_rectangle(x + 65 , y  , width , height , width = 2 , outline = "#FFFF00" )

        if self.phoneOn == 1 and self.path3 == 1:
                shotgun = canvas.create_image(itemsPosX + 70 , itemsPosY , image = shotgunImg)
                rectangle = canvas.create_rectangle(x + 100 , y  , width , height , width = 2 , outline = "#FFFF00" )

        #The health bar
        if self.health == 2:
            healthBar2 = canvas.create_rectangle(650 , 20 , 680 , 10 , width=1 , fill = "#FF0000")
            healthBar = canvas.create_rectangle(650 , 20 , 680 , 10 , width=1 , fill = "#00ff00")

        elif self.health == 1:
            healthBar2 = canvas.create_rectangle(650 , 20 , 680 , 10 , width=1 , fill = "#FF0000")
            healthBar = canvas.create_rectangle(650 , 20 , 665 , 10 , width=1 , fill = "#00ff00")

        elif self.health <= 0:
            healthBar2 = canvas.create_rectangle(650 , 20 , 680 , 10 , width=1 , fill = "#FF0000")
            canvas.delete(image)
            image = canvas.create_image(350, 30,  image = rip)


    def welcome(self):

        #These variables are here to restore all the variables to their original values incase the user wanted to try again the game
        self.health = 2
        self.shovelOn = 0
        self.phoneOn = 0
        self.visible = True
        self.seconds = 0
        self.umbrellaOn = 0
        self.kniveOn = 0
        self.path = 1
        self.shotgunOn = 0
        self.hit = 0
        self.characterError = True
        self.path3 = 0
        playsound(resource_path('./assets/audio/music.mp3'), block=False)



        #Calling a function to remove the widgets in previous frames
        self.forgetFrames()

        frame = Frame(root).grid()


        list = ["You have 2 lives and a torch to start with. You will be collecting items to help you" , "It will be displayed in your inventory. Some decisions will take a life. Be careful." ,
                 "There's no going back. Choose wisely. Your character and inventory will be shown below" , "Click on the buttons below the image to choose your path"]

        Label(frame , text = "Welcome to Choose your own adventure game!" , font = ("Times New Roman" , "20") , bg = "black" , fg = "red" ).grid(columnspan = 2 , sticky = N + S + W + E)
        
        for text in list:
            Label(frame , text = text , font = ("Times New Roman" , "14") , bg = "black" , fg = "red" ).grid(sticky = W)
        Label(frame, image = exampleImg , bg = "black" , fg = "white" ).grid()
        
        Label(frame, text = "Choose your character" , font = ("Times New Roman" , "14") , bg = "black" , fg = "white" ).grid()


        #Radio Buttons representing the characters
        self.spriteVar = StringVar()
        Radiobutton(frame, image = male , variable = self.spriteVar , value = "1" , bg = "#000000").grid(sticky = W, row = 9)
        Radiobutton(frame, image = female , variable = self.spriteVar , value = "2" ,  bg = "#000000").grid(sticky = E , row = 9)
        Radiobutton(frame, image = female2 , variable = self.spriteVar , value = "3" ,  bg = "#000000").grid(sticky = W , row = 10)
        Radiobutton(frame, image = character , variable = self.spriteVar , value = "4" ,  bg = "#000000").grid(sticky = E , row = 10)

        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.first).grid( sticky = E)


#-------------------------------------------------------------- The story begins here -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
    def first(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()


        Label(frame , image = one).grid(column = 0 , row = 0)
        button1 = Button(frame , text = "Go through the haunted house?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.house).grid(column = 0 , row = 1 , sticky = W + E)

        Label(frame , image = two).grid(column = 1 , row = 0)
        button2 = Button(frame , text = "Go through the forest?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.left).grid(column = 1 , row = 1 , sticky = W + E)

        #All the upcoming functions will call the sprite function to display it in the bottom of the screen
        self.sprite()


 
    def house(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()


        frame = Frame(root).grid()


        Label(frame , image = three).grid(column = 0 , row = 0)
        Button(frame , text = "go upstairs?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.umbrella).grid(column = 0 , row = 1 , sticky = W + E)

        Label(frame , image = four).grid(column = 1 , row = 0)
        Button(frame , text = "go downstairs!" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.down).grid(column = 1 , row = 1 , sticky = W + E)
        
        self.sprite()



    def down(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        Label(frame , image = seventeen).grid(column = 0 , row = 0)
        Button(frame , text = "go to the basement?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.phone).grid(column = 0 , row = 1 , sticky = W + E)

        Label(frame , image = eighteen).grid(column = 1 , row = 0)
        Button(frame , text = "go to the light at the end of the hallway" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.hallway).grid(column = 1 , row = 1 , sticky = W + E)
        
        self.sprite()

    def hallway(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        Label(frame , image = twentyFour ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 0)
        Label(frame , text = "You step on  nails and get hurt, you lose a life" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1)
        Label(frame , text = "You end up at the back of the house and see a small town" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2)

        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.hutOrFurther).grid(column = 0 , row = 4 , sticky = E)

        #Health is reduced 
        self.health -= 1

        self.sprite()

    def hutOrFurther(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        Label(frame , image = twentyFive).grid(column = 0 , row = 0)
        Button(frame , text = "go inside the hut?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.hut).grid(column = 0 , row = 1 , sticky = W + E)

        Label(frame , image = twentySix).grid(column = 1 , row = 0)
        Button(frame , text = "go further in the town" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.further).grid(column = 1 , row = 1 , sticky = W + E)
        
        self.sprite()



    def further(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        Label(frame , image = twentyEight ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 0)
        Label(frame , text = "You hear creepy voices around you.. You attempt to run..." ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1)

        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.finalFrame).grid(column = 0 , row = 4 , sticky = E)


        self.sprite()



    def hut(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        Label(frame , image = twentySeven ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 0)
        Label(frame , text = "You find a shotgun! It has been added to your inventory" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1)
        Label(frame , text = "You then leave the hut" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2)

        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.finalFrame).grid(column = 0 , row = 4 , sticky = E)

        #The shotgun is now visible
        self.shotgunOn += 1
        self.path3 += 1

        self.sprite()



    def finalFrame(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        #There are 3 different combact in this game, this functions leads to the third combact
        self.hit += 3

        #If the shotgun is visible then appropriate text will be displayed
        frame = Frame(root).grid()
        if self.shotgunOn == 1:

            Label(frame , image = twentyNine ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 0)
            Label(frame , text = "You're suddenly surrounded by zombies" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1)
            
            self.scare1 = 0


            Button(frame , text = "You shot them with the shotgun?" ,   font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = lambda: self.dice("1")).grid(column = 0 , row = 2, sticky = W)
            Button(frame , text = "Scare them with the torch?" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = lambda: self.dice("0")).grid(column = 0 , row = 2, sticky = E)

        else:
            
            Label(frame , image = twentyNine ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 0)
            Label(frame , text = "You're suddenly surrounded by zombies" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1)
            Button(frame , text = "try to scare them with th torch?" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = lambda: self.dice("0")).grid(column = 0 , row = 2)

        self.sprite()



    def umbrella(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        Label(frame , image = thirtyTwo ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 0)
        Label(frame , text = "You find an umbrella!" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1)
        Label(frame , text = "It has been added to your inventory" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2)

        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.livingOrKitchen).grid(column = 0 , row = 4 , sticky = E)

        #The Umbrella is now visible
        self.umbrellaOn += 1

        self.sprite()



    def livingOrKitchen(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        Label(frame , image = twentyOne).grid(column = 0 , row = 0)
        Button(frame , text = "go to the living room?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.doll).grid(column = 0 , row = 1 , sticky = W + E)

        Label(frame , image = twentyTwo).grid(column = 1 , row = 0)
        Button(frame , text = "go to the kitchen?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.kitchen).grid(column = 1 , row = 1 , sticky = W + E)
        
        self.sprite()



    def kitchen(self):

        self.forgetFrames()

        frame = Frame(root).grid()

        #Health is reduced
        self.health -= 1

        Label(frame , image = thirty ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 0 , sticky = W + E)
        Label(frame , text = "On your way to the kitchen, you slip on water and get hurt!" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
        Label(frame , text = "You Lose a life" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)

        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.knive).grid(column = 0 , row = 4 , sticky = E)

        self.sprite()



    def knive(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        Label(frame , image = twentyThree ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 0 , sticky = W + E)
        Label(frame , text = "You find a knife! It has been added to your inventory" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
        Label(frame , text = "You try to leave the kitchen but you see the doll! It attacks you before you can move" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)

        #This function leads to the second combact
        self.hit += 2
        Button(frame , text = "Try to kill it with the knife?" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = lambda: self.dice("2")).grid(column = 0 , row = 4 , sticky = W)
        Button(frame , text = "Try to kill it with the umbrella?" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = lambda: self.dice("3")).grid(column = 0 , row = 4 , sticky = E)

        #The knife is now visible
        self.kniveOn += 1

        self.sprite()



    def doll(self):

        self.forgetFrames()
        frame = Frame(root).grid()

        Label(frame , image = twentyThree).grid(column = 0 , row = 0)
        Label(frame , text = "The door closes and a doll crawls to you, you hit it with the umbrella..." , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
        Label(frame , text = "But she hurts you so you lose a life, you then run to the kitchen" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)

        #Health is reduced
        self.health -= 1

        self.sprite()

        Label(frame , text = "Remember: Some decisions will cost you a life"  , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(row = 4 , sticky = W)
        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.knive).grid(row = 4 , sticky = E)



    def phone(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        Label(frame , image = thirtyThree ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 0)
        Label(frame , text = "You find a phone! Sadly, it doesn't have a battery" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1)
        Label(frame , text = "It has been added to your inventory" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2)

        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.upstairsOrHallway).grid(column = 0 , row = 4 , sticky = E)

        #The phone is now visible
        self.phoneOn += 1

        self.sprite()



    def upstairsOrHallway(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        #This function takes the user on the second path
        self.path += 1

        Label(frame , image = three).grid(column = 0 , row = 0)
        Button(frame , text = "go upstairs to look for battery?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.umbrella).grid(column = 0 , row = 1 , sticky = W + E)

        Label(frame , image = eighteen).grid(column = 1 , row = 0)
        Button(frame , text = "go back to the hallway?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.hallway).grid(column = 1 , row = 1 , sticky = W + E)
        
        self.sprite()



    def left(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        Label(frame , image = seven).grid(column = 0 , row = 0)
        Label(frame , text = "You keep walking until you see a lake with someone waving in the end" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1)

        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.swimOrRun).grid(sticky = E)



    def fallDown(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        self.health -= 1

        frame = Frame(root).grid()

        Label(frame , image = thirtyOne).grid(column = 0 , row = 0)
        Label(frame , text = "You fell!! You lost a life!!" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1)
        Label(frame , text = "You end up in a small town" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2)

        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.hutOrFurther).grid(row = 2, sticky = E)

        self.sprite()



    def swimOrRun(self):

        self.forgetFrames()
        frame = Frame(root).grid()

        Label(frame , image = eight).grid(column = 0 , row = 0)
        Button(frame , text = "Swim to the man?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.swim).grid(column = 0 , row = 1 , sticky = W + E)

        Label(frame , image = nine).grid(column = 1 , row = 0)
        Button(frame , text = "Run away?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.fallDown).grid(column = 1 , row = 1 , sticky = W + E)
        
        self.sprite()



    def swim(self):

        self.forgetFrames()
        frame = Frame(root).grid()

        Label(frame , image = ten).grid(column = 0 , row = 0)
        Label(frame , text = "a fish bites you! you lose a life." , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
        
        self.health -= 1

        self.sprite()

        Label(frame , text = "Remember: Some decisions will cost you a life"  , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(row = 4 , sticky = W)
        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.land).grid(row = 4 , sticky = E)



    def land(self):

        #calling the forgetFrames function to remove the previous frame
        self.forgetFrames()

        frame = Frame(root).grid()

        Label(frame , image = eleven).grid(column = 0 , row = 0)
        Label(frame , text = "as you land, you seeing the man holding a saw and is getting closer to you" ,  font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1)

        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.graveyardOrSwim).grid(sticky = E)



    def graveyardOrSwim(self):

        self.forgetFrames()
        frame = Frame(root).grid()


        Label(frame , image = twelve).grid(column = 0 , row = 0)
        Button(frame , text = "Run to a graveyard?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red", command = self.graveyard).grid(column = 0 , row = 1 , sticky = W + E)

        Label(frame , image = fish).grid(column = 1 , row = 0)
        Button(frame , text = "try to swim back?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.swim2).grid(column = 1 , row = 1 , sticky = W + E)
        
        self.sprite()



    def swim2(self):

        self.forgetFrames()
        frame = Frame(root).grid()

        #Creating a variable to store a random number from 0 to 5
        int = random.randint(0 , 5)

        odd = [1 , 3 , 5]

        #If the random number is an odd number, the user loses the game
        if int in odd:
            playsound(resource_path('./assets/audio/laugh.mp3'), block=False)

            Label(frame , image = gameOver).grid(column = 0 , row = 0)
            Label(frame , text = "A fish bites Again, you lose your second life" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
            self.health -= 1
            self.sprite()

            Button(frame , text = "Quit" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.closeWindow).grid(row = 4 , sticky = E)
            Button(frame , text = "Try again" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.welcome).grid(row = 4 , sticky = W)

        #if the random number is an even number the user wins
        else:

            Label(frame , image = houseImg).grid(column = 0 , row = 0)
            Label(frame , text = "You returned back safely" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
            Label(frame , text = "You find an apple and get your second life back" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
            Button(frame , text = "Go back to the house" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.house).grid(row = 4 , sticky = E)

            self.health += 1

            self.sprite()



    def graveyard(self):

        self.forgetFrames()
        frame = Frame(root).grid()

        #The shovel is now visible
        self.shovelOn += 1

        Label(frame , image = thirteen).grid(column = 0 , row = 0)
        Label(frame , text = "You find a shovel! It's been added to your inventory!" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
        Label(frame , text = "You hear steps behind you...." , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)

        self.sprite()

        Button(frame , text = "Next" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.turnOrRun).grid(row = 4 , sticky = E)



    def turnOrRun(self):

        self.forgetFrames()
        frame = Frame(root).grid()


        Label(frame , image = forteen).grid(column = 0 , row = 0)
        Button(frame , text = "Look behind you?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red", command = self.turnAround).grid(column = 0 , row = 1 , sticky = W + E)

        Label(frame , image = fifteen).grid(column = 1 , row = 0)
        Button(frame , text = "RUN!!!!" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = self.run).grid(column = 1 , row = 1 , sticky = W + E)
        
        self.sprite()



    def turnAround(self):

        self.forgetFrames()
        frame = Frame(root).grid()

        self.hit += 1

        Label(frame , image = sixteen).grid(column = 0 , row = 0)
        Label(frame , text = "You see the man!" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
        Button(frame , text = "hit him with the shovel?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = lambda: self.dice("4")).grid(column = 0 , row = 2 , sticky = W)
        Button(frame , text = "Scare him with the torch?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = lambda: self.dice("5")).grid(column = 0 , row = 2 , sticky = E)


        self.sprite()



    def run(self):

        self.forgetFrames()
        frame = Frame(root).grid()

        self.hit += 1

        Label(frame , image = sixteen).grid(column = 0 , row = 0)
        Label(frame , text = "You ran and suddenly see him standing in front of you!" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
        Button(frame , text = "hit him with the shovel?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = lambda: self.dice("4")).grid(column = 0 , row = 2 , sticky = W)
        Button(frame , text = "Scare him with the torch?" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red" , command = lambda: self.dice("5")).grid(column = 0 , row = 2 , sticky = E)

        self.sprite()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #The function that generates random numbers to deciede if the user will win or lose
    def dice(self , scare):


        self.forgetFrames()
        frame = Frame(root).grid()

        #Creating a variable to store a random number from 0 to 5
        int = random.randint(0 , 5)

        odd = [1 , 3]

        #If the random number is an odd number, the user wins the game
        if int in odd:
            playsound(resource_path('./assets/audio/winSound.mp3'), block=False)

            if self.hit == 1: #win
                if scare == "4":
                    Label(frame , image = win).grid(column = 0 , row = 0)
                    Label(frame , text = "You hit him with the shovel! But he's a nice guy and will help you out" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "You won!" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
                    self.sprite()

                if scare == "5":
                    Label(frame , image = win).grid(column = 0 , row = 0)
                    Label(frame , text = "You flash the torch in his face! But he's a nice guy and will help you out" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "You won!" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
                    self.sprite()

            elif self.hit == 2:
                if scare == "2":
                    Label(frame , image = win).grid(column = 0 , row = 0 , sticky = W + E)
                    Label(frame , text = "You hit it with the knife and kill it!" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "You find a phone and the charger call for help" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
                    self.sprite()

                if scare == "3":
                    Label(frame , image = win).grid(column = 0 , row = 0 , sticky = W + E)
                    Label(frame , text = "You hit it with the umbrella!" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "You find a phone and the charger so you call for help" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
                    self.sprite()

            elif self.hit == 3:
                if scare == "1":
                    Label(frame , image = win).grid(column = 0 , row = 0 , sticky = W + E)
                    Label(frame , text = "You try scaring with the shotgun!" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "They feel threatened which gives time to escape" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
                    self.sprite()

                if scare == "0":
                    Label(frame , image = win).grid(column = 0 , row = 0 , sticky = W + E)
                    Label(frame , text = "You try scaring with the torch!" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "They feel threatened which gives time to escape" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
                    self.sprite()


            Button(frame , text = "Quit" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.closeWindow).grid(row = 4 , sticky = E)
            Button(frame , text = "Try again" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.welcome).grid(row = 4 , sticky = W)

        # if the random number is an even number the user loses
        else: 
            playsound(resource_path('./assets/audio/laugh.mp3'), block=False)

            if self.hit == 1:
                if scare == "4":
                    Label(frame , image = gameOver).grid(column = 0 , row = 0)
                    Label(frame , text = "You hit him with the shovel! But he gets angry and kills you" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "Game over" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
               
                if scare == "5":
                    Label(frame , image = gameOver).grid(column = 0 , row = 0)
                    Label(frame , text = "You flash the torch in his face! But he gets angry and kills you" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "Game over" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
               

            if self.hit == 2:
                if scare == "2":
                    Label(frame , image = gameOver).grid(column = 0 , row = 0)
                    Label(frame , text = "You hit it with the knife! But it gets angry and kills you" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "Game over" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
            
                if scare == "3":
                    Label(frame , image = gameOver).grid(column = 0 , row = 0)
                    Label(frame , text = "You hit it with the umbrella! But it gets angry and kills you" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "Game over" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
 

            if self.hit == 3:
                if scare == "1":
                    Label(frame , image = gameOver).grid(column = 0 , row = 0)
                    Label(frame , text = "You try scaring with with the shotgun! But it does not work" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "Game over" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)
                if scare == "0":
                    Label(frame , image = gameOver).grid(column = 0 , row = 0)
                    Label(frame , text = "You try scaring with the torch! But it does not work" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 1 , sticky = W + E)
                    Label(frame , text = "Game over" , font = ("Times New Roman" , "16") , bg = "black" , fg = "red").grid(column = 0 , row = 2 , sticky = W + E)

                    
            self.health -= 1
            self.sprite()
            Button(frame , text = "Quit" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.closeWindow).grid(row = 4 , sticky = E)
            Button(frame , text = "Try again" , bg = "black" , fg = "red" , font = ("Times New Roman" , "14") , command = self.welcome).grid(row = 4 , sticky = W)

    #A function that delete whats in the previous frames 
    def forgetFrames(self):
        list = root.grid_slaves()
        for l in list:
            l.destroy()

    def closeWindow(self): 
        root.quit()
        root.destroy()







        

#The main window
root = Tk()

root.geometry("707x405")

root.title("Waed's Horror Adventure game")

root.configure(bg ="#000000")

#to aviod the user fromr resizing the window
root.resizable(False, False)




#Inserting the images used in the stories, characters and items
try:

    welcome = PhotoImage(file=resource_path("./assets/welcome.png"))
    one = PhotoImage(file=resource_path("./assets/1.png"))
    two = PhotoImage(file=resource_path("./assets/2.png"))
    three = PhotoImage(file=resource_path("./assets/3.png"))
    four = PhotoImage(file=resource_path("./assets/4.png"))
    five = PhotoImage(file=resource_path("./assets/5.png"))
    six = PhotoImage(file=resource_path("./assets/6.png"))
    seven = PhotoImage(file=resource_path("./assets/7.png"))
    eight = PhotoImage(file=resource_path("./assets/8.png"))
    nine = PhotoImage(file=resource_path("./assets/9.png"))
    ten = PhotoImage(file=resource_path("./assets/10.png"))
    eleven = PhotoImage(file=resource_path("./assets/11.png"))
    twelve = PhotoImage(file=resource_path("./assets/graveyard.png"))
    thirteen = PhotoImage(file=resource_path("./assets/13.png"))
    forteen = PhotoImage(file=resource_path("./assets/14.png"))
    fifteen = PhotoImage(file=resource_path("./assets/15.png"))
    sixteen = PhotoImage(file=resource_path("./assets/16.png"))
    seventeen = PhotoImage(file=resource_path("./assets/17.png"))
    eighteen = PhotoImage(file=resource_path("./assets/18.png"))
    nineteen = PhotoImage(file=resource_path("./assets/19.png"))
    twenty = PhotoImage(file=resource_path("./assets/20.png"))
    twentyOne = PhotoImage(file=resource_path("./assets/21.png"))
    twentyTwo = PhotoImage(file=resource_path("./assets/22.png"))
    twentyThree = PhotoImage(file=resource_path("./assets/23.png"))
    twentyFour = PhotoImage(file=resource_path("./assets/24.png"))
    twentyFive = PhotoImage(file=resource_path("./assets/25.png"))
    twentySix = PhotoImage(file=resource_path("./assets/26.png"))
    twentySeven = PhotoImage(file=resource_path("./assets/27.png"))
    twentyEight = PhotoImage(file=resource_path("./assets/28.png"))
    twentyNine = PhotoImage(file=resource_path("./assets/29.png"))
    thirty = PhotoImage(file=resource_path("./assets/30.png"))
    thirtyOne = PhotoImage(file=resource_path("./assets/31.png"))
    thirtyTwo = PhotoImage(file=resource_path("./assets/32.png"))
    thirtyThree = PhotoImage(file=resource_path("./assets/33.png"))
    rip = PhotoImage(file=resource_path("./assets/rip.png"))
    character = PhotoImage(file=resource_path("./assets/sprite.png"))
    torch = PhotoImage(file=resource_path("./assets/torch.png"))
    phoneImg = PhotoImage(file=resource_path("./assets/phone.png"))
    umbrellaImg = PhotoImage(file=resource_path("./assets/umbrella.png"))
    fish = PhotoImage(file=resource_path("./assets/fish.png"))
    shovelImg = PhotoImage(file=resource_path("./assets/shovel.png"))
    kniveImg = PhotoImage(file=resource_path("./assets/knive.png"))
    shotgunImg = PhotoImage(file=resource_path("./assets/shotgunImg.png"))
    gameOver = PhotoImage(file=resource_path("./assets/gameover.png"))
    win = PhotoImage(file=resource_path("./assets/win.png"))
    houseImg = PhotoImage(file=resource_path("./assets/house.png"))
    male = PhotoImage(file=resource_path("./assets/male.png"))
    female = PhotoImage(file=resource_path("./assets/female.png"))
    female2 = PhotoImage(file=resource_path("./assets/sprite1.png"))
    exampleImg = PhotoImage(file=resource_path("./assets/example.png"))

except:
    root.quit()


#assiging a variable for the class
a = Application(root)

#creating a loop to keep the window open
root.mainloop()


#https://www.fesliyanstudios.com/royalty-free-music/downloads-c/scary-horror-music/8 , music reference
#https://www.pinterest.com/pin/311029917993382389/?lp=true, welcome image
#https://www.google.com/search?q=forest+horror+cartoon+purple&tbm=isch&ved=2ahUKEwibu4rR0YHmAhWRIRQKHVx0AqsQ2-cCegQIABAA&oq=forest+horror+cartoon+purple&gs_l=img.3...234047.235380..235628...0.0..0.52.325.7......0....1..gws-wiz-img.......35i39.yjtpGm5Zd2U&ei=_NTZXZvNAZHDUNzoidgK&bih=608&biw=1280#imgrc=, image 2
#https://www.google.com/search?q=creepy+stairs+cartoon&tbm=isch&ved=2ahUKEwiAvoju3IHmAhUY0oUKHXl5A08Q2-cCegQIABAA&oq=creepy+stairs+cartoon&gs_l=img.3..0.25495.26445..26596...0.0..0.58.303.6......0....1..gws-wiz-img.......0i7i30j0i8i7i30.R4Oa1zQ4HEM&ei=weDZXcDZJJiklwT58o34BA&bih=608&biw=1263&sfr=vfe&hl=en#imgrc=Sc_Eh0fd3ikVvM , image 3
#https://www.google.com/search?q=creepy+forest+cartoon&tbm=isch&ved=2ahUKEwiUifKu3oHmAhWLYBQKHYNGD0IQ2-cCegQIABAA&oq=creepy+forest+cartoon&gs_l=img.3..0j0i5i30j0i8i30l3.196214.202869..203351...1.0..0.158.1161.20j1......0....1..gws-wiz-img.....10..35i362i39j35i39j0i67.8yvqQE2S8IA&ei=VeLZXdSKPIvBUYONvZAE&bih=608&biw=1280#imgrc=8PXXt1oYyqC2-M&imgdii=2QpyMl5bOYbN5M, image 5
#https://backgrounddownload.com/scary-cartoon-forest-background-2/, image 6
#https://www.pinterest.com/pin/725361083712470729/?lp=true, image 7
#http://www.themaineblog.com/night-swim-lake-megunticook/, image 8
#https://weheartit.com/entry/32634967, image 9
#https://brobible.com/sports/article/lake-trout-two-mouths-champlain-mutant-new-york/, image 10
#https://www.coastalfamilybible.org/pastor_s_pen/view/488/not_so_strange_times, image 11
#https://www.insidevancouver.ca/2011/09/03/3-creepy-alternative-tours-of-vancouver/, image 12
#https://gamedev.stackexchange.com/questions/127767/getting-sprites-from-a-spritesheet-with-rows-and-columns, character image
#https://www.google.com/search?q=torch&tbm=isch&hl=en&chips=q:torch,g_1:cartoon:nf1wzRQSPrQ%3D,g_1:light:nf1wzRQSPrQ%3D&tbs=ic:trans,isz:i&sfr=vfe&hl=en&ved=2ahUKEwjZid-x-4PmAhXP8IUKHXPeCvkQ4lYoBnoECAEQIg&biw=1263&bih=608#imgrc=vuu5UbUQhJg3MM, torch image
#http://lofigunandgame.com/beginners-guide-to-ice-fishing-ice-fishing-for-brook-trout/, fish image
#https://icon-library.net/icon/shovel-icon-3.html, shovel image
#http://zetcode.com/tkinter/drawing/
#https://www.python-course.eu/tkinter_canvas.php
#https://www.reddit.com/r/bindingofisaac/comments/celrif/characters_sprite_remake_as_ive_been_having/ , sprites images
#https://wallpapercave.com/creepy-background
#https://imgflip.com/memetemplate/83631149/Zombies-surrounded
#https://www.iconfinder.com/icons/1743644/cartoon_gun_hunter_rifle_shotgun_war_weapon_icon
#https://tralfaz.blogspot.com/2016/03/tex-avery-nails-it.html
#https://kissclipart.com/kitchen-knife-clipart-utility-knives-knife-kitchen-f546xt/
#https://www.roblox.com/games/1286071228/creepy-doll
#https://photorator.com/photo/60488/a-kitchen-stuck-in-time-inside-an-abandoned-house-in-ontario-canada-oc-x
#http://www.iconarchive.com/show/free-flat-sample-icons-by-thesquid.ink/umbrella-icon.html
#https://www.iconfinder.com/icons/2329867/cartoon_cell_mobile_phone_smart_smartphone_tablet_icon
#https://www.google.com/search?q=hallway+creepy+cartoon&tbm=isch&ved=2ahUKEwiRupPu9YbmAhUyEGMBHTHFA4UQ2-cCegQIABAA&oq=hallway+creepy+cartoon&gs_l=img.3..0i8i30.980.4409..4705...0.0..0.51.678.15......0....1..gws-wiz-img.......0i67j0.jx7ZdlgsUhY&ei=D5rcXdH2FbKgjLsPsYqPqAg&bih=608&biw=1280#imgrc=pRWXmdkWqdNDSM
#https://www.redbubble.com/people/chocodole/works/32320243-game-over-pixel-font-with-gradient?p=poster
#https://stackabuse.com/introduction-to-phaser-3-building-breakout/
#https://icons-for-free.com/death+grave+rip+stone+icon-1320168093746242927/
#https://nexter.org/the-nun-extremely-creepy-unknown-facts-movie-filming-give-you-heebie-jeebies
#https://www.youtube.com/watch?v=57o-tpONFLo
#https://stream.org/time-men-church-man/
#https://www.google.com/search?q=empty+forest+at+night&tbm=isch&ved=2ahUKEwiYuc3x0IbmAhXG2eAKHZpmCG8Q2-cCegQIABAA&oq=empty+forest+at+night&gs_l=img.3..0.5367.8526..8854...1.0..0.48.488.11......0....1..gws-wiz-img.......0i7i30j0i8i7i30.Brg2thfwiaU&ei=SnPcXZjsHcazgweazaH4Bg&bih=608&biw=1280#imgrc=lpvCZTx3bjcHvM&imgdii=gU6_e3x4nBjfVM
#https://www.iconninja.com/shovel-icon-252681
#https://waterextractionexperts.com/refrigerator-leaking-water-help-is-on-the-way/
#https://www.istockphoto.com/gb/illustrations/woman-falling-down-stairs
#https://www.cultofmac.com/577293/phone-xs-nfc-express-card-dead-battery/
#https://www.kissclipart.com/umbrella-on-white-background-clipart-umbrella-clip-f9hfw0/
#https://www.freesoundeffects.com/free-sounds/scary-laugh-10091/
#http://soundbible.com/1823-Winning-Triumphal-Fanfare.html
