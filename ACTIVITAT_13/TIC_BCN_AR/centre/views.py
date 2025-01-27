from django.shortcuts import render

def students(request):
    students = [
        { 'id': 1, 'nom': 'Arman', 'cognom1': 'Mohammed', 'cognom2': 'Akther', 'correu': 'arman@example.com', 'curs': 'DAW2A', 'moduls': ['M07', 'M08', 'M09']},
        { 'id': 2, 'nom': 'Oriol', 'cognom1': 'Gonzalez', 'cognom2': 'Farrsac', 'correu': 'oriol@example.com', 'curs': 'DAW2A', 'moduls': ['M07', 'M08', 'M09']},
    ]
    return render(request, 'students.html', {'students': students})

def students2(request, pk):
    students = [
        { 'id': 1, 'nom': 'Arman', 'cognom1': 'Mohammed', 'cognom2': 'Akther', 'correu': 'arman@example.com', 'curs': 'DAW2A', 'moduls': ['M07', 'M08', 'M09']},
        { 'id': 2, 'nom': 'Oriol', 'cognom1': 'Gonzalez', 'cognom2': 'Farrsac', 'correu': 'oriol@example.com', 'curs': 'DAW2A', 'moduls': ['M07', 'M08', 'M09']},
    ]
    
    student_Obj = None
    for student in students:
        if student['id'] == pk:
            student_Obj = student
    
    return render(request, 'student2.html', {'student': student_Obj})

def teachers(request):
    professors = [
        { 'id': 1, 'nom': 'Roger', 'cognom1': 'Sobrino', 'cognom2': 'Gil', 'correu': 'roger@example.com', 'curs': 'DAW2A', 'moduls': ['M07']},
        { 'id': 2, 'nom': 'Oriol', 'cognom1': 'nose', 'cognom2': 'nose', 'correu': 'oriol@example.com', 'curs': 'DAW2A', 'moduls': ['M06']},
    ]
    return render(request, 'teachers.html', {'teachers': professors})

def teachers2(request, pk):
    professors = [
        { 'id': 1, 'nom': 'Roger', 'cognom1': 'Sobrino', 'cognom2': 'Gil', 'correu': 'roger@example.com', 'curs': 'DAW2A', 'moduls': ['M07']},
        { 'id': 2, 'nom': 'Oriol', 'cognom1': 'nose', 'cognom2': 'nose', 'correu': 'oriol@example.com', 'curs': 'DAW2A', 'moduls': ['M06']},
    ]
    
    teacher_Obj = None
    for teacher in professors:
        if teacher['id'] == pk:
            teacher_Obj = teacher
    
    return render(request, 'teacher2.html', {'teacher': teacher_Obj})
