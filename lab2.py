import random
import sys
#--------------------------------------DEl 1------------------------------------ O(3n)=O(n)
def inc_smallest(arr,small_arr):

    if(len(small_arr)==3):
        return small_arr

    smallest=arr[0]
    index=0

    for i in range(1,len(arr)):
        if smallest>arr[i]:
            smallest=arr[i]
            index=i
    
    small_arr+=[smallest]
    arr=arr[:index]+arr[index+1:]

    return inc_smallest(arr,small_arr)

def dc_smallest(arr):
    n=len(arr)

    left_arr=arr[:n//2]
    right_arr=arr[n//2:]

    return merge(inc_smallest(left_arr,[]),inc_smallest(right_arr,[]))

def merge(left_arr,right_arr):
    combined_array=[]
    while 3>len(combined_array):
        if(left_arr[0]<right_arr[0]):
            combined_array+=[left_arr[0]]
            left_arr=left_arr[1:]
        else:
            combined_array+=[right_arr[0]]
            right_arr=right_arr[1:]
    return combined_array
#---------------------------------------------------------------------------------


#--------------------------------------DEl 2------------------------------------ O(n^2)

def cross_Maxvalue(arr,low,high,mid):
    leftSum= -sys.maxsize
    sum=0
    for i in range(mid,low-1,-1):
        sum += arr[i]
        if sum>leftSum:
            leftSum=sum
    leftSum= -sys.maxsize
    sum=0
    for i in range(mid+1,high+1):
        sum += arr[i]
        if sum>leftSum:
            leftSum=sum






def random_array(n):                                        #creates a array with random numbers from -100 to 100 with a size of n
    arr_rm=[]
    for i in range(0,n):
        arr_rm.append(random.randint(1,100))
    return arr_rm

def main():
    r_arr=[1,32,42,132,3,4,5,6,56]
   
    print(r_arr)
    print(inc_smallest([1,32,42,132,3,4,5,6,56],[]))
    print(dc_smallest([1,32,42,132,3,4,5,6,56]))

main()