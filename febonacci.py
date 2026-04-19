# def fibonacci():
#     a=0
#     b=1
#     for _ in range(n):
#         print(a)
#         a=b
#         b=a+b
      
# n= int(input("Value of n :"))
# fibonacci()

def fibo():
    n=int(input("Number: "))
    a=0
    b=1
    for _ in range(n):
        print(a)
        a=b
        b=a+b
fibo()