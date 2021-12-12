def readInput():
    given_file = open('input.txt', 'r')
    lines = given_file.readlines()
    inputs = [line for line in lines]
    given_file.close()
    return inputs


inputs = readInput()


def calculateBits(inputs,size):
    total = 0
    counts = [0]*size
    for x in inputs:
        for y in range(size):
            counts[y] += int(x[y])
        total += 1
    print("Total: ",total, "Counts: ",counts)
    gamma = ''
    delta = ''
    for x in counts:
        if x > total/2:
            gamma += "1"
            delta += "0"
        else:
            gamma += "0"
            delta += "1"
    print("gamma: ",gamma," delta: ",delta)
    return int(gamma,2)*int(delta,2)


print(calculateBits(inputs,len(inputs[0])-1))