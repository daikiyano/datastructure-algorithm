# coding: UTF-8

# o(n log n)



def partition(numbers,low,high):
    i = low - 1
    pivot = numbers[high]
    for j in range(low,high):
        if numbers[j] <= pivot:
            i = i + 1
            numbers[i],numbers[j] = numbers[j],numbers[i]
    numbers[i+1],numbers[high] = numbers[high],numbers[i+1]
    return i + 1

pass

def quick_sort(numbers):
    def _quick_sort(numbers,low,high):
        if low < high:
            partition_index = partition(numbers,low,high)
            _quick_sort(numbers,low,partition_index -1)
            _quick_sort(numbers,partition_index +1,high)


    _quick_sort(numbers,0,len(numbers)-1)
    return numbers




if __name__ == '__main__':

    nums = [2,5,1,8,7,3]
    print(quick_sort(nums))