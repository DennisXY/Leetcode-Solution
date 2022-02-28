# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visited = set()

        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i, j, 0):
                    return True
        return False

