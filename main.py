from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel # request body and post method = طلب النص وطريقة الإرسال


app = FastAPI()

students = {
  1: {
    "name": "saleh",
    "age": 48,
    "year": "year 12"
  }
}

class Student(BaseModel):
  name: str
  age: int
  year: str
  
class UpdateStudent(BaseModel):
  name: Optional[str] = None
  age: Optional[int] = None
  year: Optional[str] = None

@app.get("/")
def index():
  return {"name": "First Data"}


@app.get("/get-student/{student_id}") 
# get by id param 'int'
def get_student(student_id: int = Path(None, description= "The ID of the student you want to view", gt=0, lt=3)):
  return students[student_id]


# get by param query? "str"
# combining path and query parameter = الجمع بين المسار ومعلمة الاستعلام
@app.get("/get-by-name,{student_id}")
def get_student( *, student_id: int, name: Optional[str] = None, test : int):
  for student_id in students:
    if students[student_id]["name"] == name:
        return students[student_id]
    return {"Date": "Not found"}
      
# request body and post method = طلب النص وطريقة الإرسال
@app.post("/create-student/{student_id}")
def creat_student(student_id: int, student: Student):
  if student_id in students:
      return {"Error": "Student exists"}
  
  students[student_id] = student
  return students[student_id]

# put methon
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
  if student_id not in students:
    return {"Error": "Student does not exist"}
  
  # students[student_id] = student # by id to update

  if student.name != None:
    students[student_id].name = student.name
    
  if student.age != None:
    students[student_id].age = student.age
    
  if student.year != None:
    students[student_id].year = student.year
      
  return students[student_id]

# Delete Method
@app.delete("/delete-student/{student_id}")
def delete_studunt(student_id: int):
  if student_id not in students:
    return {"Error": "student does not exist"}
  
  del students[student_id]
  return {"Message": "Student deleted successfully"}