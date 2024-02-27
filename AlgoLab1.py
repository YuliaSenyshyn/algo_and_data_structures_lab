def gardener_bot_work(our_list):
    n = len(our_list)
    ready_list = []
    for i in range(n):
        if i % 2 == 0:
            ready_list.extend(our_list[i])
        else:
            ready_list.extend(reversed(our_list[i]))
    return ready_list


our_list = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
print(gardener_bot_work(our_list))
