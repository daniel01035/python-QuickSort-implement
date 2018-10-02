#  best case = N log N  ||  average case = N log N  ||  worst case = N**2


def Partition(arr, front, end):  # Partition = 劃分 (陣列, 最前面的索引值, 最後面的索引值)
    pivot = arr[end]  # 找到樞紐，可以是任意一個數字
    i = front - 1  # i 代表的是小於樞紐的最後一位數字索引值
    for j in range(front, end):  # j 代表的是當前索引值
        if arr[j] < pivot:  # 從最前面開始找, 如果小於樞紐
            i += 1  # 代表指向大於樞紐的那堆數字最前面那個
            arr[i], arr[j] = arr[j], arr[i]  # 當前找到小於樞紐的數字與大於樞紐的最前面數字交換
    i += 1  # 代表指向大於樞紐的那堆數字最前面那個
    arr[i], arr[end] = arr[end], arr[i]
    return i


def QuickSort(arr, front, end):
    if front < end:
        pivot = Partition(arr, front, end)
        QuickSort(arr, front, pivot - 1)
        QuickSort(arr, pivot + 1, end)
        return arr


array = [9, 1, 10, 4, 2, 3, 7, 6, 8, 5]
print(QuickSort(array, 0, len(array) - 1))