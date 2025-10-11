while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
   
    dna = {}
    for _ in range(n):
        seq = input()
        if seq in dna:
            dna[seq] += 1
        else:
            dna[seq] = 1
      
    freq = [0] * (n + 1)
    for count in dna.values():
        freq[count] += 1
    for i in range(1, n + 1):
        print(freq[i])
    
    
        
        
    
        