def prime():
    n=int(input("Num: "))
    if n<=1:
        print("not prime")
        return
    for i in range(2,n):
         if n%i==0:
            print("Not prime")
            return
    else:
        print("prime")
prime()
