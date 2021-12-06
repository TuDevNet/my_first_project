#list

a = [[n,n*1,n*2] for n in range (1,4)]
print(a)

b = list('Nguyen Tu')
print(b) 

c= a + b
print(c)

#check whether a member belongs to a list or not
check = 'T' in b 
print(check) 

#choose one member in a list
d = [1,2,3,'a','b',[4,5]]
e = d[0]
f = d[5][0] 
g = d[0:3] #3 is length of list g
print(e)
print(f)
print(g)

#Matrix
h = [[1,2,3],[4,5,6]]
i = h[0]
k = h[1]
print(i)
print(k)
