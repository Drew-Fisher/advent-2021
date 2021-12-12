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

print(calculatePosition(inputs))

def calculatePositionWithAim(inputs):
    horizontal_position = 0
    aim = 0
    depth = 0
    for x in inputs:
        if x[0] == "forward":
            horizontal_position += x[1]
            depth += (aim*x[1])
        elif x[0] == "down":
            aim += x[1]
        elif x[0] == "up":
            aim -= x[1]
    return depth*horizontal_position

print(calculatePositionWithAim(inputs))