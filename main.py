questions = {
    1: '¿Quien descubrió América según los libros de historia?',
    2: '¿Cuánto vale Pi?',
    3: '¿Quien es el futbolista con más balones de oro?',
    4: '¿Cuál es el animal más grande en la tierra?',
    5: '¿Cuánto duró la guerra de los 100 años?',
    6: '¿Qué periodo de años comprendió la primera guerra mundial?',
    7: '¿Cuántos huesos tiene el cuerpo humano?',
    8: '¿Qué medicamento mata a los virus?',
    9: '¿Cuál es el resultado de cualquier número elevado a 0?',
    10: '¿Cuál es la edad del universo?',
    11: '¿Qué país tiene la menor cantidad de población del mundo?',
    12: '¿Cuál es el album musical más vendido en la historia?', 
    13: '¿Con qué se fabricaba el pergamino?',
    14: '¿Qué cantante es conocido como "The Boss"?',
    15: '¿Qué es lo más caro del mundo?'
}

answers = {
    1: ['A', 'a) Cristóbal Colón b) Hernán Cortés\nc) William Sheakspeare d) Rene Descártes', 'a) Cristobal Colón  d) René Descartes'],
    2: ['D', 'a) 12.23 b) 89.78\nc) 76.87 d) 3.14', 'b) 89.78 d) 3.14'],
    3: ['A', 'a) Lionel Messi b) Pelé\nc) Cristiano Ronaldo d) La Chofis', 'a) Lionel Messi  c) Cristiano Ronaldo'],
    4: ['D', 'a) Elefante b) Jirafa\nc) Tiburón blanco d) Ballena azul', 'c) Tiburón blanco  d) Ballena Azul'],
    5: ['C', 'a) 100 años b) 101 años\nc) 116 años d) 126 años', 'a) 100 años  d) 116 años'],
    6: ['C', 'a) 1939-1945 b) 1978-1983\nc) 1914-1918 d) 1920-1925', 'a) 1939-1945  c) 1914-1918'],
    7: ['D', 'a) 100 b) 987\nc) 398 d) 206', 'b) 987  d) 206'],
    8: ['D', 'a) Aspirina b) Paracetamol\nc) Ramipiril d) Ninguno', 'c) Ramipiril  d) Ninguno'],
    9: ['B', 'a) Cero b) Uno\nc) El mismo número d) Diez', 'b) Uno  c) El mísmo número'],
    10: ['B', 'a) 1 billon de años b) 13.8 billones de años\nc) 100 billones de años d) 13 billones de años', 'a) 1 billón de años  d) 13.8 billones de años'],
    11: ['B', 'a) Islas Marshall b) Ciudad del Vaticano\nc) Palau d) San Marino', 'a) Islas Marshall  b) Ciudad del Vaticano'],
    12: ['A', 'a) Thriller de Michael Jackson b) Back in Black de AC/DC\nc) El guardaespaldas de Witney Houston d) The Dark Side of the Moon de Pink Floyd', 'a) Thriller de Michael Jackson b) Back in Black de AC/DC'],
    13: ['D', 'a) Plastico b) Hule\nc) Hojas d) Piel', 'a) Plastico d) Piel'],
    14: ['D', 'a) Bruno Mars b) Freddie Mercury\nc) Michael Jackson d) Bruce Springsteen', 'a) Bruno Mars d) Bruce Springsteen'],
    15: ['B', 'a) Polvo lunar b) Antimateria\nc) Oro d) Uranio', 'a) Polvo lunar b) Antimateria']
}

scoring = {
    1: '100',
    2: '200',
    3: '300',
    4: '500',
    5: '1,000',
    6: '2,000',
    7: '4,000',
    8: '8,000',
    9: '16,000',
    10: '32,000',
    11: '64,000',
    12: '125,000',
    13: '250,000',
    14: '500,000',
    15: '1,000,000'
}

extra_questions = {
    1: 'Quién es el padre del psicoanálisis?',
    2: '¿Cuál es el país más poblado en la tierra?',
    3: '¿Qué área de la biología estudia a los animales?'
}

extra_answers = {
    1: ['A', 'a) Sigmund Freud b) Noam Chumski\nc) Abraham Maslow d) William James', 'a) Sigmund Freud b) Noam Chumsky'],
    2: ['B', 'a) Estados Unidos b) China\nc) Malasia d) Japón', 'a) Estados Unidos b) China'],
    3: ['A', 'a) Zoología d) Anatomía\nc) Morfología d) Eligotomía', 'a) Zoología c) Morfología']
}

def print_questions(n):
    print('PREGUNTA NÚMERO', n)
    print(questions[n])
    print(answers[n][1])

def capture_answer(n):
    answer = input('Escribe tu respuesta: ').upper() 
    if answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D' or answer == '50:50':
        return answer
    else:
        while answer != 'A' or answer != 'B' or answer != 'C' or answer != 'D' or answer != '50:50':
            answer = input('Escribe una pregunta válida (A, B, C, D o 50:50): ').upper()
            if answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D' or answer == '50:50':
                return answer
                break

def fifty_fifty_function(n, fifty_fifty):
    if fifty_fifty == 1:
        print('-----------COMODÍN 50:50--------------')
        print(questions[n])
        print(answers[n][2])
        fifty_fifty -= 1
        return fifty_fifty
    else:
        print('Ya no tienes comodines 50:50!')
        fifty_fifty = 0
        return fifty_fifty

def evaluate_answer(answer, n):
    final_answer = input('Escribe * para confirmar tu respuesta final: ').upper()
    if final_answer == '*':
        if answer == answers[n][0]:
            return True

def incorrect_answer(bucket):
    print('Respuesta incorrecta!')
    print('Has conseguido ${} dólares.'.format(bucket))

def scoring_money(bucket, scoring, n):
    if n == 15:
        bucket = scoring[n]
        return bucket
    else:
        bucket = scoring[n]
        print('Correcto! Ahora tienes ${} dólares en total. Avanzas a la siguiente pregunta.'.format(bucket))
        return bucket

def extra_question(extra_questions, extra_answers, extra_question_number):
    print('--PREGUNTA EXTRA {}--'.format(extra_question_number))
    print(extra_questions[extra_question_number])
    print(extra_answers[extra_question_number][1])
    extra_answer = input('Escribe tu respuesta aquí: ').upper()
    final_answer = input('Escribe * para confirmar tu respuesta final: ')
    if final_answer == '*':
        if extra_answer == extra_answers[extra_question_number][0]:
            return True

def instructions():
    print('''
    WHO WANTS TO BE A MILLIONAIRE?
    ------------------------------

    ¡Bienvenido al juego dónde puedes hacerte rico con 15 pregutnas!
    
    Estas son las reglas:
    
    * Cada pregunta vale cierta cantidad de dinero mientras avanzas (véase en la tabla de premios).
    * Cada pregunta es de opción múltiple, hay 4 respuestas posibles.
    * Si no conoces una respuesta, tendrás la oportunidad de contestar una pregunta extra de menor dificultad
      pero si la fallas, termina el juego y te retiras con la cantidad de dinero que has ganado.
    * Tienes 3 preguntas extra disponibles.
    * Tienes la oportunidad de usar un comodín 50:50 que eliminará dos respuestas incorrectas del tablero al esbribir lo siguiente: 50:50.
    * En las respuestas extra no puedes usar el comodín 50:50 para evitar un desbalance.
    * Al llegar a la pregunta número 15, no podrás usar ni comodines 50:50 ni preguntas extra.
      Si no respondes correctamente, te retirarás con el dinero equivalente de la pregunta número 10.
        
        Esta es la tabla de premios:

        Pregunta     Premio
        ******************************
        * 1 ---------> 100 USD       *
        * 2 ---------> 200 USD       *
        * 3 ---------> 300 USD       *      
        * 4 ---------> 500 USD       *
        * 5 ---------> 1,000 USD     * 
        * 6 ---------> 2,000 USD     * 
        * 7 ---------> 4,000 USD     * 
        * 8 ---------> 8,000 USD     *
        * 9 ---------> 16,000 USD    *
        * 10 --------> 32,000 USD    *
        * 11 --------> 64,000 USD    *
        * 12 --------> 125,000 USD   *
        * 13 --------> 250,000 USD   *   
        * 14 --------> 500,000 USD   *
        * 15 --------> 1,000,000 USD *
        ******************************
    ''')
    input('Presiona * para comenzar: ')

def main(questions, scoring, answers, extra_questions, extra_answers):
    bucket = 0
    extra_question_number = 0
    fifty_fifty = 1
    for n in questions:
        if n == 15:
            print('\n------------------------------')
            print('Has llegado a la pregunta {}. Si te equivocas en esta pregunta, te retirarás con el dinero que conseguiste en la pregunta número 10.\nTampoco hay preguntas extra ni comodines 50:50'.format(n))
            print_questions(n)
            if evaluate_answer(capture_answer(n), n):
                bucket = scoring_money(bucket, scoring, n)
                print('¡FELICIDADES! ¡ACABAS DE GANAR ${} DÓLARES! El juego ha terminado.'.format(bucket))
                break
            else:
                print('La respuesta fue incorrecta. Te retiras con ${} dólares.'.format(scoring[10]))
                break
        print('\n------------------------------')
        print('Tienes {} comodín(es) 50:50 disponible(s)'.format(fifty_fifty))
        print_questions(n)
        answer = capture_answer(n)
        if answer == '50:50':
            fifty_fifty = fifty_fifty_function(n, fifty_fifty)
            answer = capture_answer(n)
        if evaluate_answer(answer, n):
            bucket = scoring_money(bucket, scoring, n)
        else:
            
            extra_question_number += 1
            print('Respuesta incorrecta!')
            print('\n------------------------------')
            if extra_question_number == 1:
                if extra_question(extra_questions, extra_answers, extra_question_number):
                    bucket = scoring_money(bucket, scoring, n)
                    continue
                else:
                    incorrect_answer(bucket)
                    break
            elif extra_question_number == 2:
                if extra_question(extra_questions, extra_answers, extra_question_number):
                    bucket = scoring_money(bucket, scoring, n)
                    continue
                else:
                    incorrect_answer(bucket)
                    break  
            elif extra_question_number == 3:
                if extra_question(extra_questions, extra_answers, extra_question_number):
                    bucket = scoring_money(bucket, scoring, n)
                    continue
                else:
                    incorrect_answer(bucket)
                    break
            else:
                print('Se te acabaron las preguntas extra! El juego terminó.')
                print('Te retiras con ${} dólares!'.format(bucket))
                break