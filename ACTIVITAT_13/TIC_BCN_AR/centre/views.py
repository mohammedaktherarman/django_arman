from django.shortcuts import render
alumnes = [
        { 'id': 1, 'nom': 'Arman', 'cognom1': 'Mohammed', 'cognom2': 'Akther', 'correu': 'arman@example.com', 'curs': 'DAW2A', 'moduls': ['M07', 'M08', 'M09']},
        { 'id': 2, 'nom': 'Oriol', 'cognom1': 'Gonzalez', 'cognom2': 'Farrsac', 'correu': 'oriol@example.com', 'curs': 'DAW2A', 'moduls': ['M07', 'M08', 'M09']},
    ]

professors = [
        { 'id': 1, 'nom': 'Roger', 'cognom1': 'Sobrino', 'cognom2': 'Gil', 'correu': 'roger@example.com', 'curs': 'DAW2A', 'moduls': ['M07']},
        { 'id': 2, 'nom': 'Oriol', 'cognom1': 'nose', 'cognom2': 'nose', 'correu': 'oriol@example.com', 'curs': 'DAW2A', 'moduls': ['M06']},
    ] 

def students(request):
    return render(request, 'students.html', {'students': alumnes})

def students2(request, pk):
    student_Obj = None
    for student in alumnes:
        if student['id'] == pk:
            student_Obj = student
    
    return render(request, 'student2.html', {'students': student_Obj})


def teachers(request):
    return render(request, 'teachers.html', {'teachers': professors})

def teachers2(request, pk):
    teacher_Obj = None
    for teacher in professors:
        if teacher['id'] == pk:
            teacher_Obj = teacher
    
    return render(request, 'teacher2.html', {'teachers': teacher_Obj})
