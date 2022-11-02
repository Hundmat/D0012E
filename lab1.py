import time
import random
import matplotlib.pyplot as plt
import math


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


def random_array(n):                                        #creates a array with random numbers from -100 to 100 with a size of n
    arr_rm=[]
    for i in range(0,n):
        arr_rm.append(random.randint(-100,100))
    return arr_rm

def sorted_array(n):
    arr = random_array(n)
    return bSort(arr)


def tester(n):                                              #test the algorithm with a random array with a size of n
    rm_array=random_array(n)
    start= time.perf_counter()                              #check time before call of algorithm
    insertionSort(rm_array)
    end= time.perf_counter()                                #check time after call of algorithm
    return end-start

def graph_creater(graph_inf):                               #Create a graph that represent the data that we collect in main
    x_ax=[]
    y_ax=[]

    for x,y in graph_inf.items():                           #create x and y axis
        x_ax.append(int(x))
        y_ax.append(float(y))

    plt.plot(x_ax, y_ax)
    plt.show()

def main():
    graph_inf={}

    for size in range(1,500):                               #For loop that test the algorithm that gets an input with the size of 1-xxx
        
        total_time=0
        for i in range(1,100):                              #For loop that test the algorithm x times that gets an input with the size created before 
           total_time+= tester(size)                        #collect the total time

        graph_inf[size]=(total_time/100)                    #bind the avarge time to the size
        graph_inf=dict(sorted(graph_inf.items()))           

    graph_creater(graph_inf)

    
main()