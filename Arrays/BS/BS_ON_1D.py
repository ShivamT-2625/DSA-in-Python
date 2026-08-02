#Binary search on 1-D array
# arrayyy =[23,45,12,24,45]
# arr_sorted=[11,12,34,54,67]
# def lower_bound(arr:list,key:int):
#     if arr is None:
#         return None
#     left = 0
#     right = len(arr)-1
#     while left < right:
#         mid = (left+right)//2
#         if arr[mid] > key:
#             right = mid 
        
#         else:
#             left = mid
#     return left
# print(lower_bound(arr_sorted,13))


#basic question of binary search 
# arr_=[2,3,4,5,6,7,8,10]

# def binary_search(arr:list,key:int):
#     if arr is None:
#         return None
#     low = 0
#     high = len(arr)-1
#     while low <= high:
#         mid = (low + high) //2
#         if arr[mid] > key :
#             high = mid-1
#         elif arr[mid] < key:
#             low = mid + 1
#         else:
#             return mid
#     return -1
# print(binary_search(arr_,7))

#recursive solution 

from turtle import up


def recursive(arr:list,low,high,key:int):
    if low > high :
        return -1 
    mid = (low+high)//2
    if arr[mid] > key:
        return recursive(arr,low,mid-1,key)
    elif arr[mid] == key:
        return mid
    else:
        return recursive(arr,mid+1,high,key)

arr = [1, 3, 5, 7, 9, 11]

# print(recursive(arr, 0, len(arr) - 1,7))  # 3
# print(recursive(arr, 0, len(arr) - 1,6) )  # -1

def lower_bound(arr:list,key:int):
    if arr is None:
        return None
    low = 0
    ans=len(arr)-1
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid]<key:
            low =mid+1
        elif arr[mid]>=key:
            high = mid-1
            ans=mid
    return ans

def lower_bound_recursive(arr:list,key:int,low,high):

    if low > high:
        return low
    mid = (low+high)//2
    if arr[mid]<key:
        return lower_bound_recursive(arr,key,mid+1,high)
    elif arr[mid]>=key:

        return lower_bound_recursive(arr,key,low,mid-1)
    
print(lower_bound_recursive(arr,7,0,len(arr)-1))

# def upper_bound_recursive(arr:list,key:int,low,high):
#     if low > high:
#         return low
#     mid = (low+high)//2
#     if arr[mid] <= key:
#         return upper_bound_recursive(arr,key,mid+1,high)
#     else:
#         return upper_bound_recursive(arr,key,low,mid-1)
# print(upper_bound_recursive(arr,7,0,len(arr)-1))


arr_4 = [ 2,3,5,7,19,20]

def lower_bound_problem(arr:list,key:int , low ,high):
    if not arr:
        return None
    ans = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid]<key:
            low = mid + 1
        elif arr[mid] >= key:
            high = mid - 1
            ans = mid
        else :
           ans = mid
    return ans 
print(lower_bound_problem(arr_4,7,0,len(arr_4)-1))

def upper_bound_problem(arr:list,key:int,low,high):
    if not arr:
        return None
    ans = -1
    while low <= high :
        mid = (low + high)//2
        if arr[mid] <= key:
            low = mid+1
        else:
            high = mid -1
            ans = mid 
    return ans

print(upper_bound_problem(arr_4,7,0,len(arr_4)-1))

def lower_bound_rec(arr:list,key:int,low,high)->int:
    if low > high :
        return low 
    mid = (low + high)//2
    if arr[mid]< key:
        return lower_bound_rec(arr,key,mid+1,high)
    else:
        return lower_bound_rec(arr,key,low,high-1)
print(lower_bound_rec(arr_4,7,0,len(arr_4)-1))


def upper_bound_rec(arr,key,low,high):
    if low > high :
        return low
    mid = (low + high )//2
    if arr[mid] <= key:
        return upper_bound_rec(arr,key,mid+1,high)
    else:
        return upper_bound_rec(arr,key,low,mid-1)
print(upper_bound_rec(arr_4,7,0,len(arr_4)-1))