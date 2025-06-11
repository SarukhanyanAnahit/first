# 4.2
# def count(l):
#     if not l:
#         return 0
#     return 1+count(l[:-1])
#
# print(count([14, 2, 8 , 9, 40, [1, 8], (7,9)]))

# 4.3
# def maximus(ls):
#     if len(ls)==1:
#         return ls[0]
#     return max(ls[0],maximus(ls[1:]))
#
# print(maximus([1, 2, 8 , 9, 40, 77,9]))

#4.4
# def binary_search(ml, target):
#     low = 0
#     high = len(ml) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if ml[mid] == target: #bazayin
#             return mid
#         if ml[mid] > target: #rekursiv
#             high = mid
#         else:
#             low = mid
#     return None #bazayin