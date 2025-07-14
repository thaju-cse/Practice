# def maxArea(height):
#     mx=0
#     l = len(height)
#     for i in range(0,l):
#         h1 = height[i]
#         w = 0
#         for j in range(i+1,l):
#             h2 = height[j]
#             w += 1
#             if h1 < h2:
#                 least_height = h1
#             else:
#                 least_height = h2
#             value = least_height*w
#             if value > mx:
#                 mx = value
#     return mx
# print(maxArea([1,8,6,2,5,4,8,3,7,873,6,7,8,9,0,4,3,2,1,2,3,4,5,6,7,78,87,76,5,4,34]))

# def canArrange(arr , k ):
#     l = len(arr)
#     #arrReminders = [None]*l
#     i = k
#     arrArrays = []
#     while i:
#         arrArrays.append([])
#         i -= 1

#     print(arrArrays)
#     for i in range(l):
#         value = arr[i]
#         if value < 0:
#             value *= -1
#         if value >= k:
#             value = value % k

#         #arrReminders[i] = value
#         arrArrays[value].append(value)
#         print(arrArrays)


#     start = 0
#     end = k
#     while start < end:
#         start += 1
#         end -= 1
#         print(start, end)
#         if (len(arrArrays[start]) != len(arrArrays[end])):
#             return False

#     return True

#print(canArrange([-1,1,-2,2,-3,3,-4,4],3))

# print(-10%3)
# a = -7
# b = 5
# 4546

# print(a % b)

# a = input()
# print(a)

from array import *

arr = array('i', [9,7,6,5,4,3,2])

print(arr)