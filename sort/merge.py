# coding: UTF-8
# マージソート

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
        # 配列を中央で分割
    center = len(numbers) // 2 
    #左側の配列
    left = numbers[:center]
    # 右側の配列
    
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
# i == 左配列のインデックス 番号を管理
# j == 右配列のインデックス 番号を管理

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    return numbers

if __name__ == '__main__':
    nums = [5,4,1,8,7,3,2,9]
    print(merge_sort(nums))





