def f(n):
    count = 0
    for num in range(1, n+1):
        for b in range(2, num):
            if b**3 > num:
                break
            for a in range(2, num):
                if a**2 > num:
                    break
                elif (a**2)*(b**3) == num:
                    count += 1
                    break
    return count