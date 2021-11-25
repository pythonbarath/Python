# #Break

# for i in range(10):
#   if i == 7:
#     print("Loop Reached the Limit")
#     break
#   print(i)
# print("Outside The Loop")

# for i in range(10):
#   if i%2==0:
#     continue
#   print(i)

# for i in range(3):
#   for j in range(3):
#     if i == j:
#       break
#     print(i,j)


# cart = [10,20,30,40,50,800]

# for i in cart:
#   if i > 500:
#     print("Insurance Required ", i)
#     break
#   print("Proccessed Item",i)
# else:
#   print("Congrats successfully completed")

# x = int(input("enter the marks "))

# if x >= 35:
#   print("Passed")
# else:
#   pass

# x =10 
# del x
# print(x)

# n = int(input("Enter the Number: "))

# if n <=1:
#   print("It is Not a Prime Number")

# else:
#   is_prime = True
#   for i in range(2,n):
#     if n%i== 0:
#       is_prime = False
#       break
#   if is_prime == True:
#         print("It Is  Prime Number")
#   else:
#         print("It Is Not Prime Number")

# n= int(input("Enter the Number  "))
# count = 0
# n1 =2
# while True:
#   is_prime = True
#   for i in range(2,n1//2+1):
#     if n1%i ==0:
#       is_prime=False
#       break
#   if is_prime==True:
#     print(n1)
#     count= count+1
#   if count == n:
#     break
#   n1 = n1+1


s = input("Enter the String")
i = 0
for x in s:
  print("The char Present at +ve index:{} and at -ve index : {} is {}".format(i,i-len(s),x))
  i =i+1
  


   


  
