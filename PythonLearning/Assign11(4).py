students={
"student1":{
    "name":"Bob",
    "age":18,
    "marks":85
},
"student2":{
    "name":"Alice",
    "age":20,
    "marks":90
},
"student3":{
    "name":"John",
    "age":17,
    "marks":89
}
}

for student in students.values():
    print(student["name"], "-", student["age"])