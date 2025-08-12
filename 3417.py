while True:
    n1 = int(input())
    k = 0
    if n1 == -1:
        break
    
    for i in range(10):
        x = int(input())
        
        if x == n1:
            k +=1
    print(f'{n1} appeared {k} times')
    
    
    
    
    
    
    