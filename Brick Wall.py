#https://gist.github.com/kinshuk4/2758b2a9a76e0630886c
#https://www.hackerrank.com/challenges/lego-blocks/problem

Mod = 100000007

def power(num, times):
    if times == 0: return 1
    if times == 1: return num
    temp = num
    for i in range(2, times+1):
        num *= temp
        num %= Mod
    return num

if __name__ == '__main__':
    N = input("Please input the height: ")
    M = input("Please input the width: ")

    total = [0] * 1001
    stable = [0] * 1001
    total[0] = total[1] = 1
    total[2] = 2
    total[3] = 4
    total[4] = 8
    stable[0] = stable[1] = 1
    for i in range(5, 1001):
        total[i] = (total[i-1] + total[i-2] + total[i-3] + total[i-4]) % Mod
    for i in range(M+1):
        total[i] = power(total[i], N)
    for i in range(2, M+1):
        Sum = 0
        for j in range(i):
            Sum += (stable[j]*total[i-j]) % Mod
            Sum %= Mod
        stable[i] = total[i] - Sum
        stable[i] = stable[i] % Mod

    while stable[M] < 0:
        stable[M] += Mod
    print(stable[M])