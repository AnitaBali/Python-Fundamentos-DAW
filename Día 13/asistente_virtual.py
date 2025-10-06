#Esta biblioteca te permite convertir texto a voz. Es útil para que tu programa "hable" y
#comunique información verbalmente al usuario.
import time

import pyttsx3

#Es la biblioteca que se encarga de convertir el audio a texto. Funciona como un "oído"
#para que tu programa pueda entender lo que dice el usuario.
import speech_recognition as sr

#Con esta biblioteca puedes automatizar tareas de WhatsApp, como enviar mensajes a un contacto
#en una hora específica o reproducir un video de YouTube.
import pywhatkit

#Esta es la biblioteca perfecta para obtener datos financieros del mercado de valores.
#Te permite consultar información sobre acciones, bonos, y otros activos.
import yfinance as yf

#Como su nombre indica, esta biblioteca te sirve para generar chistes al azar, lo que puede ser
#útil para añadir un toque divertido a tu programa.
import pyjokes

#Es una biblioteca estándar que te permite controlar y abrir el navegador web desde tu código.
#Es útil para abrir páginas web o realizar búsquedas en línea.
import webbrowser

#Esta biblioteca maneja fechas y horas. Con ella puedes obtener la fecha y hora actual,
#calcular diferencias entre fechas, o formatear la información de tiempo para mostrarla como necesites.
import datetime

#Te permite acceder y obtener información de Wikipedia directamente desde tu script,
#facilitando la búsqueda de datos y resúmenes sobre casi cualquier tema.
import wikipedia

# Función para escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():
    # Almacenar recognizer en una variable
    r=sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as origen:

        # Tiempo de espera
        r.pause_threshold=0.8

        # Informar que comenzco la grabación
        print("Ya puedes hablar.")

        # Guardar lo que escuche como audio
        audio= r.listen(origen)

        try:
            # Buscar en google
            pedido=r.recognize_google(audio,language="es-es")

            # Prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # Devolver a pedido
            return pedido

        # Excepción en caso de que no comprenda el audio
        except sr.UnknownValueError:
            # Prueba de que no comprendio el audio
            print("Ups, no entendi.")

            #Devolver error
            return "Sigo esperando."

        # Excepción en caso de no resolver el pedido
        except sr.RequestError:
            # Prueba de que no comprendio el audio
            print("Ups, no hay servicio.")

            # Devolver error
            return "Sigo esperando."

        # Error inesperadp
        except:
            # Prueba de que no comprendio el audio
            print("Ups, algo ha salido mal.")

            # Devolver error
            return "Sigo esperando."

# Función para que el asistente de voz pueda ser escuchado
def hablar(mensaje):

    # Encender el motor de pyttsx3
    engine=pyttsx3.init()

    #Obtener la lista de voces disponibles
    voces=engine.getProperty("voices")

    # Imprimir información sobre cada voz para que puedas elegir
    # (Opcional, pero muy útil para saber qué voces tienes)
    #for i, voz in enumerate(voces):
    #    print(f"Voz {i}: ID={voz.id}, Nombre={voz.name}, Idioma={voz.languages}")

    # Seleccionar la voz deseada
    # Elige la voz que quieras de la lista que imprimiste.
    # Por ejemplo, para elegir la primera voz de la lista, usa el índice 0.
    # Puedes cambiar 'voces[0]' por 'voces[1]', 'voces[2]', etc.
    try:
        engine.setProperty('voice', voces[1].id)
    except IndexError:
        print("No se encontraron voces disponibles.")
        return

    # Pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Informar el dia de la semana
def pedir_dia():

    # Crear la variable con datos de hoy
    dia_actual=datetime.date.today()
    print(dia_actual)

    # Crear la variable con datos de hoy
    dia_semana=dia_actual.weekday()

    # Diccionario con nombres de los días
    semana_dias={0:"Lunes",1:"Martes",2:"Miércoles",3:"Jueves",4:"Viernes",5:"Sábado",6:"Domingo"}

    #Decir dia de la semana
    hablar(f"Hoy es {semana_dias[dia_semana]}")

    #for valor,dia in semana_dias.items():
    #    if valor==dia_semana:
    #        print(dia)

# Informar hora
def pedir_hora():
    # Crear la variable con la hora
    hora = datetime.datetime.now()

    #Asistente decir hora
    hablar(f"Son las {hora.hour} y {hora.minute} minutos.")

# Saludo inicial
def saludo_inicial():

    # Crear variable con datos de hora
    hora=datetime.datetime.now()
    if hora.hour <6 or hora.hour> 20:
        momento="Buenas noches"
    elif 6 <= hora.hour < 13:
        momento="Buenos días"
    else:
        momento="Buenas tardes"

    # Decir el saludo
    hablar(f"{momento}, soy Ana, tu asistente personal. Por favor, dime en que te puedo ayudar.")

# Función central del asistente
def pedir():

    #Activar saludo inicial
    saludo_inicial()

    #Variable de fin del loop
    comenzar=True
    while comenzar:

        #Activar el micro y guardar el pedido en un string
        pedido=transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo Youtube')
            webbrowser.open('https://www.youtube.com')
            continue

        elif 'abrir navegador' in pedido:
            hablar('Con gusto, estoy abriendo el Navegador')
            webbrowser.open('https://www.google.com')
            continue

        elif 'dime el día' in pedido:
            pedir_dia()
            continue

        elif 'dime la hora' in pedido:
            pedir_hora()
            continue

        elif 'busca en wikipedia' in pedido:
           hablar('Buscando eso en Wikipedia')
           pedido=pedido.replace('busca en wikipedia','')
           wikipedia.set_lang('es')
           resultado=wikipedia.summary(pedido,sentences=2)
           hablar("Wikipedia dice lo siguente: ")
           hablar(resultado)
           continue

        elif 'busca en internet' in pedido:
            hablar('Buscando eso en Internet')
            pedido=pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue

        elif 'reproducir' in pedido:
            hablar("Buena idea, ya comienzo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue

        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue

        elif 'precio de las acciones' in pedido:
            accion=pedido.split('de')[-1].strip()
            cartera={'apple':'APPL',
                     'amazon':'AMZN',
                     'google':'GOOGL'}

            try:
                accion_buscada=cartera[accion]
                accion_buscada=yf.Ticker(accion_buscada)
                precio_actual=accion_buscada.info['regularMarketPrice']
                hablar(f"La encontre, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("Perdón, pero no la he encontrado.")
                continue

        elif 'adiós' in pedido:
            hablar("Espero haberte ayudado. Gracias.")
            break


pedir()



