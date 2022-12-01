def file_input():
    f = open('2022/day01/input.txt')
    input = []
    sum = 0
    for line in f:
        if line.strip():
            sum += int(line)
        else:
            input.append(sum)
            sum = 0
    input.append(sum)
    return input

def find_largest():
    calories = file_input()
    max = calories[0]
    for num in calories:
        if num > max:
            max = num
    print(max)

def find_three_largest():
    cals = file_input()
    cals.sort(reverse=True)
    max = 0
    for i in range(3):
        max += cals[i]
    print(max)

find_largest()
find_three_largest()