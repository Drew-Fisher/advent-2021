def readInput():
    given_file = open('input.txt', 'r')
    lines = given_file.readlines()
    inputs = [int(line) for line in lines]
    given_file.close()
    return inputs


inputs = readInput()


def countIncrease(inputs):
    count = sum(1 for (i, x) in enumerate(inputs) if i > 0 if x > inputs[i - 1])
    return count


print(countIncrease(inputs))


def countSlices(inputs):
    count = sum(1 for (i,x) in enumerate(inputs) if i > 0 and i <= len(inputs)-3 if sum(inputs[i:i+3]) > sum(inputs[i-1:i+2]))
    return count

print(countSlices(inputs))
