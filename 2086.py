while True:
    n1 = int(input())
    k = 0
    if n1 == -1:
        break
    nums = [n1]
    for i in range(999):
        x = int(input())
        nums.append(x)
    n = int(input())
    for j in nums:
        if n == j:
            k = k+1

    print(f'{n} appeared {k} times')