import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import webbrowser
import datetime
import wikipedia

#Rutas de los paquetes de voz instalados en mi pc
#idV1_espmex = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
#idV2_jap = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0'

#Funcion para escuchar el micro y devolver audio como texto:
def transformar_audio_a_texto():

    #Almacenamos el recognizer en una variable
    r = sr.Recognizer()

    #Configuracion del microfono
    with sr.Microphone() as origen:

        #Tiempo de espera entre la activacion del microfono y escucha
        r.pause_threshold = 0.8 #.pause_threshold es el umbral de espera

        #Informe de comienzo de la grabacion, para testeos
        print('Grabacion iniciada')

        #Guardado del audio
        audio = r.listen(origen)

        try:
            #Busqueda de lo escuchado en google
            pedido = r.recognize_google(audio, language='es-mex')

            #Prueba de que el pedido se ingresó correctamente
            print('Dijiste: ' + pedido)

            #Retorno de pedido
            return pedido

        #En caso de no comprender el audio:
        except sr.UnknownValueError:
            #Prueba de audio no comprendido
            print('...No entendí que dijiste')
            #Devolucion de error
            return 'Sigo esperando...'

        #En caso de no poder resolver el pedido:
        except sr.RequestError:
            # Prueba de pedido
            print('...Mhm...creo que lo haré después...')
            # Devolucion de error
            return 'Sigo esperando...'

        #Errores inseperados
        except:
            # Prueba de audio y errores inesperados
            print('...Ah! Hubo un error...')
            # Devolucion de error
            return 'Sigo esperando...'

#Funcion para que Mara hable:
def hablar(mensaje):

    #Encender el motor de pyttsx3
    engine = pyttsx3.init()
    #Ejemplo de como configurar el idioma:
    #engine.setProperty('voice', idV2_jap)
    #Si esta línea de codigo no se escribe se usa el formato de voz predefinido del pc

    #Iniciar voz
    engine.say(mensaje)
    engine.runAndWait()

#Funcion para pedir la fecha:
def pedir_dia():
    #Variable que almacena el día actual
    dia = datetime.date.today()

    #Variable para almacenar el día de la semana
    dia_semana = dia.weekday()

    #Diccionario con los nombres de los días:
    calendario_semanal = {0:'Lunes', 1:'Martes', 2:'Miércoles', 3:'Jueves', 4:'Viernes', 5:'Sábado', 6:'Domingo'}

    #Decir el día de la semana:
    hablar(f'Hoy es {calendario_semanal[dia_semana]}')

#Funcion para pedir la hora:
def pedir_hora():
    #Variable que almacena la fecha y hora actual:
    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} con {hora.minute} minutos.'

    #Llamada para decir la hora
    hablar(hora)

#Funcion de saludo:
def saludo_inicial():
    #Variable para almacenar hora y fecha
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches~, ¿no crees que ya deberías ir a dormir?'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día~, ¿así que hoy empezamos temprano?'
    else:
        momento = 'Buenas tardes~, jumjum, ¿ya está listo el arroz?'
    #Llamada para decir el mensaje de saludo
    hablar(f'{momento}, de todas formas, soy Mara, asistente virtual y proyecto en proceso. ¿Necesitas algo?')

#Funcion principal:
def pedidos():
    #Llamada al saludo inicial
    saludo_inicial()

    #Variable para mantener activo al asistente
    continuar = True

    #Loop de la aplicacion
    while continuar:
        #Encender microfono y almacenar pedido en un string
        pedido = transformar_audio_a_texto().lower()

        if 'abre youtube' in pedido:
            hablar('Claro, dame un momento...')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abre el navegador' in pedido:
            hablar('¡Entendido! Dame un momento')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Vale, me pongo a buscarlo...')
            pedido = pedido.replace('busca en wikipedia', '').strip()  # Elimina espacios adicionales
            if not pedido:  # Si no quedó texto después del reemplazo
                hablar('...¿Quieres que busque en wikipedia...."busca en wikipedia"?')
                continue
            wikipedia.set_lang('es')
            try:
                resultado = wikipedia.summary(pedido, sentences=1)
                hablar('Wikipedia dice que...')
                hablar(resultado)
            except wikipedia.exceptions.PageError:
                hablar(f'No encontré información sobre {pedido} en Wikipedia.')
            except wikipedia.exceptions.DisambiguationError:
                hablar('Hay varias opciones, ¿puedes ser más especifico?')
            continue
        elif 'busca en internet' in pedido:
            hablar('Claro, dame un momento~')
            pedido = pedido.replace('busca en internet', '').strip()
            if not pedido:  # Si no quedó texto después del reemplazo
                hablar('...¿Qué debo buscar en internet?')
                continue
            pywhatkit.search(pedido)
            hablar('Encontré esto.')
            continue
        elif 'reproduce' in pedido:
            hablar('¡Oh! Vale vale, me pongo a ello.')
            pedido = pedido.replace('reproduce', '').strip()
            pywhatkit.playonyt(pedido)
            continue
        elif 'un chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'adiós' in pedido:
            hablar('Claro, ¡hablamos luego!')
            break

pedidos()

