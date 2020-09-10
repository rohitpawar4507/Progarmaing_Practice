# Display the given array in reverse order
#Initialize array     
arr = [1, 2, 3, 4, 5];     
print("Original array: ");    
for i in range(0, len(arr)):    
    print(arr[i])    
print("Array in reverse order: ");    
#Loop through the array in reverse order    
for i in range(len(arr)-1, -1, -1):     
    print(arr[i])
    
    
# Python code to remove duplicate elements 
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
duplicate = [2, 4, 10, 20, 5, 2, 20, 4] 
print(Remove(duplicate)) 

# Find second max element in given array
list1 = [11,22,1,2,5,67,21,32]
# to get unique elements
new_list = set(list1)
# removing the largest element from list1
new_list.remove(max(new_list))
# now computing the max element by built-in method?
print(max(new_list))

#4. Find sum of elements from given array and find average of all elements in array.
def sum_1(arr):
    result = sum(arr)
    return result
def Average(arr): 
    result = sum(arr) / 5
    return result
  
#average = Average(arr) 
  



# main function
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]

    print ('Average: {}'.format(Average(arr)))
    print ('sum_1: {}'.format(sum_1(arr)))
    
 # Check Arrays are disjoint or not( Two arrays are said to be disjoint if they have no elements in common).
def areDisjoint(set1, set2, m, n): 
    # Take every element of set1[] and search it in set2 
    for i in range(0, m): 
        for j in range(0, n): 
            if (arr1[i] == arr2[j]): 
                return False
  
    # If no element of set1 is present in set2 
    return True
  
  
#
arr1 = [12, 34, 11, 9, 3] 
arr2 = [7, 2, 1, 5] 
m = len(arr1) 
n = len(arr2) 
print("yes") if areDisjoint(arr1, arr2, m, n) else(" No") 


    
    
