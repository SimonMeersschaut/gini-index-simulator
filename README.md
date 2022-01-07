# gini-index-simulator
This python script simulates a given Gini-index.
## nstalation
* Download the source (by clicking code, and then choosing download ZIP by example)
* First open <em>setup.bat</em>
* Now you can run the program by opening <em>simulator.py</em>
## using the program
* If the program is running fine, you should see a prompt asking for the gini-index, enter the gini-index you want to simulate (from 0 to 100)
* now it will ask for the number of people in the simulation, <ins>pay attention</ins> this is the amount of bars in the plot, <ins>not</ins> the amount of people in a country! (I usually go for 100) 
* Next, the program will be printing values, that means it is simulating. Just wait for about 5 minutes
## What does the plot mean?
* every bar on the plot is a simulated person. The height of the bar is the percent of money the person has (money of the person/total money)
* On the left you can see a label: 'error=...'. The value of the error shows how far the simulation is from the requested number
  * If this label is red, the plot is not accurate enough
