import random as r, time as t

def generate_sorted_data(size):
    """
    generates and sorts array based on size
    """
    if size < 10:
        # Generate random data and sort with insertion sort for small datasets
        data = [r.randint(1, 100) for _ in range(size)]
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
    else:
        # generates a larger dataset and sorts it using merge sort
        data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [r.randint(1, 100) for _ in range(size - 10)]
        data = merge_sort(data)
    return data

def binary_search(sorted_array, target):
    '''
    takes array from generate_sorted_data function and using binary search, looks for and returns the index of the target value
    '''
    l, r = 0, len(sorted_array) - 1 #defining endpoints for searching array
    while l <= r: #to keep looping
        mid = (l + r) // 2
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] > target: #search left half
            r = mid - 1
        elif sorted_array[mid] < target: #search right half
            l = mid + 1
    return None

def merge_sort(arr):
    """sorts an array using merge sort
    """
    
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid]) # recursive call to merge_sort for left half
    right_half = merge_sort(arr[mid:]) # recursive call to merge_sort for right half
    
    # Merge the sorted halves
    sorted_array = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1
    
    # Add remaining elements
    sorted_array.extend(left_half[i:])
    sorted_array.extend(right_half[j:])
    
    return sorted_array



def linear_search(arr, target):
    """
        performs linear search on array to look for target value
    """   
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def main():
    target = int(input("give target value ")) # takes user input for target value
    size = int(input("give size of array ")) # takes user input for array size
    
    sorted_data = generate_sorted_data(size)
    
    if size >= 10:
        print("Phase 3 - Merge Sort Output (first 10 elements):", sorted_data[:10])
    else:
        print(f"sorted data is {sorted_data}")

    index = binary_search(sorted_data, target) #does the binary search
    if index is None:
        print(f"target {target} not found")
    else:
        print(f"target {target} found at index {index}")
    
    start_time = t.perf_counter() # calculates start time for linear search
    linear_search_result = linear_search(sorted_data, target) 
    end_time = t.perf_counter() #calculates end time for linear search
    linear_search_time = end_time - start_time #calculates total time elapsed for linear search function

    start_time = t.perf_counter() # calculates start time for binary search
    binary_search_result = binary_search(sorted_data, target)
    end_time = t.perf_counter() #calculates end time for binary search
    binary_search_time = end_time - start_time #calculates total time elapsed for binary search function
    
    print("Linear Search Time:", linear_search_time, "seconds")
    print("Binary Search Time:", binary_search_time, "seconds")

main()

""" Reflection:

    by choosing the suitable sorting algo, the searching speed can be increased 
    because binary search can be utilizied when sorted and it has a time complecity of o(log(n)) as opposed to linear search which is o(n)(which is slow for large datasets)
    binary search uses divide and cnquer while linear search goes one at a time whcih is timeconsuming for large datasets
    using an efficient sorting method like mergesort with time complexity O(n(log n) is faster than insertion sort (O(n^2)) with large data sets
    so it reduces time for sorting and total processing time since the search methods after sorting are efficient so it promotes boosts in performance
     
    """