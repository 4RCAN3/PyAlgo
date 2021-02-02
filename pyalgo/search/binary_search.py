#Iterative Implementation of the Binary Search Algorithm using Python
#Time Complexity: O(log(N))

#Approach:
#In each iteration, check if the current middle element of the array is on the right, left or, is more than or less than the "Value to be searched for".
#If it is less than the "Value to be searched for", simply iterate over the right hand side of the array, that is from "mid...n-1".
#If it is more than the "Value to be searched for", simply iterate over the left hand side of the array, that is from "0...mid".
#If the arr[mid] is the same as the "Value to be searched for", simply return the index of the current element.

#If after all of the iterations, no element was found to be of the exact match, simply return -1.

def bin_search(arr, left, right, x):
    while left <= right:
        mid = left + ((right-left)//2)
        if arr[mid]<x:
            left = mid
        elif arr[mid]>x:
            right = mid
        else:
            return mid
    return -1

#Enter the elements present in the array
arr = list(map(int, input().split()))
#Binary Search works only on sorted arrays, so if the array was unsorted before, sorting now.
arr.sort()
n = len(arr)
#Enter the value you need to search for in the array
value_to_be_searched_for = int(input())
#The binary search function is now called with left = 0, and right = n-1
result = bin_search(arr, 0, n-1, value_to_be_searched_for)
if result > -1:
    print(f"The Element was present in the Array at the index, {result+1}.")
else:
    print(f"The Element is not present in the Array.")
