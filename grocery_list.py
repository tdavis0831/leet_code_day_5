# Part 1
# ------

# Write a function that'll help you figure out whether you have
# enough money to buy all items in a shopping list.

# The function should take in:

# - A list of numbers -- the cost of every item in your shopping
#   list
    
# - A number -- the amount of money you have to spend

# The function should return true if you have enough money to
# buy all the items in your shopping list (otherwise, it
# should return false).

# For example:
    
# [4, 3, 5], 9
# => False

# [4, 5], 9
# => True

# [3, 2, 1], 100
# => True

# Part 2
# ------

# Now your function should take discounts into consideration.

# Edit your function to take in an additional
# argument -- a list of discounts. Each discount corresponds
# with an item in your shopping list, in order.

# Your function should print out the new price of each
# item you want to buy (don't worry about the return value
# for now).

# For example:
    
# [4, 3, 5], 9, [1, 2, 1]
# the cost of 4 is now 3
# the cost of 3 is now 1
# the cost of 5 is now 4




discount = [1,2,1]
grocery_item_cost = [4,3,5]

budget = 9
new_cost_list = []
def enough_money(items):
    total = 0
    for i in items:
        total += i
    
    if total <= budget:
        print("you have enough money")
        
    else:
        print("you don't have enough money")
        
    
    for i in range(len(items)):
        discount_total = items[i] - discount[i]
        new_cost_list.append(discount_total)
        
        print(f"the original cost was {grocery_item_cost[i]}, now its {new_cost_list[i]}")
        

    

enough_money(grocery_item_cost)



