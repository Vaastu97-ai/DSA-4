def max_sum_of_subarray(arr , k):
    if len(arr) < k:
        return None
    
    max_sum = 0

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k , len(arr)):

        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum , window_sum)

    return max_sum