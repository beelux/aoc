def file_input():
    with open("day01/input.txt", "r") as f:
        return f.readlines()
    
def part1(lines):
    calibrationValues = []

    for line in lines:
        firstNumber = -1
        secondNumber = -1
        for character in line:
            try:
                number = int(character)

                if firstNumber == -1:
                    firstNumber = character
                
                secondNumber = character
            except ValueError:
                continue
        
        calibrationValues.append(int(firstNumber + secondNumber))
        firstNumber = -1

    return sum(calibrationValues)

def part2(lines):
    calibrationValues = []
    # Dictionary
    numbers = {
        "1": 1, "one": 1,
        "2": 2, "two": 2,
        "3": 3, "three": 3,
        "4": 4, "four": 4,
        "5": 5, "five": 5,
        "6": 6, "six": 6,
        "7": 7, "seven": 7,
        "8": 8, "eight": 8,
        "9": 9, "nine": 9
    }

    for line in lines:
        low = -1
        up = -1
        
        lowestIndex = 999
        lowSize = 0
        for key in numbers.keys():
            index = line.find(key)
            if(index != -1 and index < lowestIndex):
                lowSize = len(key)
                lowestIndex = index
        
        highestIndex = -1
        highSize = 0
        for key in numbers.keys():
            index = line.rfind(key)
            if(index > highestIndex):
                highSize = len(key)
                highestIndex = index

        lowValue = line[lowestIndex:lowestIndex+lowSize]
        low = numbers[lowValue]
        high = numbers[line[highestIndex:highestIndex+highSize]]

        calibrationValues.append(int(str(low) + str(high)))

    return sum(calibrationValues)

print(part1(file_input()))
print(part2(file_input()))