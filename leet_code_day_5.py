"""

 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
 
	"""
 
 
 #if we want to get the index of something, put it in a dictary and set the key to be the number and the value to be index
 #syntax dict[keyvalue-Typically the list name[i here to list through individual items in list] ex nums[i] = i (this is to call index)]
 
nums = [2,7,11,15]
target = 9
return_nums = []
 
def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):     #need to use range(len) since we are getting indicies
        if target - nums[i] not in dict:
            dict[nums[i]] = i
        else:
            print(dict[target - nums[i]])
            print(dict[2])
		
            print(i)
            return [dict[target - nums[i]], i] #gives us back target-numsi in this case, 9-7 so 2 
			


print(twoSum(nums, target))
        