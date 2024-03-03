def find_three_elements(array, P):
    array.sort()
    n = len(array)
    for i in range(n - 2):
        start = i + 1
        end = n - 1
        while start < end:
            current_sum = array[i] + array[start] + array[end]
            if current_sum == P:
                return True
            elif current_sum < P:
                start += 1
            else:
                end -= 1
    return False


array = [3, 1, 10, 7]
P = 20
print(find_three_elements(array, P))
