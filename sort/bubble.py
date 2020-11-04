# coding: UTF-8
#バブルソート
# from typing import List

def bubble_sort(numbers):
    len_numbers = len(numbers)
    # 配列の長さ分ループ
    for i in range(len_numbers):
        # 比較のため配列長さから一個分減らす
        for j in range(len_numbers -1 -i):
            if numbers[j] > numbers[j + 1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    return numbers


if __name__ == '__main__':

    nums = [2,5,1,8,7,3]
    print(bubble_sort(nums))