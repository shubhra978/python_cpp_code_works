list_1 = [1, 5, 8]
list_2 = [3, 2, 5]
list_3 = [2, 3, 6]


def addition(a,b,c):
    x= a+b+c
    print(x)
#map function takes each element and adding it as per function
list_4 = map(addition,(list_1),(list_2),(list_3)) 
