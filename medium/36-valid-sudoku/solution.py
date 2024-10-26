class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols, rows = {i: set() for i in range(9)}, {i: set() for i in range(9)}
        squares = {(i, j): set() for j in range(9) for i in range(9)}
        
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col.isnumeric():
                    if (col in rows[i] 
                    or col in cols[j] 
                    or col in squares[(i//3, j//3)]):
                        return False
                    cols[j].add(col)
                    rows[i].add(col)
                    squares[(i//3, j//3)].add(col)

        return True