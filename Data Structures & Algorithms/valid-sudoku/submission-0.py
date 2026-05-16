class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in rows[i]:
                        return False
                    rows[i].add(board[i][j])
                    if board[i][j] in cols[j]:
                        return False
                    cols[j].add(board[i][j])
                    block = 0
                    if i < 3 and j <3:
                        block = 0
                        if board[i][j] in blocks[block]:
                            return False
                        else:
                            blocks[block].add(board[i][j])
                    elif (3<=i<6) and (0<=j<3):
                        block = 1
                        if board[i][j] in blocks[block]:
                            return False
                        else:
                            blocks[block].add(board[i][j])
                    elif (6<=i<9) and (0<=j<3):
                        block = 2
                        if board[i][j] in blocks[block]:
                            return False
                        else:
                            blocks[block].add(board[i][j])
                    elif (0<=i<3) and (3<=j<6):
                        block = 3
                        if board[i][j] in blocks[block]:
                            return False
                        else:
                            blocks[block].add(board[i][j])
                    elif (3<=i<6) and (3<=j<6):
                        block = 4
                        if board[i][j] in blocks[block]:
                            return False
                        else:
                            blocks[block].add(board[i][j])
                    elif (6<=i<9) and (3<=j<6):
                        block = 5
                        if board[i][j] in blocks[block]:
                            return False
                        else:
                            blocks[block].add(board[i][j])
                    elif (0<=i<3) and (6<=j<9):
                        block = 6
                        if board[i][j] in blocks[block]:
                            return False
                        else:
                            blocks[block].add(board[i][j])
                    elif (3<=i<6) and (6<=j<9):
                        block = 7
                        if board[i][j] in blocks[block]:
                            return False
                        else:
                            blocks[block].add(board[i][j])
                    elif (6<=i<9) and (6<=j<9):
                        block = 8
                        if board[i][j] in blocks[block]:
                            return False
                        else:
                            blocks[block].add(board[i][j])

        return True
