my_list = [1,2,3,5,7,9]
size = len(my_list)
#print reverse list 
print(my_list[::-1])
#print reverse list using while
while(size !=0):
    print(my_list[size-1])
    size-=1
#print reverse list using for  
for i in my_list:
    print(my_list[size-1])
    size-=1
new_list=[]
for i in my_list:
    new_list.append(i*i)
print(new_list)

num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]
added_list_value = []

for items in num_list:          # items is a sub-list
    result = 0
    for inner_items in items:   # inner_items is an element of that sub-list
        result += int(inner_items)
    added_list_value.append(result)

print(added_list_value)
# Output: [21, 28, 38, 39, 23]

heights = [177, 160, 171, 163, 168,  175, 176, 183, 162, 170]
heights.sort() #sorting the list
result = []
result = heights[-3:] #storing it in a different list
print(result[::-1]) #printing the result

# cook your dish here
list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
list2 = set(list1)
count = 0
for items in list1:
    if(items == target):
        count+=1
print(count)
print(len(list1)-len(list2)+1)
print(list1)
