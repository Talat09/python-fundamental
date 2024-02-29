#list methods
numbers=[1,8,12,10,2,3,4,5,6,7,9]
numbers.append(11)  # adds one element at at end
print(numbers)

numbers.insert(3,13)  # adds one element  at 3 no position old all elements present here just shift 1 position to right
print(numbers)

numbers.remove(11)  # removes the first element with value 11
print(numbers)

numbers.pop()  # removes the last element
print(numbers)

numbers.pop(3)  # removes the element at 3 position
print("removes the element at 3 position:",numbers)

numbers.sort()  # sorts the list
print("sorts the list ascending order:",numbers)#sorts in ascending order

numbers.sort(reverse=True)  # sorts the list
print("sorts the list descending order:",numbers)#sorts in ascending order

numbers.reverse()  # reverses the list
print("reverses the list: ",numbers)