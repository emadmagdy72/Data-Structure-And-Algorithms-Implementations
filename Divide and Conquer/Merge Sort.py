def mergeSort(arr, start, end):
    mid = (start + end) // 2

    if start < end:
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):

    i = start
    j = mid + 1
    temp = []
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    temp.extend(arr[i:mid+1])
    temp.extend(arr[j:end+1])

    k = start
    while k <= end:
        arr[k] = temp[k-start]
        k += 1


arrNumbers = [-10, -20, 1, 2, 3, 0, 5, -4, 2]
mergeSort(arrNumbers, 0, len(arrNumbers) - 1)
print(arrNumbers)




