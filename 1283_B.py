t = int(input())

for i in range(0, t):
    n , k = map(int, input().split())

    ans =int((int((n / k)) * k) + int((k/2)))
    if ans <= n:
        print(ans)
    else:
        print(n)
   
    
