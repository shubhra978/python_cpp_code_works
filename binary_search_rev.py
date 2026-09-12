def pairs(my_list,target):
    
    left = 0

    right =len(my_list)-1
    
    while(left<right):
        
        mid = left + (right-left)//2
        
        if(my_list[mid]==target):
            
            return mid
            
        elif(my_list[mid] < target):
            
            left = mid + 1
            
        else:
            
            right = mid - 1
            
    return mid


my_list = [5,3,6,7,8,9,1,2,4]

target = 3

my_list.sort()

new_list = pairs(my_list,target)

print(new_list)
