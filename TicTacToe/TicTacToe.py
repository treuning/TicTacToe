#var = input("Please enter something: ")
#print("You entered " + str(var))
import numpy

tics = ['#','#','#',
        '#','#','#',
        '#','#','#']
moves = []
active = True

def moveCheck(n):
    try:
        i = moves.index(n)
        return False
    except ValueError:
        moves.append(n)
        return True
    

def getABC(arg):
    if (arg == 'a'):
        return 1
    elif (arg == 'b'):
        return 4
    else:
         return 7


def get123(arg):
    if (arg == '1'):
        return 1
    elif (arg == '2'):
        return 2
    else:
         return 3


def draw():
    print("  1 2 3 \nA|"+tics[0]+'|'+tics[1]+'|'+tics[2]+'|\nB|'+tics[3]+'|'+tics[4]+'|'+tics[5]+'|\nC|'+tics[6]+'|'+tics[7]+'|'+tics[8]+'|')

#def update(tString):
#    move = tString.split()
#    y = getABC(move[0])
#    x = get123(move[1])
#    s = x+y
#    n = s-2
#    tics[n] = 'X'
#    print('s',s)
#    print('n',n)
    

def oTurn():
    turn = input("Its O's move\nEnter move (example a 1):")
    move = turn.split()
    y = getABC(move[0])
    x = get123(move[1])
    s = x+y
    n = s-2
    if(moveCheck(n)):
        tics[n] = 'O'
        print('s',s)
        print('n',n)
        print(moves)
        #return turn
    else:
        print("\nCan't move there, lose a turn\n")

def xTurn():
    turn = input("Its X's move\nEnter move (example a 1):")
    move = turn.split()
    y = getABC(move[0])
    x = get123(move[1])
    s = x+y
    n = s-2
    n = ((getABC(move[0])+get123(move[1]))-2)
    if(moveCheck(n)):
        tics[n] = 'X'
        print('s',s)
        print('n',n)
        print(moves)
        #return turn
    else:
        print("\nCan't move there, lose a turn\n")

def isFinished():
    return active == False


#oTurn()
#update(oTurn())

while active:
#    if(isFinished()):
    draw()
    oTurn()
    draw()
    xTurn()
    isFinished()


