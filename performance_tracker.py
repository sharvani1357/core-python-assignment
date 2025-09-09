class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)    
n = int(input("enter no of stds:"))
students = {}
for i in range(n):
    name = input("Enter student name: ").strip()
    marks = list(map(int, input("Enter marks: ").split()))
    students[name] = Student(name, marks)
average_marks = {}
for name, student in students.items():
    average_marks[name] = round(student.average_marks(), 2)
top_performer = max(average_marks, key=average_marks.get)
print("\nAverage Marks:", average_marks)
print("Top Performer:", top_performer)
