def another_one(digits):
  result = 0
  for nums in digits:
    result = result * 10 + nums
    
  
  result +=1
  
  
  
  new_list =[]
  
  for nums in str(result):
    
    new_list.append(int(nums))
    
  return new_list


list = [1,2,3]
  
