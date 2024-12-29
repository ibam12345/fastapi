from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    age: int
    grade: int

students = [
    Student(id=1, name="ali a", age=20, grade=6),
    Student(id=2, name="ali b", age=21, grade=5)
]

@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def create_student(new_student: Student):
    students.append(new_student)
    return new_student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for index, existing_student in enumerate(students):
        if existing_student.id == student_id:
            students[index].name = student.name
            students[index].age = student.age
            students[index].grade = student.grade
            return students[index]
    return {"error": "Student not found"}
  
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, existing_student in enumerate(students):
        if existing_student.id == student_id:
            del students[index]
            return {"message": "Student deleted"}
    return {"error": "Student not found"}