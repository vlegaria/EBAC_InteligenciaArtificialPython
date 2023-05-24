# Libreria para la interfaz
import PySimpleGUI as sg
import os
# Modulo math para calcular raiz cuadrada
import math
# Librerias para procesamiento de lenguaje natural
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.corpus import stopwords
#Descomentar e instalar en caso de indicar error la librería nltk
#nltk.download()

# Declaración de variables para la parte de Procesamiento de Lenguaje Natural (PNL)
# Se inicializan las listas vacias que se llenaran
# dependiento del texto del archivo
sentences = []
tagged = []
tokens = []
named_entities = []
filtered_words = []

# Declaración de la función para extraer la distinta información de interés de un texto mediante PNL
def process_text(text):
    # Tokenización de oraciones
    sentences = sent_tokenize(text)
    # Tokenización de palabras
    tokens = word_tokenize(text)
    # Etiquetado gramatical
    tagged = pos_tag(tokens)
    # Reconocimiento de entidades nombradas
    named_entities = ne_chunk(tagged)
    # Eliminación de palabras vacías (stop words)
    stop_words = set(stopwords.words('english'))
    filtered_words = [token for token in tokens if token.lower() not in stop_words]

    return sentences, tokens, tagged, named_entities, filtered_words

# Para la parte de PLN solo se buscaran archivos de texto de tipo .txt
file_types = [("TXT (*.txt)", "*.txt")]

# Configuración de los elementos de la interfaz (ubicación de los botones, textos de entrada y salida)
layout = [ 
            [sg.Text('Escribe tus datos para guardarlos en las variables:')],
            [sg.Text("Nombre:"), sg.Input("", size=(40,1), key="-NOMBRE-"), sg.Text("Edad en años:"), sg.Input("", size=(5,1), key="-EDAD-")],
            [sg.Text("Altura en metros, ejemplo 1.50:"), sg.Input("", size=(5,1), key="-ESTATURA-"), sg.Text("¿Eres estudiante? Escribe True o False:"), sg.Input("", size=(5,1), key="-ESTUDIANTE-")],
            [sg.Button('GENERAR TEXTO')] ,
            [sg.Text("Escribe un numero para contar:"), sg.Input("", size=(5,1), key="-NUMERO-"), sg.Button('CONTADOR')],
            [sg.Text("Escribe frutas separadas por PUNTO Y ESPACIO. Ej: Pera. Uva. Fresa"), sg.Input("", size=(5,1), key="-LISTA-"), sg.Button('IMPRIMIR')],
            [sg.Text('Escribe la base y la altura de un rectangulo para calcular su área:')],
            [sg.Text("Base:"), sg.Input("", size=(5,1), key="-BASE-"), sg.Text("Altura:"), sg.Input("", size=(5,1), key="-ALTURA-"), sg.Button('CALCULAR AREA')],
            [sg.Text('Escribe un numero para calcular su raíz cuadrada:')],
            [sg.Text("Número:"), sg.Input("", size=(5,1), key="-RAIZ-"), sg.Button('CALCULAR RAIZ')],
            [sg.Text('Resultados:')], 
            [sg.Output(size=(50,7), key='-OUTPUT-')],
            [sg.Text("PRESIONA el boton para buscar archivo txt"), sg.Input(size=(25, 1), key="-FILENAME-"),sg.FileBrowse(file_types=file_types),sg.Button("PROCESAR TEXTO")],
            [sg.Text("Oraciones"),sg.Combo(sentences,default_value=" ",size=(50,1),key="-SENTENCES-",enable_events=True, readonly=True )],
            [sg.Text("Tokens"),sg.Combo(tokens,default_value=" ",size=(20,1),key="-TOKENS-",enable_events=True, readonly=True),
                sg.Text("Etiquetas gramaticales"),sg.Combo( tagged,default_value=" ", size=(20,1), key="-TAGGED-", enable_events=True, readonly=True) ],
            [sg.Text("Entidades nombradas"), sg.Combo(named_entities, default_value=" ",  size=(20,1), key="-NAMED_ENTITIES-", enable_events=True, readonly=True),
                sg.Text("Palabras filtradas"),  sg.Combo( filtered_words, default_value=" ", size=(20,1), key="-FILTERED_WORDS-",  enable_events=True,readonly=True,),],
            [sg.Button('BORRAR TODO'), sg.Button('EXIT')],
    ]
def main():
    # Se crea el objeto de la ventana y se le asigna un nombre a la pestaña
    window = sg.Window('Tarea EBAC Valeria Legaria', layout)
    # La ventana se estará ejecutando hasta que se cierre o se de clic en el botón exit
    while True: 
        # Se agrega un bloque try-except para manejar que en caso de algún error, la ventana no se cierre
        try:
            # Se leen los valores de los objetos de la interfaz (estatus de los botones y contenido de los espacios de entrada de texto)
            event, values= window.read()
            # Si el botón EXIT es presionado, se termina el ciclo while
            if event in (sg.WIN_CLOSED, 'EXIT'):
                break
            # Si se presiona el botón "BORRAR TODO" se borra el contenido de los objetos en la interfaz
            if event == 'BORRAR TODO':
                window['-OUTPUT-'].update('')
                window['-NOMBRE-'].update('')
                window['-EDAD-'].update('')
                window['-ESTATURA-'].update('')
                window['-ESTUDIANTE-'].update('')
                window['-NUMERO-'].update('')
                window['-LISTA-'].update('')
                window['-BASE-'].update('')
                window['-ALTURA-'].update('')
                window['-RAIZ-'].update('')
                window['-FILENAME-'].update('')
                window["-SENTENCES-"].Update(value="", values=[])
                window["-TOKENS-"].Update(value="", values=[])
                window["-TAGGED-"].Update(value="", values=[])
                window["-NAMED_ENTITIES-"].Update(value="", values=[])
                window["-FILTERED_WORDS-"].Update(value="", values=[])
            # El botón GENERAR TEXTO Imprime en el cuadro de salida la variable de entrada siempre y cuando
            # no sea un campo vació y coincida con el tipo de dato que se espera. En caso contrario se imprime
            # un mensaje indicando el tipo de error
            if event == "GENERAR TEXTO":
                window['-OUTPUT-'].update('')
                if values["-NOMBRE-"]=="":
                    print("Campo de Nombre vacio")
                else:
                    nombre = values["-NOMBRE-"].replace(" ","")
                    if nombre.isalpha():
                        print("Mi nombre es", values["-NOMBRE-"])
                    else:
                        print("Nombre no válido, solo se aceptan letras y espacios")
                if values["-EDAD-"] == "":
                    print("Campo de Edad vacio")
                else:
                    try:
                        print("Tengo", int(values["-EDAD-"]), "años de edad.")
                        if int(values["-EDAD-"]) >= 18:  # Si la edad es mayor o igual a 18
                            print("Soy mayor de edad")
                        else:
                            print("Soy menor de edad")
                    except:
                        print("Edad no válida, debe ser un número entero")
                if values["-ESTATURA-"] == "":
                    print("Campo de Estatura vacio")
                else:
                    try:
                        print("Mido", float(values["-ESTATURA-"]), "metros de estatura.")
                    except:
                        print("Estatura no válida, debe ser un valor numérico")
                if values["-ESTUDIANTE-"] == "":
                    print("Campo de Estudiante vacio")
                else:
                    if values["-ESTUDIANTE-"] == "True" :
                        print("Soy estudiante", True)
                    elif values["-ESTUDIANTE-"] == "False":
                        print("No soy estudiante ", False)
                    else:
                        print("Respuesta de Estudiante no válida, debe ser escrito como True o False")
                
            # El botón CONTADOR imprime el incremento de 1 en 1 de la variable contador hasta llegar 
            # al valor indicado por el usuario 
            if event == "CONTADOR":
                window['-OUTPUT-'].update('')
                try:
                    contador = 0
                    while contador < int(values["-NUMERO-"]):
                        print("El contador es", contador)
                        contador += 1
                except:
                    print("El valor debe ser numérico y entero")

            # El botón IMPRIMIR imprime la oración "Me gusta la fruta" + el nombre de la fruta proveniente de la lista
            # de frutas que ingrese el usuario. La oración se imprime cuantas frutas se hayan ingresado. Estas deben estar
            # separadas por un punto y un espacio.
            if event == "IMPRIMIR":
                window['-OUTPUT-'].update('')
                try:
                    result = process_text(values["-LISTA-"])
                    frutas = result[0]
                    for fruta in frutas:
                        print("Me gusta comer", fruta)
                except:
                    print("La lista debe estar escrita de la forma: Pera. Uva. Fresa")

            # El botón calcular área regresa el resultado de la operación matemática de multiplicar los valores númericos ingresados
            # en los recuadros respectivos a base y altura.
            if event == "CALCULAR AREA":
                try:
                    area = float(values["-BASE-"]) * float(values["-ALTURA-"])
                    print("El area del rectangulo de base", values["-BASE-"], "y altura", values["-ALTURA-"], "es: ", area)
                except:
                    print("Los valores de base y altura deben ser numéricos")
                    
            #l El botón CALCULAR RAÍZ regresa la raíz cuadrada del número ingresado por el usuario
            if event == "CALCULAR RAIZ":
                try:
                    area = math.sqrt(float(values["-RAIZ-"]))
                    print("La raiz cuadrada de", values["-RAIZ-"], "es:", area)
                except:
                    print("El valor para cacular la raiz debe ser numérico")

            # Para ejecutar el botón PROCESAR TEXTO primero es necesario buscar un archivo de texto .txt con el botón BROWSER
            # Una vez que se visualiza la ruta del archivo en la interfas, al presionar el botón PROCESAR TEXTO se ejecuta la función 
            # process_text la cual regresa listas después de aplicar distintos métodos de NPL al texto seleccionado
            if event == 'PROCESAR TEXTO':
                window['-OUTPUT-'].update('')
                filename = values["-FILENAME-"]
                if os.path.exists(filename):
                    with open(filename, encoding="UTF-8") as archivo:
                        file = archivo.read()
                print(file)
                sentences, tokens, tagged, named_entities, filtered_words,  = process_text(file)
                window["-SENTENCES-"].Update(value=sentences[0], values=sentences)
                window["-TOKENS-"].Update(value=tokens[0], values=tokens)
                window["-TAGGED-"].Update(value=tagged[0], values=tagged)
                window["-NAMED_ENTITIES-"].Update(value=named_entities[0], values=named_entities)
                window["-FILTERED_WORDS-"].Update(value=filtered_words[0], values=filtered_words)
        except:
            # Se ignora si ocurrió algún error y se continúa en el bucle while
            pass
    # Se cierra la ventana de la interfaz
    window.close()

if __name__ == "__main__":
    main()