
for i in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().split()))   
    print(n-arr.count(min(arr)))
    
