num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]

unsorted_list = []
result = 0
maximum_sub_list =[]
for items in num_list:
    for inner_items in items:
        result = result + inner_items
        
    unsorted_list.append(result)


sorted_list = sorted(unsorted_list)
print(f"largest number = {sorted_list[len(sorted_list)-1]} and smallest number = {sorted_list[0]}")
