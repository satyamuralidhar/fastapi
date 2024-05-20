from fastapi import FastAPI , Path

app = FastAPI()

students = {
    1 : {
        'Name' : 'satya',
        'Age'  :  30,
        'Domain' : 'IT'
    },
    2 : {
        'Name' : 'mohan',
        'Age'  :  32,
        'Domain' : 'MBA'
    },
    3 : {
        'Name' : 'pavan',
        'Age'  :  25,
        'Domain' : 'Chemical'
    }
}

valid = students.keys()

@app.get("/info/{student_id}") 

async def info(student_id: int =Path(gt=0,description="student info with ID")):
    return students[student_id]
#Getting the response form query 
@app.get("/name")
async def get_student(name: str):
    for student_id in students:
        if students[student_id]["Name"] == name:
            return students[student_id]
        else:
            return f"{name} not Avalible on Given Dictionary"
    return {"Data" : "NotFound"}