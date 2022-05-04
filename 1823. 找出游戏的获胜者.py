# There are n friends that are playing a game. The friends are sitting in a
# circle and are numbered from 1 to n in clockwise order. More formally,
# moving clockwise from the ith friend brings you to the (i+1)th friend for
# 1 <= i < n, and moving clockwise from the nth friend brings you to the
# 1st friend.
#
# The rules of the game are as follows:
#
# Start at the 1st friend.
# Count the next k friends in the clockwise direction including the friend
# you started at. The counting wraps around the circle and may count some friends
# more than once.
# The last friend you counted leaves the circle and loses the game.
# If there is still more than one friend in the circle, go back to step 2
# starting from the friend immediately clockwise of the friend who just lost and
# repeat.Else, the last friend in the circle wins the game.
# Given the number of friends, n, and an integer k, return the winner of the game.

# 约瑟夫环
# f(n,m)指n个人，报第m个编号出列最终编号
# f(n,m)=(f(n-1,m)+m)%n对这个公式的理解：
# 在第一次删除一个数后，环中还有n-1个数，接下来将以m+1这个数作为新的1开始进行新的
# 一轮删除，并得到一个结果f(n-1,m)。但是由于这个结果是由新的1到n-1的编号得到的，
# 所以不能直接作为n，m的结果，必须要将得到编号还原为n，m中的编号才行。而还原编号的方法
# 则正好是编号方法的逆向过程。在上面编码的过程是将m+1变为1，也就是减m，
# 因此反过来就是加m。最后由于求余得到范围内的编号。


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 1
        for i in range(2, n + 1):
            winner = (k + winner - 1) % i + 1
        return winner

