def find_three_elements(array, P):
    array.sort()
    n = len(array)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            start = j + 1
            end = n - 1
            while start <= end:
                mid = (start + end) // 2
                current_sum = array[i] + array[j] + array[mid]
                if current_sum == P:
                    return True
                elif current_sum < P:
                    start = mid + 1
                else:
                    end = mid - 1
    return False


array = [3, 1, 10, 7]
P = 20
print(find_three_elements(array, P))
