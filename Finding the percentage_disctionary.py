if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_scores = 0
    count = 0
    if query_name in student_marks: #checking if the key is present
        for scores in student_marks[query_name]: #keeping the query name from user and adding its value in the next line
            avg_scores += scores
            count+=1
    avg_scores=avg_scores/count
    print(f"{avg_scores:.2f}")
            
            
