def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("Back Call "+str(n))

show(5)    