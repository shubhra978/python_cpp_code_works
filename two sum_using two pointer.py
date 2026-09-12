def pairs(my_list,target):
    
    left = 0
    
    right =len(my_list)-1
    
    result = []
    
    while(left<right):
        
        nums = 0
        
        nums = my_list[left] + my_list[right]
        
        if(nums == target):
            #appending two values as pairs at once using double () with append
            result.append((my_list[left],my_list[right])) 
            left+=1
            right-=1
        #condition to check if the sum is less then moving left or  right depending on condition
        elif(nums < target): 
            
            left+=1
            
        else:
            
            right-=1  
            
    return result
    

my_list = [5,3,6,7,8,9,1,2,4]

target = 9

my_list.sort()

new_list = pairs(my_list,target)

print(new_list)
