# TO-DO: Implement a recursive implementation of binary search
# Rule of thumb: any parameter that needs to be persisted across recursive calls
# The function signature is where the message gets passed down from the 
# delegator to the delegatee  
def binary_search(arr, target, left, right):
    # base case 
    # or we searched the whole array, i.e. when left > right
    if left > right:
        return -1
    # how do we move closer to a base case? 
    # we'll stop when we either find the target 
    else:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            # rule out the left side
            return binary_search(arr, target, mid + 1, right)
        else:
            # rule out the right side 
            return binary_search(arr, target, left, mid - 1)
    
# arr = [3, 4, 6, 16, 26, 28, 52, 55]
# print(binary_search(arr, 52, 0, len(arr)-1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def descending_binary_search(arr, target, left, right):
    # base case 
    # or we searched the whole array, i.e. when left > right
    if left > right:
        return -1
    # how do we move closer to a base case? 
    # we'll stop when we either find the target 
    else:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            # rule out the right side
            return descending_binary_search(arr, target, left, mid - 1)
        else:
            # rule out the left side 
            return descending_binary_search(arr, target, mid + 1, right)

# # arr = [101, 99, 87, 76, 66, 65]
# # print(descending_binary_search([101, 99, 87, 76, 66, 65], 5, 0, len(arr)-1))

def agnostic_binary_search(arr, target):
    # figure out whether the input array is sorted in ascending or descending order 
    # keep a boolean to indicate the order of the array 
    # compare arr[0] and arr[1] 
    if arr[0] > arr[-1]:
        is_ascending = False
    else:
        is_ascending = True

    # if the input array is ascending, call `binary_search` with the array and target 
    if is_ascending:
        return binary_search(arr, target, 0, len(arr) - 1)
    # otherwise, call `descending_binary_search` with the array and target 
    else:
        return descending_binary_search(arr, target, 0, len(arr) - 1)

print(agnostic_binary_search([1, 3, 5, 6, 8, 21], 8))
print(agnostic_binary_search([101, 101, 87, 76, 66, 65], 99))
