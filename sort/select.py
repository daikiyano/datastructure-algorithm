# coding: UTF-8


def selection_sort(numbers):
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i + 1, len_numbers):
        #小さい値を見つけた時入れ替え
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i],numbers[min_idx] = numbers[min_idx],numbers[i]
    return numbers

if __name__ == '__main__':

    nums = [2,5,1,8,7,3]
    print(selection_sort(nums))
