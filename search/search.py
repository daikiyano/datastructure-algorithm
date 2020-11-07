
# coding: UTF-8

##bainary search

##左から順番に検索していくのでインデックス 分ループを回している
def linear_search(numbers,value):
    for i in range(0,len(numbers)):
        if numbers[i] == value:
            print(i)
            return i
    return -1


def binary_search(numbers,value):
    print("###########")
    left,right = 0, len(numbers) -1 
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1




if __name__ == '__main__':
     nums = [0,3,5,6,9,15]
     print(binary_search(nums,9))
