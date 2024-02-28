#wap to print most repetated elements in a given string
'''s=input()
k={}
for i in s:
    if i in k:
        k[i]=k[i]+1
    else:
        k[i]=1
print(k)
m=max(k.values())
for v in k:
    if k[v]==m:
        print(v)'''
        
#wap to count number of special characters are present in given string        
'''s=input()
count=0
for i in s:
    if not i.isalnum():
        count+=1
print(count)'''
#wap to print how many times each and every character is present in given string
'''s=input()
d={}
for i in s:
    d[i]=s.count(i)
print(d) '''   
#wap to print how many times each and every characters is present in given string without using inbuild method
'''s=input()
d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d) '''       
        
    
    
