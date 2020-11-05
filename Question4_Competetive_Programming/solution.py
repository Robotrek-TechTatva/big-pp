def bouncy(n):
    return (sum(list(i) not in (sorted(i), sorted(i, reverse=True)) for i in map(str, range(1, n+1)))/n*100)

def f():
    count = 1
    percentage = 99
    step = 1000000
    while (bouncy(count)) <= percentage:
        count += step
    
    high = count
    low = count - step
    ans = (low+high)//2
    ans_percent = bouncy(ans)
    
    while ans_percent != percentage:
        if ans_percent > percentage:
            high = ans
        else:
            low = ans
        ans = (low+high)//2
        ans_percent = bouncy(ans)
    return ans