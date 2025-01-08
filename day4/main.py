def getPuzzleInput():
    rows = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            rows.append(line.strip())
    return rows

def inputToGrid(input):
    grid = []
    for line in input:
        row = []
        for letter in line:
            row.append(letter)
        grid.append(row)
    return grid

def getDirectionsToCheck(rowLength, columnLength, stringLength, part):
    possibleDirections = []
    match part:
        case 'part1':
            possibleDirections = [
                {'direction':'r',  'minCol': 0,                'maxCol': rowLength - stringLength, 'minRow': 0,                'maxRow': columnLength - 1},
                {'direction':'l',  'minCol': stringLength - 1, 'maxCol': rowLength - 1,            'minRow': 0,                'maxRow': columnLength - 1},
                {'direction':'u',  'minCol': 0,                'maxCol': rowLength - 1,            'minRow': stringLength - 1, 'maxRow': columnLength - 1},
                {'direction':'d',  'minCol': 0,                'maxCol': rowLength - 1,            'minRow': 0,                'maxRow': columnLength - stringLength},
                {'direction':'ur', 'minCol': 0,                'maxCol': rowLength - stringLength, 'minRow': stringLength - 1, 'maxRow': columnLength - 1},
                {'direction':'ul', 'minCol': stringLength - 1, 'maxCol': rowLength - 1,            'minRow': stringLength - 1, 'maxRow': columnLength - 1},
                {'direction':'dr', 'minCol': 0,                'maxCol': rowLength - stringLength, 'minRow': 0,                'maxRow': columnLength - stringLength},
                {'direction':'dl', 'minCol': stringLength - 1, 'maxCol': rowLength - 1,            'minRow': 0,                'maxRow': columnLength - stringLength}
            ]
        case 'part2':
            possibleDirections = [
                {'direction':'x', 'minCol': stringLength // 2, 'maxCol': (rowLength-1) - stringLength // 2, 'minRow': stringLength // 2, 'maxRow': (columnLength-1) - stringLength // 2},
            ]
    return possibleDirections



def evaluateCoordinate(rowIndex, columnIndex, letter, allDirections):
    possibleDirections = []
    if letter != 'X':
        return False, possibleDirections
    for direction in allDirections:
        if (direction['minRow'] <= rowIndex <= direction['maxRow']) and (direction['minCol'] <= columnIndex <= direction['maxCol']):
            possibleDirections.append(direction['direction'])
    return True, possibleDirections

def countXmas(puzzleGrid, rowIndex, columnIndex, directionsToCheck):
    numFound = 0
    for direction in directionsToCheck:
        match direction:
            case 'r':
                if (puzzleGrid[rowIndex][columnIndex]=='X' 
                    and puzzleGrid[rowIndex][columnIndex+1]=='M' 
                    and puzzleGrid[rowIndex][columnIndex+2]=='A' 
                    and puzzleGrid[rowIndex][columnIndex+3]=='S'):
                    numFound += 1
            case 'l':
                if (puzzleGrid[rowIndex][columnIndex]=='X' 
                    and puzzleGrid[rowIndex][columnIndex-1]=='M' 
                    and puzzleGrid[rowIndex][columnIndex-2]=='A' 
                    and puzzleGrid[rowIndex][columnIndex-3]=='S'):
                    numFound += 1
            case 'u':
                if (puzzleGrid[rowIndex][columnIndex]=='X' 
                    and puzzleGrid[rowIndex-1][columnIndex]=='M' 
                    and puzzleGrid[rowIndex-2][columnIndex]=='A' 
                    and puzzleGrid[rowIndex-3][columnIndex]=='S'):
                    numFound += 1
            case 'd':
                if (puzzleGrid[rowIndex][columnIndex]=='X' 
                    and puzzleGrid[rowIndex+1][columnIndex]=='M' 
                    and puzzleGrid[rowIndex+2][columnIndex]=='A' 
                    and puzzleGrid[rowIndex+3][columnIndex]=='S'):
                    numFound += 1
            case 'ur':
                if (puzzleGrid[rowIndex][columnIndex]=='X' 
                    and puzzleGrid[rowIndex-1][columnIndex+1]=='M' 
                    and puzzleGrid[rowIndex-2][columnIndex+2]=='A' 
                    and puzzleGrid[rowIndex-3][columnIndex+3]=='S'):
                    numFound += 1
            case 'ul':
                if (puzzleGrid[rowIndex][columnIndex]=='X' 
                    and puzzleGrid[rowIndex-1][columnIndex-1]=='M' 
                    and puzzleGrid[rowIndex-2][columnIndex-2]=='A' 
                    and puzzleGrid[rowIndex-3][columnIndex-3]=='S'):
                    numFound += 1
            case 'dr':
                if (puzzleGrid[rowIndex][columnIndex]=='X' 
                    and puzzleGrid[rowIndex+1][columnIndex+1]=='M' 
                    and puzzleGrid[rowIndex+2][columnIndex+2]=='A' 
                    and puzzleGrid[rowIndex+3][columnIndex+3]=='S'):
                    numFound += 1
            case 'dl':
                if (puzzleGrid[rowIndex][columnIndex]=='X' 
                    and puzzleGrid[rowIndex+1][columnIndex-1]=='M' 
                    and puzzleGrid[rowIndex+2][columnIndex-2]=='A' 
                    and puzzleGrid[rowIndex+3][columnIndex-3]=='S'):
                    numFound += 1
            case _:
                pass
    return numFound            


def part1(input):
    puzzleGrid = inputToGrid(input)
    allDirections = getDirectionsToCheck(len(puzzleGrid[0]), len(puzzleGrid), 4, 'part1')
    xmasCount = 0
    for rowIndex, row in enumerate(puzzleGrid):
        for columnIndex, letter in enumerate(row):
            isCandidate, directionsToCheck = evaluateCoordinate(rowIndex, columnIndex, letter, allDirections)
            if isCandidate:
                xmasCount += countXmas(puzzleGrid, rowIndex, columnIndex, directionsToCheck)
    return xmasCount


def part2(input):
    puzzleGrid = inputToGrid(input)
    allDirections = getDirectionsToCheck(len(puzzleGrid[0]), len(puzzleGrid), 3, 'part2')
    xmasCount = 0
    for rowIndex, row in enumerate(puzzleGrid):
        for columnIndex, letter in enumerate(row):
            isCandidate, directionsToCheck = evaluateCoordinate(rowIndex, columnIndex, letter, allDirections)
            if isCandidate:
                xmasCount += countXmas(puzzleGrid, rowIndex, columnIndex, directionsToCheck)
    return xmasCount

def main():
    input = getPuzzleInput()
    partOneAnswer = part1(input)
    partTwoAnswer = part2(input)
    print(f'Part one answer: {partOneAnswer}')
    #print(f'Part two answer: {partTwoAnswer}')

if __name__ == "__main__":
    main()