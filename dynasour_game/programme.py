# # def largestsum(li):
# #     n=len(li)
# #     m=len(li[0])
# #     maxindex=-1
# #     maxsum=-1
# #     for j in range(m):
# #         sum=0
# #         for i in range(n):
# #             sum+=li[i][j]
# #         if sum>=maxsum:
# #             maxsum=sum
# #             maxindex=j
# #     return maxsum , maxindex
# # li=[[1,2,3,],[4,5,6],[7,8,9]]
# # largestindex,largestsum=largestsum(li)
# # print(largestindex)
#
# #
# # def sum(li):
# #     n=len(li[0])
# #     m=len(li)
# #     maxindex=-1
# #     sum=-1
# #     for j in range(m):
# #         sum=0
# #         for in range(n):
# #
#
#         #  2D LIST
# li = [[1,2,3,4],[5,6,7,8],[9,1,2,3],[7,8,9,8]]
# print(li)
# print(li[2][2])
# li[2][3]= 40
# print(li)
#
# # list comprehension
#
#
# l1 = [10,20,50,9,12]
# new_list = []
# for ele in l1:
#     new_list.append(ele**2)
# print(new_list)
#
# new_list = [ele**2 for ele in l1 if ele%2==0 and ele%3==0]
# print(new_list)
#
# new_list = [ele for ele in l1 if ele%2==0 and ele%3==0]
# print(new_list)
#
#
# li_1 = [10,20,4,8]
# li_2 = [5,10,7,4,8]
# new_li = []
# for ele_1 in li_1:
#     for ele_2 in li_2:
#         if ele_1 == ele_2:
#             new_li.append(ele_2)
# print(new_li)
#
# li_1 = [10,20,4,8,9]
# li_2 = [5,10,7,4,8,9]
# new_li = [ele for ele in li_1 for ele_2 in li_2 if ele==ele_2 ]
# print(new_li)
#
# l3 = [1,2,3,4,5]
# new_list = [ele**2 if ele%2==0 else ele for ele in l3]
# # print(new_list)
#
# list = ["parikh","jitu","kanak"]
# new_list = [[s for s in ele]for ele in list]
# print(new_list)
#
#
# li = ["parakh","rohan","jitu"]
# list_2d = [[ s for s in ele] for ele in li]
# print(list_2d)
#
#
#
# # input 2d list in python
# # str = input().split()
# # n,m = int(str[0]),int(str[1])
# # l = [[int(j) for j in input().split()] for i in range (n)]
# # print(l)
# # print(l[2][5])
#
# # input jagged list in python
# #
# # n = int(input())
# # l = [[int(j) for j in input().split()] for i in range (n)]
# # print(l)
#
#
# #input a list in one line
# # 3 4
# # 1 2 3 4 5 6 7 8 9 10 11 12
#
# # str = input().split()
# # n,m = int(str[0]),int(str[1])
# # b = input().split()
# # l = [[int(b[m*i+j]) for j in range(m)]for i in range (n)]
# # print(l)
#
# # take list input inone line
# #3 4,,1 2 3 4 5 6 7 8 9 10 11  12
# # str = input().split()
# # n,m = int(str[0]),int(str[1])
# # b = str[2::]
# # l = [[int(b[m*i+j]) for j in range(m)]for i in range (n)]
# # print(l)
#
# #
# print()
# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# n = 3
# m = 4
# for i in range(n):
#     for j in range(m):
#         print(li[i][j],end=" ")
#     print()
#
# print()
# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# n = 3
# for i in li:
#     for ele in i:
#         print(ele,end=" ")
#     print()
#
# print()
# #join
# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# n = 3
# for i in li:
#     output = ' '.join([str(ele) for ele in i])
#     print(output)
#
# # 1 2 3 4
# # 5 6 7 8
# # 9 10 11 12
# array = []
# k = int(input())
# num = 1
# for i in range(1,k+1):
#     el = []
#     for j in range(1,k+1):
#         # print(num,end=" ")
#         el.append(num)
#         num = num+1
#     array.append(el)
# for i in range(len(array)):
#     print(array[i])
#
#
# arr=[]
# n=int(input())
# for i in range(n,0,-1):
#     el=[]
#     for j in range(2,i+1):
#         el.append(0)
#     el.append(1)
#     for j in range(n-i):
#         el.append(2)
#     arr.append(el)
# for i in range(len(arr)):
#     print(arr[i])






#
#
# def largestRowCol(arr):
#     rows = len(arr)
#     cols = len(arr[0])
#     sumRow = [0] * rows
#     sumCol = [0] * cols
#     for i in range(rows):
#         for j in range(cols):
#             sumRow[i] += arr[i][j]
#             sumCol[j] += arr[i][j] # Assume row 0 has maximum sum
#     l = ['row', 0, sumRow[0]]
#     for i in range(rows):
#         if sumRow[i] > l[2]:
#             l[2] = sumRow[i]
#             l[1] = i
#     for j in range(cols):
#         if sumCol[j] > l[2]:
#             l[2] = sumCol[j]
#             l[1] = j
#             l[0] = 'column'
#     return l
#
# m, n=(int(i) for i in input().strip().split(' '))
# l=[int(i) for i in input().strip().split(' ')]
# arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
# l=largestRowCol(arr)
# print()


