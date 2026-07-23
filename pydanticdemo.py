from pydantic import BaseModel

# Creating a pydantic model
class Student(BaseModel):
    name: str
    age: int

def show_data(student: Student):
    print(student.name)
    print(student.age)
    print("Done")

info= {'name':'Ram', 'age':20}
s1=  Student(**info)

show_data(s1)