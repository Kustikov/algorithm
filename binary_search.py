def binary_search (list, item):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = round((start + end) / 2)
        print(mid)
        quess = list[mid]
        if quess == item:
            return mid
        if quess > item:
            end = mid - 1
        else:
            start = mid + 1
    return None

my_list = [1, 3, 5, 7, 9, 10]

result = binary_search(my_list, 9)
print(result)

