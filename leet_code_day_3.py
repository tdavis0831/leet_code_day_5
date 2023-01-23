""" Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.     """


#sort the list
#always going to start with 1
#compare numebrs to counter
#if the number isnt the same as the counter then add the counter num to list

num_listx = [4,3,2,7,8,2,3,1]
missing_nums_list = []   #hold missing numbers
# nums_dict = {} #convert list to dict to compare keys to i
 
def missing_nums(num_list):
    
    # for nums in num_list: #creates the dict
    #     nums_dict[nums] = 1

    
    for i in range(1, len(num_list)+1):  #starting at 1 since we know it starts at 1, and goes to length of num list plus 1 to be includsive
        
        if i not in num_list:              #will keep counting at 1 so as this goes it, it will check to see if in dict keys
            missing_nums_list.append(i)        #if not present in keys, it will create a new list with item appended
            
    return(missing_nums_list)     #returns the missing items

print(missing_nums(num_listx))