def getMinMax(arr, low, high):

    if low == high:
        return arr[low], arr[high]
    elif low + 1 == high:
        arr_min = min(arr[low], arr[high])
        arr_max = max(arr[low], arr[high])
        return arr_min, arr_max

    else:
        mid = (low + high) // 2
        arr1_min, arr1_max = getMinMax(arr, low, mid)
        arr2_min, arr2_max = getMinMax(arr, mid+1, high)
        return min(arr1_min, arr2_min), max(arr2_max, arr1_max)


arrNumbers = [-10, 2, 3, -20]
mn, mx = getMinMax(arrNumbers, 0, len(arrNumbers)-1)
print(mn, mx)




