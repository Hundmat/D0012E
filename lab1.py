import time
import random
import matplotlib.pyplot as plt
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr
 
 
def merge(arr): #This function is recursive function that will divide a array until only one object is left
    n= len(arr)
    if(n==1):
        return arr
    arrayLeft=arr[:n//2] #take the left side of the array if you split it in half

    arrayRight=arr[n//2:]#take the right side of the array if you split it in half
    
    arrayLeft=merge(arrayLeft) #recall the function with the "left" array
    arrayRight=merge(arrayRight) #recall the function with the "right" array
    
    
    return bSort(bSort(arrayLeft)+bSort(arrayRight))
     



""" def merge_sort(arrayLeft,arrayRight):
    
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
   
    return merge_array """
import math

def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1

    while high - low > 1:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
        
    if x < arr[high] & x > arr[low]:
        # print("1")
        return low
    elif x < arr[low]:
        # print("2")
        return low - 1
    elif x > arr[high]:
        # print("3")
        return high + 1
    # print("4")
    return low

def bSort(arr):
    for i in range(1, len(arr)):
        
        if arr[i] < arr[i - 1]:
            index = binarySearch(arr[0:i], arr[i])
            # print(index + 1, arr, arr[i])
            arr.insert(index + 1, arr[i])
            arr.pop(i + 1)
    return arr

def mergeSort(arr, k, func):

    lists = []

    for i in range(0, len(arr)):
        if i % k == 0:
            lists.append(func(arr[i:i+k]))

    print(lists)
    

# print(output)

        








def random_array(n):
    arr_rm=[]
    for i in range(0,n):
        arr_rm.append(random.randint(-100,100))
    return arr_rm

def sorted_array(n):
    arr = random_array(n)
    return bSort(arr)


def tester(n):
    total_time=0
    rm_array=random_array(n)
    start= time.perf_counter()
    insertionSort(rm_array)
    end= time.perf_counter()
    total_time=(end-start)  
    #print((total_time)," sekunder")
    return total_time

def graph_creater(graph_inf):
    x_ax=[]
    y_ax=[]
    for x,y in graph_inf.items():
        x_ax.append(int(x))
        y_ax.append(float(y))
    print(x_ax)
    print(y_ax)
    plt.plot(x_ax, y_ax)
    plt.show()
def main():
    graph_inf={}
    for x in range(1,20):
        
        total_time=0
        #print("10 tests with size ",arg)
        for i in range(1,20):
           total_time+= tester(x)
        #print("Average time for 10 tests with size ",arg,"= ",total_time/arg)
        graph_inf[x]=(total_time/20)
        graph_inf=dict(sorted(graph_inf.items()))
    graph_creater(graph_inf)

    
main()