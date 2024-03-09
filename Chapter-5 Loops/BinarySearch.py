arr = [2, 3, 4, 10, 40]
target = 10

left = 0
right = len(arr) - 1

while left <= right:
    print("left:",left)
    print("right:",right)
    mid = (left + right) // 2
    print("mid:",mid)   
    # Check if target is present at mid
    print("arr[mid]:",arr[mid])
    if arr[mid] == target:
        print("Element is present at index", mid)
        break
    # If target is greater, ignore left half
    elif arr[mid] < target:
        left = mid + 1
    # If target is smaller, ignore right half
    else:
        right = mid - 1
else:
    print("Element is not present in array")
