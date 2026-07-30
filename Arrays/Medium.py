# leaders_num = [7, 10, 4, 10, 11, 5, 2]

# def Leaders(leaders):
#     if not leaders:
#         return 0
#     result=[]
#     last_greater = leaders[-1]
#     result.append(last_greater)
#     for key in range(len(leaders)-1,-1,-1 ):
#         if leaders[key] > leaders[last_greater]:
#             result.append(leaders[key])
#             last_greater = key

        
#     return result
# print(Leaders(leaders_num))


## Kadane algorithm

# Maximum Subarray Sum 


nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubarraysum(nums):
    if not nums :
        return None
    current_sum =nums[0]
    max_sum = nums[0]
    start=0
    temp_start=0
    end=0
    for i in range(1,len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]
        if current_sum > max_sum :
            max_sum = current_sum
            start=temp_start
            end = i
    return nums[start:end+1]
     
print(maxSubarraysum(nums))


