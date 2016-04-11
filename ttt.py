import numpy as np

def toLetter(i):
    if i==1:
        return 'X'
    if i==0:
        return 'O'
    if i==-1:
        return ' '

def printgrid(g):
    for r in range(2):
        print '\033[4m' + ' '  + toLetter(g[r,0]) + ' | ' + toLetter(g[r,1]) + ' | ' + toLetter(g[r,2]) + ' ' + '\033[0m'
    
    print ' ' + toLetter(g[2,0]) + ' | ' + toLetter(g[2,1]) + ' | ' + toLetter(g[2,2]) + ' '

def check(g):
    """Returns 1 or 0 if X or O won, respectively. Returns -1 if draw and -99 if game still in progess."""
    for row in range(3):
        left = g[row,0]
        if left != -1 and left == g[row,1] and left == g[row,2]:
            return left
    for col in range(3):
        top = g[0,col]
        if top != -1 and top == g[1,col] and top == g[2,col]:
            return top

    mid = g[1,1]
    if mid != -1 and ((mid == g[0,0] and mid == g[2,2]) or (mid == g[0,2] and mid == g[2,0])):
        return mid
    
    if -1 in g:
        return -99

    return -1

def userplay(g, player):
    """player must be 1 or 0 for X or O respectively"""
    printgrid(g)
    inp = input('\nEnter your move for Team %s:\n' %toLetter(player))
    col = inp%3 - 1
    row = (inp-1)/3
    if g[row,col] == -1:
        g[row,col] = player
    else:
        print 'Square already filled. Try again.'
        g = userplay(g,player)
    return g

def twopgame():
    grid = -np.ones((3,3), dtype=np.int)
    winner = -1
    moveno = 1
    print 'Choose your square by entering a digit 1-9 (starting from the top left like a standard phone layout)'
    result=-99
    while result==-99:
        grid = userplay(grid, moveno%2)
        moveno+=1
        result = check(grid)
    printgrid(grid)
    print 'Game over.'
    if result == -1:
        print 'It\'s a draw, as usual.'
    else:
        print 'Somehow, even though this is tic tac toe, %s managed to lose. Congrats Team %s' %(toLetter(1-result), toLetter(result))

def main():
    if input('Press 2 to play 2-player with a friend: ')==2:
        twopgame()
    return 0;

main()
