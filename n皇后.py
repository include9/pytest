#DEFINE,初始标记
n=4
#重置棋盘与标记
def Restart(n1=n):
    L=[([1] * n1) for i in range(n1)]
    alist=[i+1 for i in range(n1)]
    return L,alist
#打印棋盘1
def pr(L=[]):
    for arr1 in L:
        for arr in arr1:
            print('%3s'%arr,end='')
        print()
    print()  
#打印棋盘2
def pr2(L=[]):
    for arr1 in L:
        for arr in arr1:
            if arr==0:
                print('%3s'%arr,end='')
            else:
                print('%3s'%'',end='')
        print()
    print() 
#打印结果3
def pr3(L=[],n1=n):
    print("answer",end=":")
    cnt=0
    for i in range(n1):
        for j in range(n1):
            if L[i][j]==0:
                cnt+=1
    if cnt!=n1:
        return False           
    for i in range(n1):
        for j in range(n1):
            if L[i][j]==0:
                print('%3s'%str(j+1),end='')
    print("\n")
    
#下子
def aset(i,j,L=[([1] * n) for i in range(n)],n1=n):
    if L[i-1][j-1]!=1:
        return
    for ii in range(n1):
         L[ii][j-1]-=2
         L[i-1][ii]-=2
         if ii-i+j>=0 and ii-i+j<=n1-1:
             L[ii][ii-i+j]-=2
         if j+i-2-ii>=0 and j+i-2-ii<=n1-1:    
             L[ii][j+i-2-ii]-=2
    L[i-1][j-1]=0
#悔棋
def unset(i,j,L=[([1] * n) for i in range(n)],n1=n):
    for ii in range(n1):
         L[ii][j-1]+=2
         L[i-1][ii]+=2
         if ii-i+j>=0 and ii-i+j<=n1-1:
             L[ii][ii-i+j]+=2
         if j+i-2-ii>=0 and j+i-2-ii<=n1-1:    
             L[ii][j+i-2-ii]+=2
    L[i-1][j-1]=1
#递归函数
def k(L=[],alist=[],n1=n,n2=n):
    if n1==0:
        pr3(L,n2)
        pr(L)
        return
    for a in alist:
        if L[n1-1][a-1]==1:
            L1=L[:]
            alist1=alist[:]
            
            aset(n1,a,L1,n2)
            alist1.remove(a)
            k(L1[:],alist1[:],n1-1,n2)
            unset(n1,a,L1,n2)
            alist1.append(a)
#
def queen(num):
    print("-----------",num,"queen-----------")
    L1,a=Restart(num)
    k(L1,a,num,num)

if __name__=="__main__":
    queen(4)
