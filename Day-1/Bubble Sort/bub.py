def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-1):
            if arr[j] > arr[j + 1]:
                # swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [2, 5, 3, 7, 13, 1]
print(arr)


# def bub(arr):
#     n = len(arr)
#     for _ in range(n):
#         visited = False
#         for i in range(n-1):
#             if(arr[i] > arr[i+1]):
#                 visited = True
#         if not visited:
#             break
#     print(arr)


# bub([2, 3, 6])
