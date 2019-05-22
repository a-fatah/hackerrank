#!/usr/bin/python

def nextMove(n,r,c,grid):
    # bot position known, search for princess only
    for i, line in enumerate(grid):
            if 'p' in line:
                princess = (line.index('p'), i)

    import operator
    difference = tuple(map(operator.sub, princess, (r, c)))
    x_steps = ['RIGHT' if difference[0] > 0 else 'LEFT'] * abs(difference[0])
    if x_steps:
        return x_steps[0]

    y_steps = ['UP' if difference[1] < 0 else 'DOWN'] * abs(difference[1])
    if y_steps:
        return y_steps[0]
    

if __name__ == '__main__':
    grid = [
        '-----',
        'm----',
        'p----',
        '-----',
        '-----',
    ]
    r,c = 0,1
    print(nextMove(5,r,c,grid)) 

