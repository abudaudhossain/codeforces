

for i in range(0, int(input())):
    n =int(input())
    arr = list(map(int, input().split()))
    arr.sort()
  
    print(arr)

    a = arr[0]
    min = abs(a)
    ans = 1
    for s in range(1, len(arr)):
        b = arr[s]
        print(b)
        if(b > min):
           break
        else:
            a = b
            min = abs(b - a)
            print(f'min:{min}')
            ans = s

    print(ans+1)
