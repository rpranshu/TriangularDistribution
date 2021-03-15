'''
ENCE 662: Introduction to Project Management
Assignment 2

Submitted by: Pranshu Ranakoti
UID: 116952033

Comments have been included wherever necessary

The output produces 2 GUI graph windows containing the results
'''

#Importing libraries
import numpy as np
import statistics
from matplotlib import pyplot

#Setting the graph figure (GUI) size
pyplot.rcParams["figure.figsize"] = (12,6)


def Windows():                                                          #Create a function for Windows project
    ProjectCost=[]                                                      #Declare an empty list
    j=0                                                                 #Declare a count variable

    for i in range (100000):                                            #For loop to run 100,000 simulations
        HardwareCost = np.random.triangular(150000,175000,250000)       #Random Triangular Distribution value for Hardware Cost
        SoftwareCost = np.random.triangular(250000,300000,580000)       #Random Triangular Distribution value for Software upgrade Cost
        EmpTrainCost = np.random.triangular(5000,10000,15000)           #Random Triangular Distribution value for Employee Training Cost
        sum = HardwareCost + SoftwareCost + EmpTrainCost                #Expected project cost for one particular iteration

        if sum > 575000:                                                #Conditional statement for part 2
          j=j+1                                                         #Increase count if a value in the list is more than $575,000

        ProjectCost.append(sum)                                         #Appending the list containing 100,000 sampled project costs.

    mean = statistics.mean(ProjectCost)                                 #Taking the mean of those 100,000 sampled costs
    stdev = statistics.stdev(ProjectCost)                               #Standard deviation of the sampled Project Cost
    probability = j/1000                                                #Probability that a value in the list is more than $575,000

    #Plotting the graph of the triangular distribution
    pyplot.figure(), pyplot.hist(ProjectCost,bins = 1000, density=True, color="blue", label = "Expected Cost of Windows Project is: $" + str(round(mean,3))+ "\nStandard deviation: $"+ str(round(stdev,3))+"\nProbability of project cost being greater than $575K: "+str(round(probability,2))+"%")
    pyplot.legend(loc="upper right")
    pyplot.xlabel("Project Cost in USD")

'''
The comments will be the same for this function becuase the exact same programming logic
has been applied to find the results for the Unix project as well.
'''

def Unix():
    ProjectCost=[]
    j=0
    for i in range (100000):
        HardwareCost = np.random.triangular(70000,100000,275000)
        SoftwareCost = np.random.triangular(225000,300000,515000)
        EmpTrainCost = np.random.triangular(10000,11000,17500)
        sum = HardwareCost + SoftwareCost + EmpTrainCost
        ProjectCost.append(sum)
        if sum > 575000:
          j=j+1
    mean = statistics.mean(ProjectCost)
    stdev = statistics.stdev(ProjectCost)
    probability = j/1000
    pyplot.figure(), pyplot.hist(ProjectCost,bins = 1000, density=True, color="orange", label = "Expected Cost of Unix Project is: $" + str(round(mean,3))+ "\nStandard deviation: $"+ str(round(stdev,3))+"\nProbability of project cost being greater than $575K: "+str(round(probability,2))+"%")
    pyplot.legend(loc="upper right")
    pyplot.xlabel("Project Cost in USD")
    pyplot.show()

#Calling the function to execute the respective code and get the results
Windows()
Unix()
