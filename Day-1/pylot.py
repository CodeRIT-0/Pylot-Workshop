class Pylot:
    def __init__(self) -> None:
        pass

    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-1):
                if arr[j] > arr[j + 1]:
                    # swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]



def func(a : int,b : int) -> int:
    return a + b