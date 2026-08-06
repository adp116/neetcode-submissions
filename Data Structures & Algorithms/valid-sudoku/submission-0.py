class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for k in range(9):
                if board[i][k] == ".":
                    continue
                val = board[i][k]
                if (val in rows[i] or
                    val in cols[k] or 
                    val in squares[i//3,k//3]):
                    return False
                rows[i].add(val)
                cols[k].add(val)
                squares[i//3,k//3].add(val)
        return True

        