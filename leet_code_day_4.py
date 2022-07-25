"""	
 Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
""" 


nums = [4,1,2,1,2]


single_number = []




for i in nums:
    if i not in single_number:
        single_number.append(i)  #if something isnt in the set, add it
    
    else:
        single_number.remove(i) #if it is already on the list remove it, we only want things that will not have 2 so this condition
                                #shouldn't ever be met if there is a number in the list once

print(single_number)
    
    



    
   
    