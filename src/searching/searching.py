def linear_search(arr, target):
    # Your code here
    i = 0

    while i < len(arr):
        if arr[i] == target:
            return True
        i = i + 1


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start_index = 0
    end_index = len(arr) - 1
    # Your code here
    while start_index <= end_index:
        midpoint = start_index + (end_index - start_index) // 2
        midpoint_value = arr[midpoint]
        if midpoint_value == target:
            return midpoint
        elif target < midpoint_value:
            end_index = midpoint - 1
        else: start_index = midpoint + 1


    return -1  # not found
