if __name__ == '__main__':
    student_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name,score])
    
# Step 1: Find the lowest score
lowest = student_list[0][1]
for student in student_list:
    score = student[1]
    if score < lowest:
        lowest = score

# Step 2: Find the second-lowest score
second_lowest = float('inf')  # Start with infinity
for student in student_list:
    score = student[1]
    if score > lowest and score < second_lowest:
        second_lowest = score

# Step 3: Collect all students who have the second-lowest score
second_lowest_names = []
for student in student_list:
    name = student[0]
    score = student[1]
    if score == second_lowest:
        second_lowest_names.append(name)

# Step 4: Sort names alphabetically and print
second_lowest_names.sort()
for name in second_lowest_names:
    print(name)
            
