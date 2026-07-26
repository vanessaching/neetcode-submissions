# an explanation from the video i watched so i can understand it better
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # creates sets so that all values are unique
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # fixed value because 9 x 9 
        for r in range(9):
            for c in range(9):
                # IMPORTANT
                # almost forgot this 
                if board[r][c] == ".":
                    continue
                # checks if not unique to the three sets
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                # adds the values 
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                # use this tuple as the key since it covers boxes 0-2 using integer division! 
                squares[(r//3, c//3)].add(board[r][c])
        return True