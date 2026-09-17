#printing name recursively
count = 0
def my_name():
    global count
    if(count==5): #base function
        return
    else:
        count+=1
        print("hello")
        my_name()
my_name()


#recursion to print from 1 - n
count  = 0
def num_series(target):
    global count
    if(count == target): #base function
        return
    else:
        print(count)
        count+=1
        num_series(target)
num_series(5)


