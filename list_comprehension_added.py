num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]
added_list_value = []

for items in num_list:          # items is a sub-list
    result = 0
    for inner_items in items:   # inner_items is an element of that sub-list
        result += int(inner_items)
    added_list_value.append(result)

print(added_list_value)
# Output: [21, 28, 38, 39, 23]


#"We have two lists given below. I want you to print the first list in the original order and the second list in reverse order simultaneously.\n",

list_1 = [12, 25, 31, 20, 18]
list_2 = [11, 9, 43, 22, 55]

for i in range(0,len(list_1)):
    print(list_1[i],list_2[len(list_2)-1-i], end=" ")

#"We have a set that contains roll numbers of candidates who have applied for an event. Out of the applied candidates, few have submitted their application forms, and we have registered their details in a dictionary given below. Print the roll numbers of the candidates who have submitted their application forms and also the ones who are yet to submit it.\n",
     #   "roll_numbers = {12, 7, 15, 23, 32, 30}\n",
  #  "<br>student_details = {12:'Judy', 30:'Shane', 23:'Aaron'}\n",

roll_numbers = {12, 7, 15, 23, 32, 30}
student_details = {12:'Judy', 30:'Shane', 23:'Aaron'}

c_app =[]
pa_app = []
for items in roll_numbers:
    if items in student_details:
        c_app.append(items)
    else:
        pa_app.append(items)
        
print("completed application", sorted(c_app))
print("pending application",(pa_app))
