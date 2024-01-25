def QuickSort(arr, low, high):
    if low < high:
        loc = partition(arr, low, high)
        QuickSort(arr, low, loc-1)
        QuickSort(arr, loc+1, high)


def partition(arr, low, high):

    pivot = arr[low]
    start = low + 1
    end = high

    while start < end:
        while arr[start] < pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    arr[low], arr[end] = arr[end], arr[low]

    return end


arrNumbers = [-10, -20, 1, 2, 3, 0, 5, -4, 2]
QuickSort(arrNumbers, 0, len(arrNumbers) - 1)
print(arrNumbers)