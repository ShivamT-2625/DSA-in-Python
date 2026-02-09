n=1221
num=n

# this is for getting reverse

# while num>0:
#     last_digit=num%10
#     print(last_digit)
#     num=num//10


# this is for counting the numbers
# empty = 0
# while num > 0:
#     last_digit=num%10
#     num=num//10
#     empty+=last_digit
# print(empty)


# this is for checking a palindrome
# empty=""
# while num > 0:
#     last_digit=num%10
#     num=num//10
#     empty+=f"{last_digit}"
    
# if empty == str(n):
#     print("Number is palindrome")

# else:
#     print("Number is not a palindrome")
# print(empty)



# this is for the armstrong number code
# nod = len(str(n))
# total = 0
# while num>0:
#     last_digit = num % 10
#     total+=last_digit**nod
#     num=num//10

    
# print(total)

# printing factors of a number

number=515
# brute force

# result=[]
# for i in range(1,number+1):
#     if number%i == 0:
#      result.append(i)
# print(result)

# better solution

# result1=[]
# for i in range(1,(number//2)+1):
#    if number%i == 0:
#       result1.append(i)
# print("Result1=",result1)

#optimal solution

# from math import sqrt
# result=[]
# for i in range(1,int(sqrt(number))):
#     if number%i==0:
#         result.append(i)
#         if number//i != i:
#          result.append(number//i)
# result.sort()
# print(result)
