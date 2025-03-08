def fun1(n):
    return n*(n+1)/2
print(fun1(5))

# 2nd way
def fun2(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
print(fun2(5))   
#3rd way
def fun3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,n+i):
            sum+=1
    return sum
print(fun3(5))        