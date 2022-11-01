import time
def insertionsort(arr):
   return
def merge(arr):
    final=[]
    n= len(arr)
    if(n==1):
        return arr
    arrayLeft=arr[:int(n/2)]
    arrayRight=arr[int(n/2):]
    
    arrayLeft=merge(arrayLeft)
    arrayRight=merge(arrayRight)

    return merge_sort(arrayLeft,arrayRight)

def merge_sort(arrayLeft,arrayRight):
    
    n=1
    merge_array=[]
    while n<=len(arrayLeft) and n<=len(arrayRight):
        if arrayLeft[n-1]>arrayRight[n-1]:
            merge_array.append(arrayRight[n-1])
            arrayRight.pop(n-1)
        else:
            merge_array.append(arrayLeft[n-1])
            arrayLeft.pop(n-1)
        n+=1
        
        
    while n<=len(arrayLeft):
        merge_array.append(arrayLeft[n-1])
        arrayLeft.pop(n-1)
        n+=1
    while n<=len(arrayRight):
        merge_array.append(arrayRight[n-1])
        arrayRight.pop(n-1)
        n+=1
   
    return merge_array







def main():
    total_time=0
    n=0
    array = [233,3,4,51,6,7,434]
    
    start= time.perf_counter()
    print(merge(array))
    end= time.perf_counter()
    total_time=(end-start)

        
    print((total_time)," sekunder")
main()