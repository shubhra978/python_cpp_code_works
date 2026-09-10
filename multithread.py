import random
import time
from concurrent.futures import ThreadPoolExecutor

my_list=['apple', 'banana', 'cherry', 'date']

def item_iter(i):
    
    wait = random.randint(1,10) #assigning a random value between 1 to 10
    
    time.sleep(wait) #using time function to sleep for the random value of wait
    
    print(f"my value is {i} and time taken is {wait}")

#run the function within a loop
for items in my_list:
    
    item_iter(items)

#using ThreadPoolExecutor to run the items of the list concurrently

with ThreadPoolExecutor(max_workers=len(my_list)) as executor: #maxworker will work for all the items as per length

    futures = executor.map(item_iter.my_list) #now executor will map all the items as per the function and run concurrently
