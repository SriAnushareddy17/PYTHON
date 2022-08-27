n=int(input())
for _i in range(n):
    a,b,c=map(int,input().split())
    d=(a+b)/2
    if(d>c):
     print("yes")
    else:
     print("no")
