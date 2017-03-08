class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        height = len(board)
        width = len(board[0])
        def clickB(y, x):
            n = 0
            if y-1 >= 0:                        # row 1
                if x-1 >= 0:
                    if board[y-1][x-1] == 'E':
                        clickE(y-1, x-1)
                if board[y-1][x] == 'E':
                    clickE(y-1, x)
                if x+1 < width:
                    if board[y-1][x+1] == 'E':
                        clickE(y-1, x+1)
            if x-1 >= 0:                        # row 2
                if board[y][x-1] == 'E':
                    clickE(y, x-1)
            if x+1 < width:
                if board[y][x+1] == 'E':
                    clickE(y, x+1)
            if y+1 < height:                    # row 3
                if x-1 >= 0:
                    if board[y+1][x-1] == 'E':
                        clickE(y+1, x-1)
                if board[y+1][x] == 'E':
                    clickE(y+1, x)
                if x+1 < width:
                    if board[y+1][x+1] == 'E':
                        clickE(y+1, x+1)
            
        def clickE(y, x):
            n = 0
            if y-1 >= 0:                       # row 1
                if x-1 >= 0:
                    if board[y-1][x-1] == 'M':
                        n += 1
                if board[y-1][x] == 'M':
                    n += 1
                if x+1 < width:
                    if board[y-1][x+1] == 'M':
                        n += 1
            if x-1 >= 0:                      # row 2
                if board[y][x-1] == 'M':
                    n += 1
            if x+1 < width:
                if board[y][x+1] == 'M':
                    n += 1
            if y+1 < height:                  # row 3
                if x-1 >= 0:
                    if board[y+1][x-1] == 'M':
                        n += 1
                if board[y+1][x] == 'M':
                    n += 1
                if x+1 < width:
                    if board[y+1][x+1] == 'M':
                        n += 1
            if n == 0:
                board[y][x] = 'B'
                clickB(y, x)
            else:
                board[y][x] = str(n)
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        elif board[click[0]][click[1]] == 'E':
            clickE(click[0], click[1])
        else:
            pass
        return board