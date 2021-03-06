# Suppose you have a random list of people standing in a queue.
# Each person is described by a pair of integers (h, k),
# where h is the height of the person and k is the number of people in front of this person
# who have a height greater than or equal to h.
# Write an algorithm to reconstruct the queue.
#
# Example
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

# 当我们放入第i个人时，只需要将其插入队列中，使得他的前面恰好有k_i个人即可。


class Solution:
    def reconstructQueue(self, people):
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output


if __name__ == '__main__':
    a = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    solution = Solution()
    c = solution.reconstructQueue(a)
    print(c)

