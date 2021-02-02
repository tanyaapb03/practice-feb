# merge 2 sorted arrays

# given A=[]
# B=[]
# output- A=A+B

def mergearr(A,B,m,n): 
    
    while m >0 and n>0:
        if A[m-1]>B[n-1]:
            A[m+n-1]=A[m-1]
            m=m-1
        else:
            A[m+n-1]=B[n-1]
            n=n-1
    while n >0:
        A[m+n-1]=B[n-1]
        n=n-1
    
    return A

print(mergearr([2,4,5,6,9,0,0,0,0],[4,5,6,7],5,4))

