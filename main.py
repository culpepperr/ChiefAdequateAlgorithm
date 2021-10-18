global board #because variables are outside of function need to call global variables, call global before defining function
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
player = 'X'


# Print board
def printBoard(board):
  for line in board: print (line)


# Take in user input and replace appropriate space
def makeMove():
  global player
  print("Player " + player + ":")
  x = int(input("input your x coordinate?"))
  y = int(input("input your y coordinate?"))
  
  while 0 < x > 2 or 0 < y > 2 or board[y][x] == 'X' or board[y][x] == 'O':
    print('invalid move, try again')
    print("Player " + player + ":")
    x = int(input("input your x coordinate?"))
    y = int(input("input your y coordinate?"))

  if player == 'X':
    board[y][x] = 'X'
    player = 'O'
  else:
    board[y][x] = 'O'
    player = 'X'

def checkBoard(gameWon):
  global board
  i=0
  ''' if (board[0][i] == 'O' and board [0][i+1] =='O' and board[0][i+2] == 'O') or (board[1][i] == 'O' and board [1][i+1] =='O' and board[1][i+2] == 'O') or (board[2][i] == 'O' and board [2][i+1] =='O' and board[2][i+2] == 'O') or (board[i][0] == 'O' and board [i+1][0] =='O' and board[i+2][0] == 'O') or (board[i][1] == 'O' and board [i+1][1] =='O' and board[i+2][1] == 'O') or (board[i][2] == 'O' and board [i+1][2] =='O' and board[i+2][2] == 'O') or (board[i][i] == 'O' and board [i+1][i+1] =='O' and board[i+2][i+2] == 'O'): '''
  cRow = checkRows('O')
  cColumns = checkColumns('O')
  cDiag = checkDiagonal('O')
  if checkWin('O', cRow, cColumns, cDiag): return True

      
  '''   elif (board[i][i] == 'X' and board [i+1][i+1] =='X' and board[i+2][i+2] == 'X') or (board[i][i+2] == 'X' and board [i+1][i+1] =='X' and board[i+2][i] == 'X') or(board[0][i] == 'X' and board [0][i+1] =='X' and board[0][i+2] == 'X') or(board[i][2] == 'X' and board [i+1][2] =='X' and board[i+2][2] == 'X') or(board[i][1] == 'X' and board [i+1][1] =='X' and board[i+2][1] == 'X') or(board[2][i] == 'X' and board [2][i+1] =='X' and board[2][i+2] == 'X') or(board[1][i] == 'X' and board [1][i+1] =='X' and board[1][i+2] == 'X'): '''
  cRow = checkRows('X')
  cColumns = checkColumns('X')
  cDiag = checkDiagonal('X')
  if checkWin('X', cRow, cColumns, cDiag): return True

  boardCount = 0
  for i in range(3):
    for n in range(3):
      if board[i][n] == ' ':
        continue
      else:
        boardCount += 1
  if boardCount >= 9:
    print("TIE GAME")
    return True

  return False


def checkColumns(symbol):
  for c in range(3):
    win = True
    for r in range(3):
      if board[c][r] != symbol:
        win = False
        break
    if win: return True

def checkRows(symbol):
  
  for r in range(3):
    win = True
    for c in range(3):
      if board[c][r] != symbol:
        win = False
        break
    if win: return True

def checkDiagonal(symbol):
  win = True
  for x in range(3):
    if board[x][x] != symbol:
      win = False
      break
  if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
    win = True
  if win: return True

def checkWin(symbol, cRow, cCol, cDiag):
  if cRow == True or cCol == True or cDiag == True:
    print(symbol + ' Wins')
    return True



def main():
  gameWon = False
  while gameWon == False:
    makeMove()
    printBoard(board)
    gameWon = checkBoard(gameWon)

  print('GAMEOVER')
    




# Keep variables out of main() and all function for game in main
main()
