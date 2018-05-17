This readme is created based on the template provided by PurpleBooth at https://gist.github.com/PurpleBooth/109311bb0361f32d87a2

Created on 17 May 2018

Model Verson: 1.0

--------------------
Disease Spread Model
--------------------

This model shows how a disease spreads round a model environment under varying levels of adult and child vaccination rates. The model is based on the contact distance
and infectiousness of the Cooties complex virus. However for other diseases, these parameters can also be changed in the code. 


---------------------
Intention of software
---------------------

This software intends to model how the disease will spread in a population when differing percentages of the adult and child population are vaccinated (or are immune 
through other channels). It creates families of 2 adults and 2 children (one family contains an infected adult).
People can either be susceptible to the disease (status: 0), immune (status: 1) or infectious (status: 2). People are either susceptible or immune, depending on 
whether they have been vaccinated. The percentage of adults and children that have been vaccinated can be changed by the user. If people come into contact with an 
infected person (are a certain distance from them), there is a chance they will catch the disease. If someone catches the disease they are infectious for a certain 
amount of time before becoming immune. Every day, people come home and mix with their families (mixing between ages) and then go to work/nursery (mix with more people 
of the same age). This process repeats itself until no one infectious is left. The model records show many people are infectious each day and prints a graph which 
shows how the disease is progressing. 

This model assumes that both children in a family go to the same nursery and that no-one socialses outside home or work.
The set period that the disease is infectious for is 4 days. There is no incubation period for the virus, and people do not stay at home when they know they are 
infectious.


---------------
Getting Started
---------------


Prerequisites
-------------

To get this model to work, python 3 has to be downloaded on the computer. 
This project was created in the spyder Integrated Development Environment (IDE). If this IDE is not installed on your computer, the
matplotlib module will need to be installed. This can be installed from https://matplotlib.org/

You will also need to have downloaded the disease_module.py and disease_model.py
Load/Run disease_module.py and then disease_model.py


How to run the code.
-------------------

The files provided that are required to run this program are
1)	disease_module.py
This contains a Human, Person0 and Child classes required to create people with the required properties. It also contains an Infection class which determines if 
people are near another infected person and if they are, it then runs the function on the people classes to update their infection status accordingly.

2)	disease_model.py
This creates people using the classes in the disease_module. It places people into lists of families, workplaces, and nurseries. It then allows people to interact 
with other people during the day, spreading disease between them until no-one infectious is left.

Instructions:
1) Open up disease_model.py and disease_module.py in spyder, 
2) Run disease_module and then disease_model.py
3) Enter the number of adults and children you want to be vaccinated. This should be a value between 0 and 100.
4) Wait for this to finish running (it can take a while). When it has finished, “finished running” will appear in the console window and a GUI will appear. The GUI 
will show a graph of how the disease has spread through time.


The model has finished running when "Finished running" appears in the IDE and a GUI should appear with a graph showing how the disease has progressed through time.


-------
Authors
-------
Kate Benny

-------
License
-------
This project is licensed under the MIT license

(Description of MIT license copied from git hub)
MIT License

Copyright (c) 2018 3python

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---------------
Acknowledgments
---------------
Thank you to Andy Evans coding courses, Programming for Spatial Analysits Core Skills and Programming for Spatial Analysits Advanced Skills
These courses can be found here: http://www.geog.leeds.ac.uk/courses/computing/.
Also thanks to Andy Evans for all his coding help.