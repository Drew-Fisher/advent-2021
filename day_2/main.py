def readInput():
    given_file = open('input.txt', 'r')
    lines = given_file.readlines()
    inputs = [[line.split()[0], int(line.split()[1])] for line in lines]
    given_file.close()
    return inputs


inputs = readInput()

print(inputs)
def calculatePosition(inputs):
    depth = 0
    forward = 0
    for x in inputs:
        if x[0] == "forward":
            forward+= x[1]
        elif x[0] == "down":
            depth += x[1]
        elif x[0] == "up":
            depth -= x[1]
    calc = depth * forward
    print(depth)
    print(forward)
    print(calc)

calculatePosition(inputs)