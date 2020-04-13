# cook your code here
import math as m
import random as r
c = []

def dist(p1,p2):
    return m.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def mod(x):
    if x<0:
        return -1*x
    else: 
        return x
def diff(p1,p2):
    return mod(p1[0]-p2[0]+p1[1]-p2[1])
def center(a):
    for i in a:
        global c
        c.append(((i[0]+i[2])/2,(i[1]+i[3])/2))
    return 0
                
def allfour(l):
    
    x2 = (l[0],l[3])
    x3 = (l[1],l[2])
    x1 = (l[0],l[1])
    x4 = (l[2],l[3])
   
    return [x1,x3,x4,x2]
def minn(a):
    m = mini([a[0]]+[a[1]])
    d = []
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j and (i,j) not in d:
                d.append((i,j))
                b = [(a[i])] + [(a[j])]
                
                c = mini(b)
                
                if c!=-1 and c<m:
                    m = c
                elif m == -1 or m==0:
                    m = c
            
    return m
def check(r1,r2):
    l1 = r1[0]-r1[2]
    b1 = r1[1]-r1[3]
    l2 = r2[0]-r2[2]
    b2 = r2[1]-r2[3]
    if l1>l2 and b1>b2:
        if r1[0]>r2[0] and r1[0]<r2[3] and r1[3]< r2[3] or r1[0]<r2[0] and r1[0]>r2[3] and r1[3]<r2[3]:
            return 1
        else: return 0
    elif l1>l2 and b1>b2:
        if r2[0]>r1[0] and r2[0]<r1[3] and r2[3]< r1[3] or r2[0]<r1[0] and r2[0]>r1[3] and r2[3]<r1[3]:
            return 1
        else: return 0
def diff1(x1,x2):
    return mod(x2-x1)
            
def mini(a):
    
    
    x = 0
    y = 1
    r1 = allfour(a[x])
    r2 = allfour(a[y])
    
    if 1:
        l1 = a[x][0]-a[x][2]
        b1 = a[x][1]-a[x][3]
        l2 = a[y][0]-a[y][2]
        b2 = a[y][1]-a[y][3]
        
        if((l2-l1)*(b2-b1)>=0):
            if check(a[x],a[y]):
                m = diff1(a[x][0],a[y][0])
                if m>diff1(a[x][1],a[y][1]):
                    m = diff1(a[x][1],a[y][1])
                elif m>diff1(a[x][2],a[y][2]):
                    m = diff1(a[x][2],a[y][2])
                elif m>diff1(a[x][3],a[y][3]):
                    m = diff1(a[x][3],a[y][3])
                return m
            
            m = diff(r1[0],r2[0])
            if m> diff(r1[1],r2[1]):
                m = diff(r1[1],r2[1])
            elif m> diff(r1[2],r2[2]):
                m = diff(r1[2],r2[2])
            elif m>diff(r1[3],r2[3]):
                m = diff(r1[3],r2[3])
            return m
        
    return -1
    
   





t  = int(input())
for i in range(t):
    n = int(input())
    a = []
    for j in range(n):
        a.append(list(map(int,input().split(' '))))
    center(a)
    ans = minn(a)
    print(ans)
    del n,a,c
    c = []
'''
0 0 4 1
-1 1 1 2
2 1 5 2'''
