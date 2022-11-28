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

def dc_smallest(arr):#3*(2T(n/2))=O(n)
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

def cross_Maxvalue(low_arr,high_arr):#O(n/2)+O(n/2)=2*O(n/2)
    leftSum= -sys.maxsize
    sum=0
    for i in range(len(low_arr)-1,-1,-1):#O(n/2)
        sum += low_arr[i]
        if sum>leftSum:
            leftSum=sum
    rightSum= -sys.maxsize
    sum=0
    for i in range(0,len(high_arr)): #O(n/2)
        sum += high_arr[i]
        if sum>rightSum:
            rightSum=sum
    return leftSum+rightSum

def maxSum(arr):                                                #2T(n/2)+O(n/2)+O(n/2)=O(n)+O(n/2)+O(n/2)=O(n)
    n=len(arr)
    if(n==1):
        return arr[0]

    #Divide array, left and right 
    left_arr=arr[:n//2]
    right_arr=arr[n//2:]

    #Call maxSum but for the two arrays
    maxSumL =maxSum(left_arr)                                   #O(n/2)
    maxSumR =maxSum(right_arr)                                  #O(n/2)
    
    #start values
    leftSum=left_arr[0]
    sum=0

    #Going from end of the left array (middle) inward findning the largest sum
    for i in range(len(left_arr)-1,-1,-1):                      #O(n/2)
        sum += left_arr[i]
        if sum>leftSum:
            leftSum=sum

    #Going from start of the right array outward findning the largest sum      
    rightSum= right_arr[0]
    sum=0
    for i in range(0,len(right_arr)):                           #O(n/2)
        sum += right_arr[i]
        if sum>rightSum:
            rightSum=sum

    
    maxCross= leftSum+rightSum

    #Return the max value of the three inputs
    return max(maxSumL,maxSumR,maxCross)


def random_array(n):                                        #creates a array with random numbers from -100 to 100 with a size of n
    arr_rm=[]
    for i in range(0,n):
        arr_rm.append(random.randint(-100,100))
    return arr_rm

def main():
    r_arr=random_array(8)

   
    print(r_arr)
    print(maxSum(r_arr))

main()