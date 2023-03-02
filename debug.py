arr2 = [4, 2, 1]

def shellSort(arr):
    n = len(arr)
    dist = n//2
      
    while dist > 0:
        j = dist
        while j < n:
            i = j - dist
            while i >= 0:
                if arr[i+dist] > arr[i]:
                    break
                else:
                    arr[i+dist],arr[i]=arr[i],arr[i+dist]
                i=i-dist
            j+=1
        dist=dist//2

shellSort(arr2)