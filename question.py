import random
import sys
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
6.
7.
1.
2.
3.
# El usuario deberá contestar 3 preguntas
points = 0
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

for questions, option_answers, correct_answers in questions_to_ask:
    print(questions)
    for i, answers in enumerate(option_answers):
         print(f"{i + 1}. {answers}")
        # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ") 
        if user_answer.isdigit() == False or 0 < int(user_answer) > 4:
            print("respuesta invalidad")
            exit(1)
            
        else:
            user_answer = int(user_answer)
        # Se verifica si la respuesta es correcta
            if user_answer -1 == correct_answers:
                print("¡Correcto!")
                points += 1
                break
            else:
             # Si el usuario no responde correctamente después de   2 intentos,
             # se muestra la respuesta correcta
                print("Incorrecto. La respuesta correcta es:")
                points += -0.5
                print(f' la respuesta correcta es: {option_answers[correct_answers]}')
# Se imprime un blanco al final de la pregunta
print(f'tu punjaje fue de {points}')
print()