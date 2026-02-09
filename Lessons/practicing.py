# n = 1221

# result = 0

# num=n

# while num>0:
#     lastd= num%10
#     result = result*10+lastd
#     num=num//10
# print(result)
# print(n)
# if(result == n):
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")

# def palindrome(n):
#     if(n == 0):
#         print("Number is palindrome")
#     num = n
#     result = 0
#     while(num>0): 
#         lastd=num%10
#         result =result*10 +lastd
#         num = num //10
#     if(result == n):
#         print("Number is a palindrome ")
#     else:
#         print("Number is not a palindrome")

# palindrome(789987)


# def ArmStrong(n): 
#     if(n == 0):
#         print("0")
#     num = n
#     x = str(n)
#     count = len(x)
#     result = 0
#     while(num> 0):
#         lastd =num%10
#         result = result + lastd**count
#         num = num//10
#     if(result == n):
#         print("Number is Armstrong")
#     else:
#         print("Number is not Armstrong")

# ArmStrong(93084)

nums = [ 3,4,5,5,6,7,3,5,8,9,2,3,5,8,1,9]
n =len(nums)
# freq_map={

# }

# for i in range(0,len(nums)):
#       if nums[i] in freq_map:
#         freq_map[nums[i]]+=1
        
#       else:
#           freq_map[nums[i]]=1
# print(freq_map)

hash_map={}
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)

