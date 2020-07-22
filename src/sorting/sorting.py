# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a = 0
    b = 0
    print(f"{merged_arr} <----- nothing done yet")
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            merged_arr.pop(0)
            a += 1
        else:
            merged_arr.append(arrB[b])
            merged_arr.pop(0)
            b += 1

            # check both arrays to see if the pointer is still in range of its array
    if a < len(arrA):
        # arrA still has leftover elements 
        # push them all to the merged array 
        left_over = len(arrA[a:])
        merged_arr.extend(arrA[a:])
        for a in range(left_over):
            print(f"just curious : {a}")
            merged_arr.pop(0)

    if b < len(arrB):
        left_over = len(arrB[b:])
        merged_arr.extend(arrB[b:])
        for a in range(left_over):
            print(f"just curious : {a}")
            merged_arr.pop(0)

    return merged_arr

arrA = [3, 6, 8, 12, 15]
arrB = [1, 4, 5, 9, 11]
print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 : ])

        arr = merge(left, right)


    return arr

# arr = [45, 12, 89, 14, 67, 45, 23, 90, 11]
# print(merge_sort(arr))