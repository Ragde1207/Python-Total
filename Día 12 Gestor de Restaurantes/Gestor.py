from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

#Funcion para la registrar los botones en la calculadora:
def clic_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)
#Funcion para borrar los datos de la calculadora:
def borrado():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)
#Funcion para realizar la operación matematica
def obtener_resultado():
    global operador
    resultado = str(eval(operador))

    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0,resultado)

    operador = ''
#Funcion para activar las cajas de texto
def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1
#Funcion para obtener el total a pagar
def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    completo = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(completo, 2)}')
#Funcion para editar el contenido del ticket
def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 55 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto\n')
    texto_recibo.insert(END, f'-' * 68 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t$'
                                     f'{int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t$'
                                     f'{int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postres in texto_comida:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t$'
                                     f'{int(postres.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 68 + '\n')
    texto_recibo.insert(END, f'Costo de almuerzo: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de bebidas: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de postres: \t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 68 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'-' * 68 + '\n')
    texto_recibo.insert(END, f'Vuelva pronto!')
#Funcion para guardar el ticket
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'El recibo ha sido guardado correctamente')
#Funcion para resetear pantalla
def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

#Inicialización de Tkinter:
aplicacion = Tk()

#Tamaño de ventana:
aplicacion.geometry('1020x630+0+0')
#.geometry define el tamaño de la ventana, siendo ('Dimensiones+posición en eje X+posición en eje Y')

#Edición de maximizar ventana:
aplicacion.resizable(0, 0)
#.resizable establece el maximo de modicicación de la ventana

#Edición del titulo de la ventana:
aplicacion.title('Sistema Gestor')

#Editar el color de la ventana:
aplicacion.config(bg='lemon chiffon')

#--------------------------------------------Paneles-------------------------------------------------

#Panel superior de la aplicacion:
panel_superior = Frame(aplicacion, bd=1, relief=SUNKEN) #Frame(localización del panel, tamaño del borde, relieve)
#Frame: Clase de Tkinter para construir paneles
panel_superior.pack(side=TOP) #.pack(side='Parte de la aplicación')
#.pack se utiliza para colocar el panel

#Contenido del panel superior
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4', font=('Arial',50),
                        bg='burlywood', width=27)
#Label('Parte de la app donde se localiza la etiqueta', text='Texto de la etiqueta', fg='Color del texto',
#       font=('Tipo de fuente',Tamaño) bg='Color del fondo de la etiqueta',width=Ancho de la etiqueta)
etiqueta_titulo.grid(row=0, column=0)

#Panel izquierdo:
panel_izquierdo = Frame(aplicacion, bd=1, relief=SUNKEN)
panel_izquierdo.pack(side=LEFT)

#Panel de Costos:
panel_costos = Frame(panel_izquierdo, bd=1, relief=SUNKEN, bg='azure4', padx=55)
panel_costos.pack(side=BOTTOM)

#Panel de Comidas:
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Arial', 15, 'bold'),
                           bd=1, relief=SUNKEN, fg='azure4')
panel_comidas.pack(side=LEFT)

#Panel de Bebidas:
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebida', font=('Arial', 15, 'bold'),
                           bd=1, relief=SUNKEN, fg='azure4')
panel_bebidas.pack(side=LEFT)

#Panel de Postres:
panel_postres = LabelFrame(panel_izquierdo, text='Postre', font=('Arial', 15, 'bold'),
                           bd=1, relief=SUNKEN, fg='azure4')
panel_postres.pack(side=LEFT)

#Panel derecho:
panel_derecho = Frame(aplicacion, bd=1, relief=SUNKEN)
panel_derecho.pack(side=RIGHT)

#Panel Calculadora:
panel_calculadora = Frame(panel_derecho, bd=1, relief=SUNKEN, bg='burlywood')
panel_calculadora.pack()

#Panel Recibos:
panel_recibo = Frame(panel_derecho, bd=1, relief=SUNKEN, bg='burlywood')
panel_recibo.pack()

#Panel Botones:
panel_botones = Frame(panel_derecho, bd=1, relief=SUNKEN, bg='burlywood')
panel_botones.pack()

#--------------------------------------------Variables-------------------------------------------------

#Lista de productos:
lista_comidas = ['pollo', 'coredero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

variables_comida = []
variables_bebida = []
variables_postres = []

cuadros_comida = []
texto_comida = []
cuadros_bebida = []
texto_bebida = []
cuadros_postres = []
texto_postres = []

var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

#-----------------------------------------Loops generadores--------------------------------------------

#Generador de items comida:
contador = 0
for comida in lista_comidas:
    #Generar Checkbuttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold',), onvalue=1,
                         offvalue=0, variable=variables_comida[contador], command=revisar_check)
    comida.grid(row=contador, column=0, sticky=W)

    # Cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', 18, 'bold'), bd=1,
                                     width=6, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1

#Generador de items bebida:
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold',), onvalue=1,
                         offvalue=0, variable=variables_bebida[contador], command=revisar_check)
    bebida.grid(row=contador, column=0, sticky=W)

    #Cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Dosis', 18, 'bold'), bd=1,
                                     width=6, state=DISABLED, textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1

#Generador de items postre:
contador = 0
for postres in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres, text=postres.title(), font=('Dosis', 19, 'bold'), onvalue=1,
                          offvalue=0, variable=variables_postres[contador], command=revisar_check)
    postres.grid(row=contador, column=0, sticky=W)

    # Cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres, font=('Dosis', 18, 'bold'), bd=1,
                                     width=6, state=DISABLED, textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)

    contador += 1

#-------------------------------------------Etiquetas inferiores--------------------------------------------

#Etiquetas de costos y campos de entrada:
#Comidas
etiqueta_costos_comida = Label(panel_costos, text='Costo Comida:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costos_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10,
                           state='readonly', textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

#Bebidas
etiqueta_costos_bebida = Label(panel_costos, text='Costo Bebida:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costos_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10,
                           state='readonly', textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

#Postres
etiqueta_costos_postres = Label(panel_costos, text='Costo Postres:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costos_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10,
                           state='readonly', textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

#Subtotal
etiqueta_subtotal = Label(panel_costos, text='Subtotal:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal= Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10,
                           state='readonly', textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

#Impuestos
etiqueta_impuestos = Label(panel_costos, text='Impuestos:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos= Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10,
                           state='readonly', textvariable=var_impuesto)
texto_impuestos.grid(row=1, column=3, padx=41)

#Total
etiqueta_total = Label(panel_costos, text='Total:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total= Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10,
                           state='readonly', textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

#--------------------------------------------Botones-------------------------------------------------

botones = ['total', 'recibo', 'guardar', 'reset']
botones_creados = []

columnas = 0

for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=('Dosis', 10, 'bold'),
                   fg='White', bg='azure4', bd=1, width=9)
    botones_creados.append(boton)

    boton.grid(row=0, column=columnas)

    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

#Recibos
texto_recibo = Text(panel_recibo, font=('Dosis', 10, 'bold'), bd=1, width=42, height=20)
texto_recibo.grid(row=0, column=0)

#--------------------------------------------Calculadora-------------------------------------------------

visor_calculadora = Entry(panel_calculadora, font=('Dosis', 16, 'bold'), width=19, bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', '=', 'Borrar', '0', '/']
botones_guardados = []
fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(), font=('Dosis', 11, 'bold'),
                   fg='white', bg='azure4', bd=1, width=8)
    boton.grid(row=fila, column=columna)

    botones_guardados.append(boton)

    if columna == 3:
        fila += 1

    columna +=1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : clic_boton('7'))
botones_guardados[1].config(command=lambda : clic_boton('8'))
botones_guardados[2].config(command=lambda : clic_boton('9'))
botones_guardados[3].config(command=lambda : clic_boton('+'))
botones_guardados[4].config(command=lambda : clic_boton('4'))
botones_guardados[5].config(command=lambda : clic_boton('5'))
botones_guardados[6].config(command=lambda : clic_boton('6'))
botones_guardados[7].config(command=lambda : clic_boton('-'))
botones_guardados[8].config(command=lambda : clic_boton('1'))
botones_guardados[9].config(command=lambda : clic_boton('2'))
botones_guardados[10].config(command=lambda : clic_boton('3'))
botones_guardados[11].config(command=lambda : clic_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrado)
botones_guardados[14].config(command=lambda : clic_boton('0'))
botones_guardados[15].config(command=lambda : clic_boton('/'))

#Funcion para mantener pantalla de app abierta:
aplicacion.mainloop()