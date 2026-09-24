if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

new_list = []    
for i in range(x+1): #for the first value
    for j in range (y+1): #for the second value
        for k in range (z+1): #for the third value
            if(i + j + k != n): #sum of all the numbers should not be equal to n
                new_list.append([i,j,k])
print(new_list)
