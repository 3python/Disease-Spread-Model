# -*- coding: utf-8 -*-
"""
Created on Sun May  6 08:53:37 2018

This project is loosely based on an agent based model practical for the core 
programming module. Both models take in agents and get them to move
around an environment. However, unlike in the core module, this program sucessfully
shares the distance between the agents with all other agents and updates the agent status 
accordingly which didn't work on the previous model. 
This model also has other properties in that it has more agent classes
to distinguish between children and adults and also has an infection class that allows
disease to spread between agents, updating thier status in the child and adult classes.
The code for the other agent based model can be found here: https://github.com/3python/Agent-Based-Model
Ultimeately this model is much more involved than the other abm and serves a commpletely different
purpose.

@author: kate

Citation for using matplotlib
@Article{Hunter:2007,
  Author    = {Hunter, J. D.},
  Title     = {Matplotlib: A 2D graphics environment},
  Journal   = {Computing In Science \& Engineering},
  Volume    = {9},
  Number    = {3},
  Pages     = {90--95},
  abstract  = {Matplotlib is a 2D graphics package used for Python
  for application development, interactive scripting, and
  publication-quality image generation across user
  interfaces and operating systems.},
  publisher = {IEEE COMPUTER SOC},
  doi = {10.1109/MCSE.2007.55},
  year      = 2007
}
"""

#Importing a random number generator module.
import random
#Importing the maths module.
import math

#Importing a module to plot graphs.
import matplotlib
import matplotlib.pyplot

#Creating humans.
class Human():
    """Create a human adult. """
    def __init__(self, contact, adult_vaccination):
        """
        Assign values to initial characteristics of the human
        
        Positional arguements:
        contact -- "yes" or "no" string value (no default)
        status -- 0, 1 or 2 integer value (no default)
        
        Returns:
        Values for the starting characteristics of the human.
        """
        #Creates the x and y starting co-ordinates of the human.
        self.x = random.randint(0,20)
        self.y = random.randint(0,20)
        #Determines whether the adult starts of with immunity/vaccination (status = 2) to the disease.
        probability = random.randint(0,100)
        if probability > adult_vaccination:
            self.status = 0
        else:
            self.status = 1
        #Determines if the human starts of being in contact with an infected person.
        self.contact = contact
        #Sets a time since people have started being infected to 0.
        #This count increases the longer people have been infected for.
        #This is important as once they have been infected for a certain time 
        #period they stop being infectious.
        self.infectiontime = 0
        
    def movex(self):
        """
        Move the human a certain distance to the left or right.
        
        Returns:
        The new horizontal position of the human.
        """
        #Create the new horizontal location of the human.
        self.x = self.x + random.randint(-2,2)
        #If the human is going out of the confined space they are in
        #bring them back in.
        if self.x > 20 or self.x < 0:
            self.x = self.x % 20
        else:
            self.x = self.x
        return self.x
    
    def movey(self):
        """
        Move the human a certain distance up or down.
        
        Returns:
        The new vertical position of the human.
        """
        #If the human is going out of the confined space they are in
        #bring them back in.
        self.y = self.y + random.randint(-2,2)
        if self.y > 20 or self.y < 0:
            self.y = self.y % 20
        else:
            self.y = self.y
        return self.y
    
    def updatestatus(self, contact):
        """
        Change the infection status.
        
        Returns:
        The new infection status of the human.
        """
        try:
            #Has a susceptible human been in contact with someone who is infectious?
            #If they have.
            if self.status == 0 and contact == "yes":
                #Give them a probability of catching it.
                x = random.randint(0,20)
                #Depending on it's infectiousness (7). Decide whether they should catch it.
                if x > 19:
                    #If they have caught it, change thier status to infectious (2).
                    self.status = 2
                    #Increase the time they have been infected for.
                    self.infectiontime +=1
                #Otherwise they remain susceptible to disease.
                else:
                    self.status = 0
            #If a susceptible person hasn't been in contact with an infected person they remain susceptible.
            elif self.status == 0 and contact == "no":
                self.status = 0
            #If someone is infected, the amount of time they been infected increases each model run.
            elif self.status == 2 and self.infectiontime < 150:
                self.infectiontime += 1
                self.status = 2
            #Once an infected person has been infected for a certain amount time they become uninfectious. 
            elif self.status == 2 and self.infectiontime > 149:
                self.status = 1
                self.infectiontime +=1
            elif self.status == 1:
                self.status = 1
            #Measure to account for any scenarios I have forgot to cover.
            #Informs the user that something has gone wrong.
            else:
                print("Error in status assignment")
                self.status = self.status
        except:
            print("Something went wrong")
        #Return the status of the person.
        return self.status
        
#Takes in characteristics from the Human class.   
class Person0(Human):
    """Create a person who starts off infectious, using the characteristcs created in the Human class"""
    def __init__(self, contact):
        """
        Assign values to initial characteristics of the infected person
        
        Positional arguements:
        contact -- "yes" or "no" string value (no default)
        
        Returns:
        Values for the starting characteristics of the human.
        """
        #Creates the x and y starting co-ordinates of the infected person.
        self.x = random.randint(0,20)
        self.y = random.randint(0,20)
        #Assigns them an infected status.
        self.status =   2
        self.contact = contact
        #They have just become infected.
        self.infectiontime = 0
        
#Takes in characteristics from the human class.        
class Child(Human):
    """Create a child class"""
    def __init__(self, contact, child_vaccination):
        #Create starting position of the child.
        self.x = random.randint(0,20)
        self.y = random.randint(0,20)
        #Determines whether the chid starts of with immunity/vaccination (status = 2) to the disease.
        probability = random.randint(0,100)
        #Determines whether the child starts of with immunity/vaccination (status = 2) to the disease.
        probability = random.randint(0,100)
        if probability > child_vaccination:
            self.status = 0
        else:
            self.status = 1
        self.contact = contact
        self.infectiontime = 0


class Infection():
    """Determines if people will become infected or not"""
    def __init__(self, adults, contact):
        """Takes in the information required to run the model.
        
        Positional arguements:
        adults -- list of people created from the Human class or its derivatives (no default)
        contact -- "yes" or "no" string value (no default)
        
        Returns:
        Information required to run the model.
        """
        #A list of people created from the Human class of a class derived from this.
        self.adults = adults  
        
    #Is the agent in question in contact with an infected agent?
    def spread(self, adults, contact):
        """
        Determines if the human has come into contact with an infected person
        
        Positional arguements:
        adults -- list of people created from the Human class or its derivatives (no default)
        contact -- "yes" or "no" string value (no default)
        
        Returns:
        A list of whether each member of the list has come into contact with an infected person.
        """
        #A blank list saying whether each person is in contact with an infected agent.
        infectionlist = []
        for adult in adults:
            try:
                #A blank list saying whether there is contact with an infected agent.
                a = []
                #Go throught the list of people again so can come adults to all other adults in the list.
                for others in adults:
                    #Calculates the distance between the person and other people.   
                    b = math.sqrt((adult.movex() - others.movex())**2 + (adult.movey() - others.movey())**2)
                    #If the person is a certain distance from an infected erson
                    if b < 2 and others.updatestatus(contact) == 2:
                        #Code for yes for list sorting purposes.
                        c = 7
                        #Add 7 to the list.
                        a.append(c)
                    else:
                        #Not in contact. Add 8 to the list.
                        c = 8
                        a.append(c)
                #Put the list in numerical order.
                a.sort()
                #If the minimum value is 7, the adult is in contact with at least one infected person.
                #So contact with an infected person is yes.
                if a[0] == 7:
                    d = "yes"
                #Otherwise there is no contact with an infected person.
                else:
                    d = "no"
                #Append the list of whether there is contact with an infected person or not.
                infectionlist.append(d)
            except:
                print("something went wrong")
        #Return a list of whether each person is in contact with an infected person
        return infectionlist
    
    def update(self, adults, contact):
        """
        Creates a list of the infection status of each individual in the adults list.
        
        Positional arguements:
        adults -- list of people created from the Human class or its derivatives (no default)
        contact -- "yes" or "no" string value (no default)
        
        Returns:
        The infection status of each person in the list of adults.
        """    
        #Blank list to store the infection status of the people in the list.
        r = []       
        #Counter to determine which position in the list of whether each person is in contact with an 
        #infected person to use.
        i = 0
        try:
                
            #Looping through all the people.
            for adult in adults:
                #If they have been in contact with an infected person, change their contact status.
                a = self.spread(adults, contact)[i]
                #Move onto the next number in the list.
                i += 1
                if a == "yes":
                    contact = "yes"
                else:
                    contact = "no"
                #Define what the status is.
                q = adult.updatestatus(contact)            
                #Moving the people.
                adult.movex()
                adult.movey()
                #Populate the list of infection status.
                r.append(q)  
        except:
            print("something went wrong")
        #Return the list of which people are infected.
        return r

    
    def image(self, adults, contact):
        """
        Plots an image of the location and infection status of all agents.
        
        Postional arguements:
        adults -- list of people created from the Human class or its derivatives (no default)
        contact -- "yes" or "no" string value (no default)
        
        Returns:
        A graph showing the location and infection status of all the people in the list.
        """
        try:          
            #Lists of the location of the people. Used for plotting results.
            x_coordinate = []
            y_coordinate = []
            for adult in adults:
                #Moving the people.
                x = adult.movex()
                y = adult.movey()
                #Adding the locations of people to a list.
                x_coordinate.append(x)
                y_coordinate.append(y)            
            #Giving people colours depending on thier infection status.
            colour = []
            for x in self.update(adults, contact):
                if x == 0:
                    col =  'green'
                elif x == 1:
                    col = 'blue'
                elif x == 2:
                    col = 'red'
                else:
                    col = 'orange'
                colour.append(col)
            #Set up the figure location.
            fig = matplotlib.pyplot.figure()
            #Clearing the graph if there is already data on it.
            fig.clear()
            #Plotting a graph of the location of the people and thier infection status.
            matplotlib.pyplot.scatter(x_coordinate, y_coordinate, c=(colour))
            matplotlib.pyplot.show()
        except:
            print("something went wrong")

        
        

        
