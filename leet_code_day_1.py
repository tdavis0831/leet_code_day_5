"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 """
 
 
 
nums = [1,2,3,1]
 
 
def contains_duplicate(nums):
    compare_list = []
    
    for x in nums:
        if x in compare_list:
            return True
        
        compare_list.append(x)
        
    return False

print(contains_duplicate(nums))





###################################################################################
nums = [1,2,3,4]
first_occurance= []
second_occurance = []


for i in nums:

    if i in first_occurance:
        second_occurance.append(i)
    
    else:
        first_occurance.append(i)
        
    
print(len(second_occurance))
    
if len(second_occurance) == 0:
    print(False)
else:
    print(True)