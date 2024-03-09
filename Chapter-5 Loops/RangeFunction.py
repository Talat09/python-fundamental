#Range functions returns a sequence of numbers,starting from 0 by default, and increments by 1(by default) and stops before a specified number.
#range(5) return 0,1,2,3,4 start by default 0.step size increase.step size by default 1
#ending condition before 5

# print(range(5))
seq=range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
# print(seq[5]) index error range object index out of range
sequence=range(1,10,2)#range(start,stop,step)
for i in sequence:
    print("sequence:",i)