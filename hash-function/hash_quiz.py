# coding: UTF-8



def get_pair(numbers,target):
    cache = set()
    for num in numbers:
        val = target - num
        # cacheの中から一致する数字を探す
        if val in cache:
            return val,num
        cache.add(num)
        # print(cache)

numbers = [11,2,5,9,10,3]
target = 12

print(get_pair(numbers,target))
