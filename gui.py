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

#Solo se buscaran archivos de texto de tipo .txt
file_types = [("TXT (*.txt)", "*.txt"), ("All files (*.*)", "*.*")]

conf_layout = [ 
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
            [
                sg.Text("TXT File"),
                sg.Input(
                    size=(25, 1), key="-FILENAME-"
                ),
                sg.FileBrowse(file_types=file_types),
                sg.Button("PROCESAR TEXTO"),
            ],
            [
                sg.Text("Oraciones"),
                sg.Combo(
                    sentences,
                    default_value=" ",
                    size=(50,1),
                    key="-SENTENCES-",
                    enable_events=True,
                    readonly=True,
                )],
            [
                sg.Text("Tokens"),
                sg.Combo(
                    tokens,
                    default_value=" ",
                    size=(20,1),
                    key="-TOKENS-",
                    enable_events=True,
                    readonly=True,
                ),
                sg.Text("Etiquetas gramaticales"),
                sg.Combo(
                    tagged,
                    default_value=" ",
                    size=(20,1),
                    key="-TAGGED-",
                    enable_events=True,
                    readonly=True,
                )
            ],
            [
                sg.Text("Entidades nombradas"),
                sg.Combo(
                    named_entities,
                    default_value=" ",
                    size=(20,1),
                    key="-NAMED_ENTITIES-",
                    enable_events=True,
                    readonly=True,
                ),
            
                sg.Text("Palabras filtradas"),
                sg.Combo(
                    filtered_words,
                    default_value=" ",
                    size=(20,1),
                    key="-FILTERED_WORDS-",
                    enable_events=True,
                    readonly=True,
                ),
            ],
            [sg.Button('BORRAR TODO'), sg.Button('EXIT')],
    ]
def main():
    global confs
    layout = [
    [
        sg.Column(conf_layout),
    ]
    ]

    window = sg.Window('Tarea EBAC Valeria Legaria', layout)

    while True:             # Event Loop
        try:
            event, values= window.read()
            if event in (sg.WIN_CLOSED, 'EXIT'):
                break
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
                

            if event == "CONTADOR":
                window['-OUTPUT-'].update('')
                try:
                    contador = 0
                    while contador < int(values["-NUMERO-"]):
                        print("El contador es", contador)
                        contador += 1
                except:
                    print("El valor debe ser numérico y entero")

            if event == "IMPRIMIR":
                window['-OUTPUT-'].update('')
                try:
                    result = process_text(values["-LISTA-"])
                    frutas = result[0]
                    for fruta in frutas:
                        print("Me gusta comer", fruta)
                except:
                    print("La lista debe estar escrita de la forma: Pera. Uva. Fresa")

            if event == "CALCULAR AREA":
                try:
                    area = float(values["-BASE-"]) * float(values["-ALTURA-"])
                    print("El area del rectangulo de base", values["-BASE-"], "y altura", values["-ALTURA-"], "es: ", area)
                except:
                    print("Los valores de base y altura deben ser numéricos")
                    
            if event == "CALCULAR RAIZ":
                try:
                    area = math.sqrt(float(values["-RAIZ-"]))
                    print("La raiz cuadrada de", values["-RAIZ-"], "es:", area)
                except:
                    print("El valor para cacular la raiz debe ser numérico")

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
            pass


    window.close()
if __name__ == "__main__":
    main()