class Board:
  def __init__(self, boardLength):
    self.board = [[Cell(rIndex, cIndex) for cIndex in range(boardLength)] for rIndex in range(boardLength)]
    self.boardLength = boardLength

  def printB(self):
    print('\n\n    0,1,2,3,4,5,6,7\n')
    for index, row in enumerate(self.board):
      rowText = '{}   '.format(index)
      for cell in row:
        rowText += 'Q,' if cell.isQueen else '_,'
      print(rowText[:-1])
    print('\n')

  def changeQueenCount(self, x):
    self.queenCount += x

  def putQueens(self):
    i = 0
    queens = []
    while i < self.boardLength:
      j = 0
      while j < self.boardLength:
        cell = self.board[i][j]
        isNotAttacked = self.attackerCountOfCell(cell) == 0
        if(isNotAttacked):
          queens.append(cell)
          cell.makeQueen()
        if(j==self.boardLength-1 and len(queens)!=i+1):
          queens[-1].unMakeQueen()
          j=queens[-1].colIndex
          i=queens[-1].rowIndex
          queens = queens[:-1]
        j += 1
      i += 1

  def attackerCountOfCell(self, cell):
    count = 0
    for row in(self.board):
      for currentCell in(row):
        count += 1 if currentCell.canMove(cell.rowIndex, cell.colIndex) else 0
    return count
        
class Cell:
  def __init__(self, rowIndex, colIndex):
    self.isQueen = False
    self.rowIndex = rowIndex
    self.colIndex = colIndex

  def canMove(self, rowI, colI):
    if(self.isQueen):
      rowDif = abs(rowI - self.rowIndex)
      colDif = abs(colI - self.colIndex)
      return rowDif == 0 or colDif == 0 or rowDif == colDif
    else:
      return False

  def makeQueen(self):
    self.isQueen = True

  def unMakeQueen(self):
    self.isQueen = False

board = Board(8)
board.putQueens()
board.printB()
