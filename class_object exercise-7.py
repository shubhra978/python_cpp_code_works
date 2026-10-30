#Write a python class *Student*, which contains the student's name and his marks in 3 subjects given below. Define a class method to calculate and return the average percentage of the student. Finally, call the class and display all the information.\n",
# "name = 'Robin'\n",
   # "<br>sub_1 = 85\n",
    #"<br>sub_2 = 74\n",
    #"<br>sub_3 = 90\n",

class Student:
  sub_1 = 85
  sub_2 = 74
  sub_3 = 90
  average = (sub_1+sub_2+sub_3)/3
  def marks_avg(self):
    print(f"average is {self.average}")

robin_marks = Student()
robin_marks.marks_avg()
