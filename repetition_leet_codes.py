"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


  Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums. n == nums.length basically it should always being with 1 and the number of items in the list being the highest end of range ex:
  ex = [1,2,1,1]  range of values should be between 1-4 even though theres only 2 different numbers inside. ex2 =[4,3,2,7,8,2,3,1] which would be the same as ex3=[4,3,2,7,2,2,3,1] evne though the 8 isnt in this list, there are 8 items so the list should be from 1-8





 Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
""" 

#1

# nums = [1,2,3,4]
# first_occurance= []
# second_occurance = []


# for i in nums:

#     if i in first_occurance:
#         second_occurance.append(i)
    
#     else:
#         first_occurance.append(i)
        
    
# print(len(second_occurance))
    
# if len(second_occurance) == 0:
#     print(False)
# else:
#     print(True)
    
    
    #2  Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do #not appear in nums.    



nums = [1,2,2,2]


missing_num = []

for i in range(1, len(nums)+1):
    
    if i not in nums:
        missing_num.append(i)


print(missing_num)




    
        
        
            