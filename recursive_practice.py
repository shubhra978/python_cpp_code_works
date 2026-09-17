#printing name recursively
count = 0
def my_name():
    global count
    if(count==5):
        return
    else:
        count+=1
        print("hello")
        my_name()

my_name()


