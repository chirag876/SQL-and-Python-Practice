def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] # The element to be sorted
        j = i-1 # comparing the index with previous one
        
        while j>=0 and arr[j]>key: # looping until we are getting the max element
            arr[j+1] = arr[j] # shifting forward one step
            j -=1 # comparing the index with the next one
        arr[j+1] = key # keeping the element at the correct position
    return arr

nums = [5, 6, 8, 3 ,1, 0]
print("Sorted:", insertion_sort(nums))