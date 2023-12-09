import contextlib

def file_input():
    with open("day03/input.txt", "r") as f:
        return f.readlines()

def adjacentToSymbol(lines, i_begin, j_begin, length):
    # Now, we can check the adjacent cells (i-1 to i+1, j-1 to j+length)
    for i in range(max(0, i_begin-1), min(i_begin+2, len(lines)-1)):
        for j in range(max(0, j_begin-1), min(j_begin+length+1, len(lines[0])-1)):
            if(not lines[i][j].isdigit() and lines[i][j] != '.'):
                return True
    return False

def getLengthOfNumber(line, j_begin):
    length = 0
    while(True):
        try:
            if(line[j_begin + length].isdigit()):
                length += 1
            else:
                break
        except:
            break
    return length

def part1(lines):
    sum = 0
    for i in range(len(lines)):
        j = 0
        while(j < len(lines[0])-1):
            if( (lines[i][j]).isdigit() ):
                length = getLengthOfNumber(lines[i], j)
                if(adjacentToSymbol(lines, i, j, length)):
                    print("Found adjacent number: " + lines[i][j:j+length] + " at (" + str(i) + ", " + str(j) + ")")
                    sum += int(lines[i][j:j+length])
                j += length + 1
            else:
                j += 1
    return sum
            
def part2(lines):
    return "TODO"

# First sol:   517186
# Second sol:  518161
# Correct sol: 512794
print("Part 1: \"" + str(part1(file_input())) + "\"")
print("Part 2: \"" + part2(file_input()) + "\"")