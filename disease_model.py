# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:16:57 2018

@author: kate
"""
#Import a module which generates random numbers.
import random
import csv

#Importing the GUI
from tkinter import *
import tkinter as Tk

#Importing the matplotlib modules draw the graphs in a GUI.
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2TkAgg)
from matplotlib.figure import Figure

#Importing the disease module.
import disease_module as pilot



#Setting up the starting conditions.

#Getting the user to enter a valid entry for the percentage adults vaccinated.
#Creates an infinte loop until broken by the continue command.
while True:
    #Try this.
    try:
        #Get user to input value.
        print("What percentage of adults are vaccinated in this model?")
        adult_vaccination = int(input("Enter a number between 1 and 100?:"))
        #If they suggest a number that is too high or low.
        if adult_vaccination < 0 or adult_vaccination > 100:
            print("That is not a valid entry")
            adult_vaccination = int(input("Enter a numer"))
            continue
        #If a valid entry has been entered break out of the while loop.
        else:
            break 
    #If get an error trying the above, do this.         
    except ValueError as Val:
        #Inform user and write error messages to file.
        print("That value is not valid. The value must be a number.")
        print("Error message")
        print(ValueError)
        print(Val)
        continue
    #If entry is correct, break out of while loop.
    else:
        break
    
#Getting the user to enter a valid entry for the percentage children vaccinated.
#Creates an infinte loop until broken by the continue command.
while True:
    #Try this.
    try:
        #Get user to input value.
        print("What percentage of children are vaccinated in this model?")
        child_vaccination = int(input("Enter a number between 1 and 100?:"))
        #If they suggest a number that is too high or low.
        if child_vaccination < 0 or child_vaccination > 100:
            print("That is not a valid entry")
            child_vaccination = int(input("Enter a numer"))
            continue
        #If a valid entry has been entered break out of the while loop.
        else:
            break 
    #If get an error trying the above, do this.         
    except ValueError as Val:
        #Inform user and write error messages to file.
        print("That value is not valid. The value must be a number.")
        print("Error message")
        print(ValueError)
        print(Val)
        continue
    #If entry is correct, break out of while loop.
    else:
        break


def writeresults(data):
    """
    Writes data to a csv file
    
    Positional arguements:
    data -- the information to be printed out in a list form (no default)
    
    Returns:
    The information added to the csv file.
    """
    #Opens the file in a way so file closes if system crashes, or forget to close.
    #Appends the results to the data in the file.
    with open('disease_results.csv', 'a', newline='') as f: 
        #Delimits with a comma so data can be analysed in excel (amongst other programs).
        writerx = csv.writer(f, delimiter=',')
        #Writes the data to a file. 
        writerx.writerow(data)    
        #Closes the file.
    f.close()
    
    
#Writes to the file that a new version of the model is being run.
writeresults(["Starting a new model run"])
writeresults(["Percentage of adults vaccinated", adult_vaccination])
writeresults(["Percentage of children vaccinated", child_vaccination])

#Setting up the lists of people to go into the model.

#Whether the agents start in contact with eachother.
#Should be set to no.
contact = "no"

#List to store all the people in the population.
people = []

#Creating the people in family units.
family = []

#Create a family with an infected person.
family.append(pilot.Person0(contact))
family.append(pilot.Human(contact, adult_vaccination))
#second vairable below might want to be set to 0, otherwise disease might not spread
#in a run if the other adult and both children in this family happen to be immune.
family.append(pilot.Child(contact, 1))
family.append(pilot.Child(contact, child_vaccination))

#Add the family to the list of people.
people.append(family)


#Create 20 other families with 2 adults and 2 children.
for s in range(20):
    family = []
    family.append(pilot.Human(contact, adult_vaccination))
    family.append(pilot.Human(contact, adult_vaccination))
    family.append(pilot.Child(contact, child_vaccination))
    family.append(pilot.Child(contact, child_vaccination))
    #Store them in people as a double list of family units within a population.
    people.append(family)
    
    
#Create 3 nurseries.
nursery1 = []
nursery2 = []
nursery3 = []

#Loop through all the families in the list.
#for i in people would be better for this in some ways
#but wouldn't give me a number to assign nurseries so hasn't been used.
for i in range(len(people)):
    #Extract the children
    a = people[i][2]
    b = people[i][3]
    #Assign them to a nursery based on an algorithm.
    if i % 3 == 0:
        nursery1.append(a)
        nursery1.append(b)
    elif i % 2 == 0:
        nursery2.append(a)
        nursery2.append(b)
    else:
        nursery3.append(a)
        nursery3.append(b)
        
#Create 2 workplaces
workplace1 = []
workplace2 = []
for i in range(len(people)):
    a = people[i][0]
    b = people[i][1]
    #I could randomly assign them to workplaces but the random number generator
    #seems to mean that there is an imbalance between the number of people in 
    #each workplaces.
    #Therefore adult a for each family is distributed between workplaces.
    #and adult b is randomly assigned.
    if i % 2 == 1:
        workplace1.append(a)
    else:
        workplace2.append(a)
    c = random.randint(0,1)
    if c == 0:
        workplace1.append(b)
    elif c == 1:
        workplace2.append(b)
    #Check in place in case the random generator doesn't work properly.
    else:
        print("Error")
 
    
    
    
#Running the main part of the model.
       
#Model starts with someone being infected (2). So everyone infected is set at 2.  
everyoneinfected = 2

#Day number
day = 1

#List to store the number of people that are infectious each day.
infected_y = []

#Set up the columns of the results.
writeresults(["Day", "Nursery 1", "Nursery 2", "Nursery 3", "Workplace 1", "Workplace 2", "Total"])

#Determining how many days it takes until no one is infected.
while everyoneinfected == 2:

    #Running through a day of the simulation.
    #This allows people to move about thier environment and giving them the
    #opportunity to become infected.
    
    #In this model it's harder for families to infect eachother as they are further apart
    #so I have given them 3 tries to do so.
    for j in range(3):
        #Go through all the families
        for i in people:
            #And give them the opportunity to become infected, by all the other members.
            pilot.Infection(i, contact).update(i, contact)

    
    #People go to work or nursery and get infected there.
    n1 = pilot.Infection(nursery1, contact).update(nursery1, contact)
    n2 = pilot.Infection(nursery2, contact).update(nursery2, contact)
    n3 = pilot.Infection(nursery3, contact).update(nursery3, contact)
    w1 = pilot.Infection(workplace1, contact).update(workplace1, contact)
    w2 = pilot.Infection(workplace2, contact).update(workplace2, contact)
    
    #This isn't neccessary but just illustrates how the data could be visualised.
    #Helps check it's working properly.
    pilot.Infection(workplace2, contact).image(workplace2, contact)
            
    #Making a single list of the status of all the people
    infectionstatus =[]
    for i in n1:
        infectionstatus.append(i)
    for i in n2:
        infectionstatus.append(i)
    for i in n3:
        infectionstatus.append(i)
    for i in w1:
        infectionstatus.append(i)
    for i in w2:
        infectionstatus.append(i)
    
    #List of total infectious at each place.
    writeresults([str(day), n1.count(2), n2.count(2), n3.count(2), w1.count(2), w2.count(2), infectionstatus.count(2)])
           
    #If even one person is infecious this will come back as 2.
    everyoneinfected = max(infectionstatus)
    
    #Counts the number of 2 values in the list.
    number_infected = infectionstatus.count(2)
    #Increment the day by 1.
    day +=1
    #Adds to the list of number that are infectious each day.
    infected_y.append(number_infected)
    
    #This can be used if you want to see a particular workplace and how the disease spreads each day.
    #pilot.Infection(workplace1, contact).image(workplace1, contact)


    
#GUI code

#Setting up the GUI window.
root = Tk.Tk()
#Naming the GUI.
root.title("Disease model")
#Setting the GUI size
root.geometry("600x600")

app = Frame(root)
app.grid()
fig = Figure(figsize=(5, 4), dpi=100)


"""
Getting the graph to print in the canvas was achieved by altering and condensing the code 
below in this comment.
edited from code found here: https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_sgskip.html
from six.moves import tkinter as Tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2TkAgg)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from six.moves import tkinter as Tk

import numpy as np


root = Tk.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = Tk.Button(master=root, text="Quit", command=_quit)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
"""
def createGraph(adult_vaccination, child_vaccination, infected_y):
    lbl = Label(text = "A model simulating disease spread under differing percentages of starting child and adult immunity", wraplength=400)
    lbl.grid(row = 0, sticky = N)
    lbl2 = Label(text = "The percentage of adults vaccinated is: " + str(adult_vaccination))
    lbl2.grid(row = 1, sticky = N)
    lbl2 = Label(text = "The percentage of children vaccinated is: " + str(child_vaccination))
    lbl2.grid(row = 2, sticky = N)

    """Creates a graph showing how the infection spreads through time"""
    #Sets up the size of the canvas.
    d = Tk.Canvas(app, width=50, height=50)
    #Gives the location of the canvas.
    d.grid(row = 3, column = 0)    
    c = infected_y
    a = []
    for i in range(len(c)):
        a.append(i)
    fig = Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).plot(a, c)
    canvas = FigureCanvasTkAgg(fig, master = app)
    canvas._tkcanvas.grid(row = 4, column = 0)
    
    canvas.get_tk_widget().grid(row = 5, column = 0)
    canvas._tkcanvas.grid(row = 4, column = 0)
    canvas.show()


def quit_method():
    """Closes window when QUIT is clicked"""
    fig.clear()
    lbl = Label(text = "quit program")
    lbl.grid(row = 0, sticky = W)
    #Creates a button, which when pressed closes the GUI window.
    QUIT = Button(app, text = "QUIT", command = root.destroy)
    #Positions the button on the window.
    QUIT.grid(row = 0, column = 0)
  
    
#Menus
    
#Sets up menu items. Giving the user a choice parts of the software to use.
menu_bar = Tk.Menu(app)
root.config(menu=menu_bar)

#Creating menus.
graph_menu = Tk.Menu(menu_bar)
#write_menu = tkinter.Menu(menu_bar)
quit_menu = Tk.Menu(menu_bar)

#Naming the menu options.

menu_bar.add_cascade(label="show", menu=graph_menu)
#menu_bar.add_cascade(label="write", menu=write_menu)
menu_bar.add_cascade(label="quit", menu=quit_menu)

#Creating the drowdown options and assigning commands to them.
graph_menu.add_command(label = "show graph", command=createGraph(adult_vaccination, child_vaccination, infected_y))

#write_menu.add_command(label = "store", command=write_store)
quit_menu.add_command(label = "quit program", command=quit_method)


Tk.mainloop()

print("Finished running")

