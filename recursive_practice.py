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

#recursion to print from n - 1
def num_series(target):
    if(target == 0): #base function
        return
    else:
        print(target)
        num_series(target-1)
        
num_series(5)
#alternate
def n_to_i (i,inp):
    if(i<1):
        return
    print(i)
    n_to_i(i-1,inp)
user_inp = int(input())
iteration = user_inp
n_to_i(iteration,user_inp)

    


