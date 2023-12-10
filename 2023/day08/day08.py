def file_input():
    with open("day08/input.txt", "r") as f:
        return f.readlines()

def parse_nodes(lines: list[str]) -> tuple[list[str], dict[str, tuple[str, str]]]:
    commands: list[str] = lines[0].rstrip('\n')
    nodes: dict[str, tuple[str, str]] = {}

    # Skip commands + empty line
    for line_index in range(2, len(lines)):
        line = lines[line_index]
        parts = line.split(" = ")
        name = parts[0]
        values = parts[1].lstrip("(").rstrip(")" + '\n').strip().split(", ")
        nodes[name] = (values[0], values[1])
    
    return (commands, nodes)

def part1(lines) -> int:
    steps = 0
    tmp = parse_nodes(lines)
    commands = tmp[0]
    nodes = tmp[1]

    current_node = "AAA"
    while(current_node != "ZZZ"):
        current_command = commands[steps % len(commands)]
        steps += 1
        match current_command:
            case 'L':
                current_node = nodes[current_node][0]
            case 'R':
                current_node = nodes[current_node][1]

    return steps

def fetch_starting_nodes(nodes: dict[str, tuple[str, str]]) -> list[str]:
    starting_nodes = []
    for node in nodes:
        if(node.endswith("A")):
            starting_nodes.append(node)
    return starting_nodes

def ends_with_z(current_nodes: list[str]) -> bool:
    for node in current_nodes:
        if(not node.endswith("Z")):
            return False
    return True

import math
from six.moves import reduce

def part2(lines):
    steps = 0
    tmp = parse_nodes(lines)
    commands = tmp[0]
    nodes = tmp[1]

    current_nodes = fetch_starting_nodes(nodes)
    least_steps : list[int] = [-1] * len(current_nodes)
    while(-1 in least_steps):
        current_command = commands[steps % len(commands)]
        steps += 1
        for index in range(len(current_nodes)):
            match current_command:
                case 'L':
                    current_nodes[index] = nodes[current_nodes[index]][0]
                case 'R':
                    current_nodes[index] = nodes[current_nodes[index]][1]
            if(least_steps[index] == -1 and current_nodes[index].endswith("Z")):
                least_steps[index] = steps

    return math.lcm(*least_steps)

#print("Part 1: \"" + str(part1(file_input())) + "\"")
# First try: 155388722128598496968704 - too high
# Second try: 21083806112641
print("Part 2: \"" + str(part2(file_input())) + "\"")