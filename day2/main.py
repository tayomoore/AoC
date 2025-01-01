import collections

def getPuzzleInput():
    rows = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            rows.append(line.strip())
    return rows

def isChanging(levels):
    # is it in order? if not, then it can't be ok, so return early
    if not(levels == sorted(levels) or levels == sorted(levels, reverse=True)):
        return False
    # otherwise check to see there's no duplicates
    else:
        counts = collections.Counter(levels)
        for count in counts.values():
            if count > 1:
                return False
        return True

def isWithinBounds(levels):
    for index, level in enumerate(levels):
        if index == len(levels)-1:
            return True
        else:
            if not (level-3 <= levels[index+1] <= level +3):
                return False

def checkReport(levels):
    if not isChanging(levels):
        return 0
    if not isWithinBounds(levels):
        return 0
    else:
        return 1

def dampenLevels(report, index):
    dampenedReport = report.copy()
    del dampenedReport[index]
    return dampenedReport

def problemDampener(report, dampenProblems = False):
    levels = [int(element) for element in report.split(" ")]
    report = checkReport(levels)
    if report == 1:
        return 1
    elif dampenProblems:
        for index in range(0, len(levels)):
            dampenedReport = dampenLevels(levels, index)
            report = checkReport(dampenedReport)
            if report == 1:
                return 1
        return 0
    else:
        return 0

def part1(reports):
    numSafe = 0
    for report in reports:
        numSafe += problemDampener(report)
    return numSafe

def part2(reports):
    numSafe = 0
    for report in reports:
        numSafe += problemDampener(report, dampenProblems = True)
    return numSafe

def main():
    input = getPuzzleInput()
    partOneAnswer = part1(input)
    partTwoAnswer = part2(input)
    print(f'Part one answer: {partOneAnswer}')
    print(f'Part two answer: {partTwoAnswer}')


if __name__ == "__main__":
    main()