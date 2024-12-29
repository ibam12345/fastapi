@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, existing_student in enumerate(students):
        if existing_student.id == student_id:
            del students[index]
            return {"message": "Student deleted"}
    return {"error": "Student not found"}
