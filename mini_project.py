import time
def multiply(F,M):
    x =  F[0][0]*M[0][0] + F[0][1]*M[1][0]
    y =  F[0][0]*M[0][1] + F[0][1]*M[1][1]
    z =  F[1][0]*M[0][0] + F[1][1]*M[1][0]
    w =  F[1][0]*M[0][1] + F[1][1]*M[1][1]
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w    
def power(F,n):
    if n is 0 or n is 1:
        return;
    M=[[1,1],[1,0]]
    power(F,n//2)
    multiply(F,F)
    if n%2 is 1:
        multiply(F,M)
def fib(n):
    F=[[1,1],[1,0]]
    if n is 0:
        return 0
    power(F,n-1)
    return F[0][0]    
n=int(input())
start=time.time()
k=fib(n)
end=time.time()
print("time elapsed is "+str(end-start))
print(k)
