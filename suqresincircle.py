
def pd (x, y):
    return (2*x+1)**2 + (2*y+1)**2 <= 4*r**2

r =int(input())
count = 0
l = r-1

for i in range(1,r):
    while not pd(i,l):
        l -= 1
    count += l
    
count = 4*(r-1)+1+count*4
print(count)
