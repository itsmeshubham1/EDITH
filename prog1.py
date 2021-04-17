A=[]
n=int(input("n= "))
for i in range(1,n+1,1):
    d=int(input())
    A.append(d)
                 
B=int(input("B= "))
count=0
for i in range(0,n+1):
    if((A[i]-A[i+1]<=B) and (A[i+1]-A[i+2]<=B) and (A[i]-A[i+2]<=B)):
        count=count+1
print(count)
        
