import random
import time
def printer(arr):
    for i in range(0,len(arr)):
        print("*"*arr[i])
        time.sleep(1)
    print("\n")
    return
    
    
def insertion_sort(arr):
    n  = len(arr)
    for i in range(1,n):
        printer(arr)
        key=arr[i]
        j =i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=key
    printer(arr)
    return arr

def merge(arr):
    n = len(arr)
    if(n==1):
        return arr
    
    left_arr=arr[:int(n/2)]
    right_arr=arr[int(n/2):]

    left_arr=merge(left_arr)
    right_arr=merge(right_arr)

    combined_array= merge_sort(left_arr,right_arr)
    printer(combined_array)
    return combined_array

def merge_sort(left_arr,right_arr):
    combined_array=[]
    
    while len(left_arr)>0 and len(right_arr)>0:
        if(left_arr[0]<right_arr[0]):
            combined_array.append(left_arr[0])
            left_arr.pop(0)
        else:
            combined_array.append(right_arr[0])
            right_arr.pop(0)

        
        
    while len(left_arr)>0:
        combined_array.append(left_arr[0])
        left_arr.pop(0)

    while len(right_arr)>0:
        combined_array.append(right_arr[0])
        right_arr.pop(0)
    
    return combined_array

def random_array(n):                                        #creates a array with random numbers from -100 to 100 with a size of n
    arr_rm=[]
    for i in range(0,n):
        arr_rm.append(random.randint(1,100))
    return arr_rm

def main():
    r_arr=random_array(10)
    print(r_arr)
    print(merge(r_arr))

main()
