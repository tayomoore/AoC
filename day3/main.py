import re

def getPuzzleInput():
    rows = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            rows.append(line.strip())
    return rows

def getListOfInstructions(input):
    #glom the rows of the input together
    text = ''
    for inputLine in input:
        text += inputLine

    regex = r"mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)"
    matches = re.findall(regex, text)
    return matches

def parseInstruction(instruction):
    instructionSplit = re.split(r"[(),]", instruction)
    operation = instructionSplit[0]
    match operation:
        case 'mul':
            return 'mul', int(instructionSplit[1]), int(instructionSplit[2])
        case 'do':
            return 'do', None, None
        case 'don\'t':
            return 'dont', None, None

def part1(input):
    instructions = getListOfInstructions(input)
    total = 0
    for instruction in instructions:
        operation, operandA, operandB = parseInstruction(instruction)
        match operation:
            case 'mul':
                total += (operandA*operandB)
            case _:
                total += 0
    return total

def part2(input):
    instructions = getListOfInstructions(input)
    total = 0
    processInstruction = True
    for instruction in instructions:
        operation, operandA, operandB = parseInstruction(instruction)
        match operation:
            case 'mul':
                if processInstruction:
                    total += (operandA*operandB)
            case 'do':
                processInstruction = True
            case 'dont':
                processInstruction = False
            case _:
                total +=0
    return total

def main():
    input = getPuzzleInput()
    partOneAnswer = part1(input)
    partTwoAnswer = part2(input)
    print(f'Part one answer: {partOneAnswer}')
    print(f'Part two answer: {partTwoAnswer}')


if __name__ == "__main__":
    main()