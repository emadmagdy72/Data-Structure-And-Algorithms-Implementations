
# bottom up
def bottom_up_fibonacci(n):
    if n <= 1:
        return n
    else:
        arr = [0] * (n+1)
        arr[0] = 0
        arr[1] = 1
        for i in range(2, n+1):
            arr[i] = arr[i-1] + arr[i-2]

        return arr[n]


def top_down_fibonacci(n):
    arr = [-1] * (n+1)

    if arr[n] == -1:
        if n <= 1:
            arr[n] = n
        else:
            arr[n] = top_down_fibonacci(n-1) + top_down_fibonacci(n-2)
    return arr[n]


print(top_down_fibonacci(6))

