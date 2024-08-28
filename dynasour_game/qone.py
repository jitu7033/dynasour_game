# #smallest and largest in python:
#
# arr = [20,20,30,40]
# max = arr[0]
# min = arr[0]
# for i in range(len(arr)):
#     if arr[i] < min:
#         min = arr[i]
#     elif arr[i] > max:
#         max = arr[i]
# print(min,max)
#
#
#
# # smallest and largest by function
#
# def smalllarg(arr):
#     min = arr[0]
#     max = arr[0]
#     for i in range(len(arr)):
#         if arr[i] < min:
#             min = arr[i]
#         elif arr[i] > max:
#             max = arr[i]
#     print(min,max)
#     return
# n = int(input())
# arr = []
# for i in range(n):
#     c = int(input())
#     arr.append(c)
# smalllarg(arr)
#
#
#
# # missing number in python:
# arr = [1,2,4,5,6]
# n = len(arr)+1
# sum = n*(n+1)/2
# restsum = 0
# for i in range(len(arr)):
#     restsum+=arr[i]
# missingNumber = sum-restsum
# print(int(restsum))
#
#
#
# # missing number in python by function :
#
# def missingNumber (arr):
#     l = len(arr)+1
#     sum = l*(l+1)/2
#     restsum = 0
#     for i in range(len(arr)):
#         restsum += arr[i]
#     print(missingnumber)
#     return
# n = int(input())
# arr = []
# for i in range(n):
#     c = int(input())
#     arr.append(c)
# missingnumber = sum-restsum
# missingNumber(arr)
#
#
#
# # find second largest value in python
#
# arr = [10,34,56,43,23,59]
# highest = 0
# SecondHighest = 0
# for i in range(len(arr)):
#     if arr[i] > highest:
#         SecondHighest = highest
#         highest = arr[i]
#     elif arr[i] > SecondHighest and arr[i] != highest:
#         SecondHighest = arr[i]
# print(SecondHighest)
#
# # find 2nd largest using fumction:
#
# def secondhighest(arr):
#     highest = 0
#     secondhighest = 0
#     for i in range(len(arr)):
#         if arr[i] > highest:
#             secondhighest = highest
#             highest = arr[i]
#         elif arr[i] > SecondHighest and arr[i] != highest:
#             secondhighest = arr[i]
#     print(secondhighest)
#     return
# arr = [10,20,56,89,87]
# secondhighest(arr)

# second lowest using python
# arr = [10,20,56,4,9,10,78,96]
# smallest = 0
# for i in range(len(arr)):
#     if arr[i] > arr[i-1]:
#         smallest = arr[i]
# print(smallest)





# arr = [20,56,4,9,2,10,78,96,75]
# smallest = min(arr[0],arr[1])
# secondsmallest = min(arr[0],arr[1])
# for i in range(len(arr)):
#     if arr[i] < smallest:
#         secondsmallest = smallest
#         smallest = arr[i]
#     elif arr[i] < secondsmallest and arr[i] != smallest:
#         secondsmallest = arr[i]
# print(secondsmallest)

#
# arr = [11,20,10,40,40,90,90]
# count = 0
# for i in range(len(arr)):
#     if arr[i] == arr[i-1]:
#         count = count+1
# if count%2!=0:
#     print(count)


#check armstrong no
# //prime not

# n = int(input())
# for i in range(1,n):
#     if i>0:
#         for j in range(2,i):
#             if(i%j)==0:
#                 break
#         else:
#             print(i)

#
# arr = [10,20,4,9,8,7,6]
# ans = []
# n = len(arr)
# for i in range(len(arr)):
#     for j in range(i,n):
#         if arr[i]>=arr[j]:
#             ans[i] += arr[i]
# print(ans)
# n = int(input())
# def printIncresing(n):
#     if n==1:
#         print(1)
#         return
#     printIncresing(n-1)
#     print(n)


