#read in bits from file
def readInput():
    given_file = open('input.txt', 'r')
    lines = given_file.readlines()
    inputs = [line.strip('\n') for line in lines]
    given_file.close()
    return inputs

#creates an array on ints adds 1 to int in index for every 1 in binary value from input at same index
def calculateBits(inputs):
    size = len(inputs[0])
    counts = [0]*size
    for x in inputs:
        for y in range(size):
            counts[y] += int(x[y])
    print("Total: ",len(inputs), "Counts: ",counts)
    return counts

#calculates if 1 or 0 is most common by comparing total count of 1s for each index if greater then total input/2 1 is more common if not then 0 ties are always 1s
def calculateMostCommon(counts,total):
    gamma = ''
    epsilon = ''
    for x in counts:
        if x > total/2:
            gamma += "1"
            epsilon += "0"
        elif x == total/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print("gamma:",gamma," delta:",epsilon)
    return [gamma,epsilon]


#returns gamma * epsilon from array of 2 bit strings
def calculateRadiation(report):
    return int(report[0],2)*int(report[1],2)


inputs = readInput()
counts = calculateBits(inputs)
print("frequency counts:",counts)
RadiationReport = calculateMostCommon(counts,len(inputs))
print("Radiation binaries",RadiationReport)
RadiationResault = calculateRadiation(RadiationReport)
print("PowerConsumption =",RadiationResault)

#Part 2


def getMostCommonAtIndex(inputs,index):
    ones = [x for x in inputs if x[index] == "1"]
    #print("filter: ",ones)
    if len(ones) >= len(inputs)/2:
        return ones
    elif len(ones) == len(inputs)/2:
        return ones
    else:
        return [x for x in inputs if x[index] == "0"]


def getLeastCommonAtIndex(inputs,index):
    zeros = [x for x in inputs if x[index] == "0"]
    if len(zeros) <= len(inputs)/2:
        return zeros
    else:
        return [x for x in inputs if x[index] == "1"]


def calculateO2(inputs,index):
    if len(inputs) > 0:
        if index == len(inputs[0]):
            return inputs[0]
        inputsNew = getMostCommonAtIndex(inputs,index)
        index += 1
        result = calculateO2(inputsNew,index)
        if not result:
            return inputs[0]
        return result
    else:
        return


def calculateCO2(inputs,index):
    if len(inputs) > 0:
        if index == len(inputs[0]):
            return inputs[0]
        inputsNew = getLeastCommonAtIndex(inputs, index)
        index += 1
        result = calculateCO2(inputsNew, index)
        if not result:
            return inputs[0]
        return result
    else:
        return


def calculatetLifeSupport(inputs):
    O2 = calculateO2(inputs,0)
    CO2 = calculateCO2(inputs,0)
    print("O2 Binary:",O2," CO2 Binary:",CO2)
    return int(O2,2) * int(CO2,2)

print("Life Support Report =",calculatetLifeSupport(inputs))