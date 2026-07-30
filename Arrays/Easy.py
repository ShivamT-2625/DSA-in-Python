nums = [ 4,3,7,1,8,10,2,4]

# def numsSortedornot(nums):
#     if not nums :
#         return True
#     for i in range (0,len(nums)-1):
#         if nums[i] > nums [i+1]:
#             return False
        
#     return True
            

                
    
# def secondLargest(nums):
#     if not nums :
#         return 0
#     nums.sort()
#     print(nums[-2])
# secondLargest(nums)

# def secondLargest(nums):
#     if not nums:
#         return None
#     first = float("-inf")
#     second = float("-inf")

#     for key in nums:
#         if key > first:
#             second=first
#             first = key
#         elif key > second and key != first:
#             second = key
#     if second == float("-inf"):
#             return None
#     print(second)

# secondLargest(nums)



#Linear search 
# def Linearsearch(nums , target):
#      if not nums:
#           return None
#      for key in range(0,len(nums)) :
#           if nums[key] == target:
#                return key
#      return -1
          
# print(Linearsearch(nums , 7))

nums2 = [1,2,3,4,6,7,8,9]

# def missingNumber(nums):
#     if not nums:
#         return 0
#     actual_sum = sum(nums)
#     calculated_sum = ((len(nums)+1)*(len(nums)+2))//2

#     missing = calculated_sum - actual_sum
#     return missing
# print(missingNumber(nums2))

# nums_3 = [4,5,8,10]

# def union_of_sorted(nums,nums1):
#      if not nums and nums1:
#           return 0
#      set_s = set(nums+nums1)
     
#      return set_s

# print(union_of_sorted(nums2,nums_3))

[7, 10, 4, 10, 6, 5, 2]
