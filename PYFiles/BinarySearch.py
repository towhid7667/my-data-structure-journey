def binarySearch(arr , target):
    left = 0
    right = len(arr)
    
    while(left <= right):
        mid = (left + right) // 2
        if arr[mid] == target:
            return "The target is at {F}".format(F=mid)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1    
    return "Not found"     

arr = [1, 2,3,4, 5, 6, 7,8];
target = 7;
print(binarySearch(arr, target))   