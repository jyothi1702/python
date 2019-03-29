# import copy
li=["name","age","id","name","emp","ram","name"]
#
# li1 = copy.copy(li)
# #li1.append("rajjjj")
# li[0]="suraj"
# print(li)
# print(li1)

# for i in li:
#     if(i=="id"):
#         print("If Stmt",i)
#     else:
#         print("else Stmt",li)

# l1=[1,2,4]
# di={}
# for i in li:
#     l=li.index(i)
#     di[i]=l
# print(di)

#li1=set(li)
# for i in li1:
#     li2=li.count(i)
#     print("%s is:%d times"%(i,li2))
# di={}
# for i,j in li:
#     di.setdefault(i,[]).append(j)
#     print(di)
# li=[1,22,33,2,3,4,56,56,78]
#
# ll=[l for l in li if(l%2==0)]
# print(ll)
# re=zip(li,l1)
# l=list(re)
# print(l)
# di=dict((k,v) for k,v in zip(li[::2],li[1::2]))
# print(di)

def get(li):
    count1=0
    print(li)
    for i in li:
        if i=="name":
            count1=count1+1
    return count1

cou=get(li)
print(cou)

