orders=[
        [1,"2-2-2022",10],
        [2,"2-2-2022",20],
        [2,"2-2-2022",30],
        [1,"2-2-2022",40],
        [1,"2-2-2022",50],
        [2,"2-2-2022",60],
        ]

'''
l1,l2=0,0
n=len(orders)

for i in range(n):
    if (orders[i][0]==2):
        if(orders[i][2]>=l2 and orders[i][2]<=l1):
            l2=orders[i][2]
        if(orders[i][2]>l1):
            l1=orders[i][2]
        
'''

        
#print(l1,l2)

#O(k * n)

orders=[
        [1,10],
        [2,20],
        [2,30],
        [1,40],
        [1,50],
        [2,60],
        ]
#[1,50,40],[1,40,10],[1,10,0]

a=[i[1] for i in orders if i[0]==1]
print(a)
a.sort(reverse=True)
print(a)
n=len(a)
ans=[]
userid=1
for i in range(n):
    if(i==n-1):
        ans.append([userid,a[i],0])
        break
    j=i+1
    ans.append([userid,a[i],a[j]])
    
print(ans)

