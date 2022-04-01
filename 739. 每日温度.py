# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you
# have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
#
# Example 1:
#
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        result = [0] * length
        stack = list()
        for i in range(length-1):
            if temperatures[i] < temperatures[i+1]:
                result[i] = 1
                while stack:
                    if stack[-1][1] < temperatures[i+1]:
                        result[stack[-1][0]] = i+1-stack[-1][0]
                        stack.pop()
                    else:
                        break
            else:
                while stack:
                    if stack[-1][1] < temperatures[i+1]:
                        result[stack[-1][0]] = i+1-stack[-1][0]
                        stack.pop()
                    else:
                        break
                stack.append([i, temperatures[i]])
        return result