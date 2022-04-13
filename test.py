def second(N, order_list):
    for i in range(len(order_list)):
        order_list[i].append(i)
        order_list[i].append(order_list[i][1]/order_list[i][0])
    order_list.sort(key=lambda x: -x[3])
    cur_time, result = 0, 0
    for i in range(N):
        if cur_time <= order_list[i][0]-1:
            result += order_list[i][1]
            cur_time += 1
        else:
            continue
    return result


def third(all, candy):
    can_sum = sum(candy)
    print(can_sum)
    if can_sum % 2 == 1:
        return -1
    mean = int(sum(candy)/2)
    dp = [[0]*(mean+1) for i in range(all+1)]
    for i in range(1, all):
        for j in range(mean):
            if j >= candy[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-candy[i-1]]+candy[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    if dp[-1][-1] == mean:
        return mean
    else:
        return -1

if __name__ == '__main__':
    N = int(input())
    order_list = list()
    while True:
        try:
            temp = input()
            temp.split(" ")
            temp[0], temp[1] = int(temp[0]), int(temp[1])
            order_list.append(temp)
        except:
            break
    # order_list = [[1, 6], [1, 7], [3, 2], [3, 1], [2, 4], [2, 5], [6, 1]]
    print(second(N, order_list))

    # all, candy = 5, [7, 4, 5, 3, 3]
    # print(third(all, candy))
