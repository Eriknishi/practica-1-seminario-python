import random
import sys #es para que funcione el sys.exit

# Preguntas para el juego
questions = ["¿Qué función se usa para obtener la longitud de una cadena en Python?","¿Cuál de las siguientes opciones es un número entero en Python?", "¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?", "¿Cuál es el operador de comparación para verificar si dos valores son iguales?", ]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [ ("size()", "len()", "length()", "count()"), ("3.14", "'42'", "10", "True"), ("input()", "scan()", "read()", "ask()"),
( "// Esto es un comentario","/* Esto es un comentario */", "-- Esto es un comentario","# Esto es un comentario",),("=", "==", "!=", "==="),]
# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# El usuario deberá contestar 3 preguntas

puntaje=0

questions_to_ask = random.choices(list(zip(questions,answers, correct_answers_index)), k=3)

for pregunta,opciones,correct_index in questions_to_ask:
    print(pregunta)
    
    for i, option in enumerate(opciones):
        print(f"{i + 1}. {option}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        if user_answer.isnumeric() and 0 <= (int(user_answer)-1) <= 3:
            if int(user_answer)-1 == correct_index:
                print("¡Correcto!")
                puntaje+=1
                break
            else:
                puntaje+= -0.5
        else:
            print('respuesta no valida')
            sys.exit(1)
    else:
         print("Incorrecto. La respuesta correcta es:")
         print(opciones[correct_index])

print(f'Puntaje total: {puntaje}')