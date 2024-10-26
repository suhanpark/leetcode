# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)


## Problem Description

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits `1-9` without repetition.
Each column must contain the digits `1-9` without repetition.
Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

### Example 1:
```plaintext
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

### Example 2:
```plaintext
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
```


### Constraints:
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j] is a digit 1-9 or '.'.`

## Solution

```python
# solution.py

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
```

## Explanation
Complexity

Time: O(n)

Space: O(n)

We have a set for each row, column and square. If the number is in the set, then it's not valid.

## Results

The following graphs show the performance of the solution:

### Time Complexity
![Time Complexity](./time.png)

### Memory Usage
![Memory Usage](./space.png)