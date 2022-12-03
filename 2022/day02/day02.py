ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 0
DRAW = 3
WIN = 6
shapes = {
    'A': ROCK, 'X': ROCK,
    'B': PAPER, 'Y': PAPER,
    'C': SCISSORS, 'Z': SCISSORS
}
end = {
    'X': LOSE, 'Y': DRAW, 'Z': WIN
}
cal_moves = {
    ROCK: {
        LOSE: 'Z',
        DRAW: 'X',
        WIN: 'Y'
    },
    PAPER: {
        LOSE: 'X',
        DRAW: 'Y',
        WIN: 'Z'
    },
    SCISSORS: {
        LOSE: 'Y',
        DRAW: 'Z',
        WIN: 'X'
    }   
}

def file_input():
    f = open('2022/day02/input.txt')
    input = []
    for line in f:
        if line.strip():
            input.append(tuple(map(str, line.split())))
    return input

def win(score):
    score[0] += LOSE
    score[1] += WIN
def lose(score):
    score[0] += WIN
    score[1] += LOSE
def draw(score):
    score[0] += DRAW
    score[1] += DRAW

def get_value(move):
    return shapes[move]

def get_round_score(round):
    score = [0, 0]
    score[0] = get_value(round[0])
    score[1] = get_value(round[1])

    if(score[1] == ROCK):
        if(score[0] == ROCK):
            draw(score)
        elif(score[0] == PAPER):
            lose(score)
        elif(score[0] == SCISSORS):
            win(score)
    elif(score[1] == PAPER):
        if(score[0] == ROCK):
            win(score)
        elif(score[0] == PAPER):
            draw(score)
        elif(score[0] == SCISSORS):
            lose(score)
    elif(score[1] == SCISSORS):
        if(score[0] == ROCK):
            lose(score)
        elif(score[0] == PAPER):
            win(score)
        elif(score[0] == SCISSORS):
            draw(score)

    return score

def find_score(): #Part1
    input = file_input()
    final = [0, 0]
    for round in input:
        outcome = get_round_score(round)
        final[0] += outcome[0]
        final[1] += outcome[1]
    print(final[1])

def calculate_move(round):
    opp = round[0]
    me = end[round[1]]
    calculated_round = (opp, cal_moves[shapes[opp]][me])
    return get_round_score(calculated_round)

def find_moves(): #Part2
    input = file_input()
    final = [0, 0]
    for round in input:
        outcome = calculate_move(round)
        final[0] += outcome[0]
        final[1] += outcome[1]
    print(final[1])


find_score()
find_moves()