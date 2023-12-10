import sys
sys.setrecursionlimit(3000)

def file_input() -> list[str]:
    with open("day10/input.txt", "r") as f:
        return f.readlines()

def find_start(lines: list[str]) -> tuple[int, int]:
    for line_index in range(len(lines)):
        if lines[line_index].find("S") != -1:
            return (line_index, lines[line_index].index("S"))

tmp_lines = file_input()
visited : list[list[int]] = [[0 for _ in range(len(tmp_lines[0]))] for _ in range(len(tmp_lines))]

import operator
def adjacent_edges(lines: list[str], start: tuple[int, int], origin: tuple[int,int]) -> list[tuple[int, int]]:
    edges = []
    possible_sides: list[tuple()] = []
    match lines[start[0]][start[1]]:
        case "L":
            possible_sides = [(-1, 0), (0, 1)]
        case "J":
            possible_sides = [(-1, 0), (0, -1)]
        case "7":
            possible_sides = [(1, 0), (0, -1)]
        case "F":
            possible_sides = [(1, 0), (0, 1)]
        case "|":
            possible_sides = [(-1, 0), (1, 0)]
        case "-":
            possible_sides = [(0, -1), (0, 1)]
        case "S":
            possible_sides = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        case other:
            possible_sides = []

    for side in possible_sides:
        new_position : tuple[int, int] = tuple(map(operator.add, start, side))
        try:
            new_character = lines[new_position[0]][new_position[1]]
            match side:
                case (-1, 0):
                    if(new_character in ["|", "7", "F", "S"]):
                        edges.append(new_position)
                case (1, 0):
                    if(new_character in ["|", "L", "J", "S"]):
                        edges.append(new_position)
                case (0, -1):
                    if(new_character in ["-", "L", "F", "S"]):
                        edges.append(new_position)
                case (0, 1):
                    if(new_character in ["-", "J", "7", "S"]):
                        edges.append(new_position)
        except IndexError:
            pass
    
    if origin in edges:
        edges.remove(origin)
    return edges

parents : dict[tuple[int, int], tuple[int, int]] = {}
def dfs(lines: list[str], start: tuple[int, int], previous: tuple[int, int] = (-1,-1)):
    global parents
    if lines[start[0]][start[1]] != "S" or (lines[start[0]][start[1]] == "S" and len(parents) >= 4):
        parents[start] = previous
    for edge in adjacent_edges(lines, start, previous):
        if edge not in parents.keys() and lines[edge[0]][edge[1]] != ".":
            dfs(lines, edge, start)

def dfs_iter(lines: list[str], start: tuple[int, int]):
    stack : list[tuple[int,int]] = []
    stack.append(start)
    current : tuple[int, int] = (-1, -1)
    previous : tuple[int, int] = (-1, -1)
    global parents
    while (len(stack) > 0):
        previous = current
        current = stack.pop()
        # not yet visited
        if current not in parents.keys() and lines[current[0]][current[1]] != ".":
            # do we wanna mark it?
            if lines[current[0]][current[1]] != "S" or (lines[current[0]][current[1]] == "S" and len(parents) >= 4):
                parents[current] = previous
            # add adjacent edges to stack
            for edge in adjacent_edges(lines, current, previous):
                stack.append(edge)

def bfs(lines: list[str], start: tuple[int, int]) -> tuple[int, int]:
    bfs_queue : list[tuple[int, int]] = []
    visited: set = set()
    visited.add(start)
    bfs_queue.append(start)
    while(len(bfs_queue) > 0):
        current = bfs_queue.pop()
        if(current != None):
            if(lines[current[0]][current[1]] == "S" and len(visited) != 1):
                return current
            for edge in adjacent_edges(lines, current):
                if edge not in visited or (lines[edge[0]][edge[1]] == "S" and len(visited) > 5):
                    visited.add(edge)
                    global parents
                    parents[edge] = current
                    bfs_queue.append(edge)

def mid_path_length(lines: list[str], start_position: tuple[int, int]) -> int:
    current = start_position
    if current is not None:
        steps = 0
        global parnets

        steps += 1
        current = parents[current]
        while(lines[current[0]][current[1]] != "S"):
            steps += 1
            current = parents[current]
        return steps/2
    else:
        return -1 

def part1(lines):
    start_position = find_start(lines)
    dfs_iter(lines, start_position)
    return mid_path_length(lines, start_position)

def part2(lines):
    return "TODO"

print("Part 1: \"" + str(part1(file_input())) + "\"")
print("Part 2: \"" + str(part2(file_input())) + "\"")