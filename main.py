def unique(n):
    k=0
    while n!=0:
        k+=n%10
        n//=10
    n=k
    return n
    
a="bharath786"
n=0 
s=""
for i in a:
    if i.isdigit():
        n+=int(i)
    else:
        s+=i
print(s)

if n<10:
    print(n)
else:
    print(unique(n))