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

def part2(lines):
    return "TODO"

print("Part 1: \"" + str(part1(file_input())) + "\"")
print("Part 2: \"" + part2(file_input()) + "\"")