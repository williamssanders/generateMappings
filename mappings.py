#!/usr/bin/python3.6
import sys, warnings, operator
from optparse import OptionParser
from random import *
from application import Application

def randomMapping(value):
        return randint(1,value)
    
def generateName(value):
        name = "A" + str(value)
        return name

def generateComputeName(value):
        name = "compute" + str(value)
        return name

def generateMapping(value):
        name = "M" + str(value)
        return name

def randomRate(dist):
    import random
    
    if (dist == "uniform"):
        # random.uniform(a, b)
        # Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
        return round(random.uniform(0.025,0.667),3)
    elif (dist == "beta"):
        # random.betavariate(alpha, beta)
        # Beta distribution. Conditions on the parameters are alpha > 0 and beta > 0. Returned values range between 0 and 1.
        return round(betavariate(0.025,0.667),3)
    elif (dist == "expo"):
        # random.expovariate(lambd)
        # Exponential distribution. lambd is 1.0 divided by the desired mean. It should be nonzero.
        return round(expovariate(0.667),3)
    elif (dist == "gamma"):
        # random.gammavariate(alpha, beta)
        # Gamma distribution. (Not the gamma function!) Conditions on the parameters are alpha > 0 and beta > 0.
        return round(gammavariate(0.025,0.667),3)
    elif (dist == "gauss"):
        # random.gauss(mu, sigma)
        # Gaussian distribution. mu is the mean, and sigma is the standard deviation.
        return round(gauss(0.025,0.667),3)
    elif (dist == "pareto"):
        # random.paretovariate(alpha)
        # Pareto distribution. alpha is the shape parameter.
        return round(paretovariate(0.025),3)
    elif (dist == "weibull"):
        # random.weibullvariate(alpha, beta)
        # Weibull distribution. alpha is the scale parameter and beta is the shape parameter.
        return round(weibullvariate(0.025,0.667),3)

def output2STDOUT(appList, numA, numM):
    applicationList = appList
    numberApplications = numA
    numberMachines = numM
    print("// Rate Definitions")
    print("// Rates starting with r are actual or original processing rates")
    print("// Rates starting with p are perturbed processing rates")
    for i in applicationList:
        print(i.string_rate(),i.string_perturbedRate())

    print("\n")
    print("// Application Definitions")
    for i in applicationList:
        print(i.definition())

    print("\n")
    print("// Machine Definition")
    for x in range(numberMachines):
        combinedString = ""
        machineNumber = x + 1
        rateString = ""
        perturbedRateString = ""
        for y in range(numberApplications):
            applicationNumber = y + 1
            if (generateMapping(machineNumber) == applicationList[y].get_mapping()):
                rateString = rateString + "(compute" + str(applicationNumber) + ", r" + str(applicationNumber) + ")."
                perturbedRateString = perturbedRateString + "(compute" + str(applicationNumber) + ", p" + str(applicationNumber) + ")."
        rateString = rateString + "M" + str(machineNumber)
        perturbedRateString = perturbedRateString + "M" + str(machineNumber)
        combinedString = "M" + str(machineNumber) + " = " + rateString + " + " + perturbedRateString + ";"
        print(combinedString)

    print("\n")
    applicationString = "("
    print("// System Equation for Mapping Definition")
    for x in range(numberApplications):
        number = x + 1
        if (number < numberApplications):
            applicationString = applicationString + generateName(number) + " <> "
        else:
            applicationString = applicationString + generateName(number) + ")"

    computeString = "<"
    for x in range(numberApplications):
        number = x + 1
        if (number < numberApplications):
            computeString = computeString + generateComputeName(number) + ", "
        else:
            computeString = computeString + generateComputeName(number) + ">"

    machineString = "("
    for x in range(numberMachines):
        number = x + 1
        if (number < numberMachines):
            machineString = machineString + generateMapping(number) + " <> "
        else:
            machineString = machineString + generateMapping(number) + ")"

    systemEquation = applicationString + " " + computeString + " " + machineString
    print(systemEquation)

def output2FILE(appList, numA, numM, filename):
    applicationList = appList
    numberApplications = numA
    numberMachines = numM
    outputfile = filename
    f = open(outputfile, "w")
    f.write("// Rate Definitions\n")
    f.write("// Rates starting with r are actual or original processing rates\n")
    f.write("// Rates starting with p are perturbed processing rates\n")
    for i in applicationList:
        my_rate = i.string_rate()
        my_perturbedRate = i.string_perturbedRate()
        my_string = my_rate + " " + my_perturbedRate + "\n"
        f.write(my_string)

    f.write("\n")
    f.write("// Application Definitions\n")
    for i in applicationList:
        my_definition = i.definition()
        my_string = my_definition + "\n"
        f.write(my_string)

    f.write("\n")
    f.write("// Machine Definition\n")
    for x in range(numberMachines):
        combinedString = ""
        machineNumber = x + 1
        rateString = ""
        perturbedRateString = ""
        for y in range(numberApplications):
            applicationNumber = y + 1
            if (generateMapping(machineNumber) == applicationList[y].get_mapping()):
                rateString = rateString + "(compute" + str(applicationNumber) + ", r" + str(applicationNumber) + ")."
                perturbedRateString = perturbedRateString + "(compute" + str(applicationNumber) + ", p" + str(applicationNumber) + ")."
        rateString = rateString + "M" + str(machineNumber)
        perturbedRateString = perturbedRateString + "M" + str(machineNumber)
        combinedString = "M" + str(machineNumber) + " = " + rateString + " + " + perturbedRateString + ";"
        f.write(combinedString + "\n")

    f.write("\n")
    applicationString = "("
    f.write("// System Equation for Mapping Definition\n")
    for x in range(numberApplications):
        number = x + 1
        if (number < numberApplications):
            applicationString = applicationString + generateName(number) + " <> "
        else:
            applicationString = applicationString + generateName(number) + ")"

    computeString = "<"
    for x in range(numberApplications):
        number = x + 1
        if (number < numberApplications):
            computeString = computeString + generateComputeName(number) + ", "
        else:
            computeString = computeString + generateComputeName(number) + ">"

    machineString = "("
    for x in range(numberMachines):
        number = x + 1
        if (number < numberMachines):
            machineString = machineString + generateMapping(number) + " <> "
        else:
            machineString = machineString + generateMapping(number) + ")"

    systemEquation = applicationString + " " + computeString + " " + machineString
    f.write(systemEquation + "\n")
    f.close()

def main():

    if not sys.warnoptions:
        warnings.simplefilter("ignore")
    usage = "usage: %prog [options]"    
    parser = OptionParser(usage=usage, version="%prog v 0.1")
    parser.add_option("-a", "--applications", action="store", dest="numberApplications", help="number of applications [DEFAULT=20]")
    parser.add_option("-m", "--machines", action="store", dest="numberMachines", help="number of machines [DEFAULT=5]")
    parser.add_option("-d", "--distribution", action="store", dest="distribution", help="statistical distribution [DEFAULT=uniform]")
    parser.add_option("-o", "--output", action="store", dest="outputName", help="output file name [DEFAULT=STDOUT]")
    parser.add_option("-c", "--constant", action="store", dest="constantFile", help="use pregenerated set of applications, generate mappings [DEFAULT=NA]")

    (options, args) = parser.parse_args()

    if (options.numberApplications):
        numberApplications = int(options.numberApplications)
    else:
        numberApplications = 20

    if (options.numberMachines):
        numberMachines = int(options.numberMachines)
    else:
        numberMachines = 5
    
    if (options.distribution):
        if (options.distribution == "uniform"):
            distribution = "uniform"
        elif (options.distribution == "beta"):
            distribution = "beta"
        elif (options.distribution == "expo"):
            distribution = "expo"
        elif (options.distribution == "gamma"):
            distribution = "gamma"
        elif (options.distribution == "gauss"):
            distribution = "gauss"
        elif (options.distribution == "pareto"):
            distribution = "pareto"
        elif (options.distribution == "weibull"):
            distribution = "weibull"
    else: 
        distribution = "uniform"

    n = numberApplications  # number of applications
    k = numberMachines   # number of machines
    applicationList = [i+1 for i in range(n)]
    machineList = [i+1 for i in range(k)]

    # if k > n, or n < k...exit with message
    if (k > n): # if number of machines is greater than the number of applications
        print("ERROR: Invalid Option: #Machines > #Applications")
        exit()
        
    elif (n < k): # if number of applications is less than the number of machines
        print("ERROR: Invalid Option: #Applications < #Machines")
        exit()

    if (n < (2*k)):
        print("ERROR: Invalid Option: Need at Least 2 Applications per Machine")
        exit()

    # initialize and/or n = k
    mySet = set([])
    while (len(mySet) < (2*k)):
        mySet.add(randrange(1,n+1))

    newList = list(mySet)
    perList = 2
    splitList = [newList[i * perList:(i + 1) * perList] for i in range((len(newList) + perList - 1) // perList )]
    myMappings = {} # empty dictionary
    myMachine = 1
    while (myMachine <= k):
        myMappings[myMachine] = splitList[myMachine -1]
        for element in (splitList[myMachine -1]):
            applicationList.remove(element)
        myMachine = myMachine + 1
    

    # finish mapping applications to machines
    myRange = len(applicationList)
    for item in applicationList:
        myMachine = randrange(1,k+1)
        tempList = myMappings[myMachine]
        tempList.append(item)
        myMappings[myMachine] = tempList

    masterApplicationList = []
    for machine in myMappings:
        myApplicationList = myMappings[machine]
        for application in myApplicationList:
            perturbed = 2.0
            normal = randomRate(distribution)
            while (perturbed > normal):
                perturbed = randomRate(distribution)

            myApplication = Application(application,generateName(application),normal,perturbed,generateComputeName(application),generateMapping(machine))
            output = myApplication.print_values()
            masterApplicationList.append(myApplication)
        
 
    masterApplicationList.sort(key=operator.attrgetter('key'))


    if (options.outputName):
        output2FILE(masterApplicationList, numberApplications, numberMachines, options.outputName)
    else: 
        output2STDOUT(masterApplicationList, numberApplications, numberMachines)

if __name__ == '__main__':
    main()