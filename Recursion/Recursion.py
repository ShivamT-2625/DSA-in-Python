name = "Shivam"
# def recursive_call(name,k):
#     if k == 0:
#         return
#     print(name)
#     recursive_call(name,k-1)
# recursive_call("Tiwari",8)



# def linear_print(num,N):
    
#     if N < num:
#         return
#     print(num)
#     linear_print(num+1,N)
# linear_print(1,10)


# def reverse_print(num,N):
    
#     if N < num:
#         return
#     reverse_print(num+1,N)
#     print(num)
# reverse_print(1,10)

def factorial_que(N):
    if N == 1:
        return 
    factorial_que(N-1) * N
factorial_que(5)