# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that
# any 'O' on the border of the board are not flipped to 'X'.
# Any 'O' that is not on the border and it is not connected to an 'O' on the border
# will be flipped to 'X'.
# Two cells are connected if they are adjacent cells connected horizontally or vertically.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        from collections import deque
        queue = deque()
        for i in range(m):
            if board[i][0] == 'O':
                queue.append([i, 0])
            if board[i][n-1] == 'O':
                queue.append([i, n-1])
        for i in range(n):
            if board[0][i] == 'O':
                queue.append([0, i])
            if board[m-1][i] == 'O':
                queue.append([m-1, i])

        while queue:
            x, y = queue.pop()
            board[x][y] = "A"
            for mx, my in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= mx < m and 0 <= my < n and board[mx][my] == "O":
                    queue.append([mx, my])

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'