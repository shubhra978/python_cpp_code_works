def window_consec_sum(my_list,nums):
    
    window_sum=0
    
   # window_sum = sum(my_list[:nums])    #using sum function for first 3 elements
    
    for i in range(0,nums):            
        window_sum+=my_list[i]         # sum of first 3 elements
        
    
    max_sum=window_sum
    
    for i in range(nums,len(my_list)):
        
        window_sum = window_sum - my_list[i-nums] + my_list[i] #removing first element and adding next element 
        
        if(max_sum<window_sum): #comparing replacing the max number
            
            max_sum=window_sum
            
    return(max_sum)
    
    



new_list=[2, 5, 3, 7, 1, 4]
target=3
print(window_consec_sum(new_list,target))
