def linearSearch(arr , target):
    for x in range(len(arr)):
        if arr[x] == target:
          return "The found position is {f}".format(f=x)
          
    return "None"
arr = [4, 2, 5, 9, 1, 3]
target = 1
print(linearSearch(arr, target))