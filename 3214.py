s = int(input())
d = 0 
h = 0 
m = 0 
while s > 0:
    if s >= 86400:
        d +=1 
        s -= 86400
    elif s >= 3600:
        h +=1 
        s -= 3600
    elif s >= 60:
        m +=1 
        s -= 60
    else:
        break
print(d)
print(h)
print(m)
print(s)