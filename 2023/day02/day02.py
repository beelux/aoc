def file_input():
    with open("day02/input.txt", "r") as f:
        return f.readlines()

def getID(line):
    return int(line.split(" ")[1].split(":",1)[0])

def getReveals(line):
    return line.split(":",1)[1].strip().split("; ")

def getColors(reveals):
    max_dict = {"red": 0, "green": 0, "blue": 0}
    for reveal in reveals:
        for color in reveal.split(", "):
            data = color.split(" ")
            if int(data[0]) > max_dict[data[1]]:
                max_dict[data[1]] = int(data[0])
    return max_dict

def part1(lines):
    sum_of_ids = 0
    for line in lines:
        id = getID(line)
        reveals = getReveals(line)
        d = getColors(reveals)
        if(d["red"] <= 12 and d["green"] <= 13 and d["blue"] <= 14):
            sum_of_ids += id
            print(id)
    return sum_of_ids

def part2(lines):
    power_sum = 0
    for line in lines:
        id = getID(line)
        reveals = getReveals(line)
        d = getColors(reveals)
        power = 1
        for color in d.items():
            power *= color[1]
        power_sum += power
    return power_sum

print("Part 1:", part1(file_input()))
print("Part 2:", part2(file_input()))