# 36. Valid Sudoku

from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board:List[List[str]]):
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val ==".":
                    continue
                if val in row[r] or val in col[c] or val in square[r//3,c//3]:
                    return False
                row[r].add(val)
                col[c].add(val)
                square[r//3,c//3].add(val)
        return True


#test
board =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

sol = Solution()

print(sol.isValidSudoku(board))