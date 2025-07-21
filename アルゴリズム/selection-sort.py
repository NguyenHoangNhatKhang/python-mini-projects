def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):                     # bước qua từng vị trí
        min_idx = i                            # giả sử i là nhỏ nhất
        for j in range(i + 1, n):              # tìm phần tử nhỏ hơn trong phần còn lại
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # đổi chỗ
