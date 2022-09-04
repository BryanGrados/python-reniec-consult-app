from cProfile import label
from email import header
from lib2to3.pgen2 import token
import tkinter
from tkinter import E, messagebox as mb
import requests
import json

#Creamos la ventana
ventana = tkinter.Tk()
ventana.title("Reniec App")

#Creamos los frames
frm = tkinter.Frame(ventana)
frm.grid(column=0, row=0, padx=(25, 25))

label1 = tkinter.Label(frm, text="Consulta DNI:", font="-weight bold")
label1.grid(column=0, row=0, pady=10)

anchoText = 35
#Buscar DNI
txtDNIBuscar = tkinter.Entry(frm, width=anchoText)
txtDNIBuscar.grid(column=0, row=1, pady=10)

#Boton para buscar DNI
btnBuscar = tkinter.Button(frm, text="Buscar", width=17, bg="skyblue", fg="white", command= lambda: buscar())
btnBuscar.grid(column=0, row=2, pady=20)

#Respuesta
fila = 3

#DNI-CUI
label2 = tkinter.Label(frm, text="DNI - CUI:", font="-weight bold")
label2.grid(column=0, row=fila, sticky="w")
fila = fila + 1


txtDniCui = tkinter.Entry(frm, width=anchoText)
txtDniCui.grid(column=0, row=fila, sticky="w")
fila = fila + 1

#Paterno
label2 = tkinter.Label(frm, text="A. Paterno: ")
label2.grid(column=0, row=fila, sticky="w")
fila = fila + 1

txtPaterno = tkinter.Entry(frm, width=anchoText)
txtPaterno.grid(column=0, row=fila, sticky="w")
fila = fila + 1

#Materno
label2 = tkinter.Label(frm, text="A. Materno: ")
label2.grid(column=0, row=fila, sticky="w")
fila = fila + 1

txtMaterno = tkinter.Entry(frm, width=anchoText)
txtMaterno.grid(column=0, row=fila, sticky="w")
fila = fila + 1

#Nombres
label2 = tkinter.Label(frm, text="Nombres: " )
label2.grid(column=0, row=fila, sticky="w")
fila = fila + 1

txtNombres = tkinter.Entry(frm, width=anchoText)
txtNombres.grid(column=0, row=fila, sticky="w")
fila = fila + 1

#Sexo
label2 = tkinter.Label(frm, text="Sexo: ")
label2.grid(column=0, row=fila, sticky="w")
fila = fila + 1

txtSexo = tkinter.Entry(frm, width=anchoText)
txtSexo.grid(column=0, row=fila, pady=(0, 10), sticky="w")
fila = fila + 1

#Accion procesar
def buscar():
    dni = txtDNIBuscar.get()  
    
    txtPaterno.delete(0, tkinter.END)
    txtMaterno.delete(0, tkinter.END)
    txtNombres.delete(0, tkinter.END)
    txtDniCui.delete(0, tkinter.END)
    txtSexo.delete(0, tkinter.END)
    
    #Obtenemos API
    url = "https://www.softwarelion.xyz/api/reniec/reniec-dni"
    _json = { "dni": dni }
    token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyNTQzLCJjb3JyZW8iOiJicnlhbmdyYWRvczlAZ21haWwuY29tIiwiaWF0IjoxNjYyMjYwOTY2fQ.DbMsaTK_98uE5N9MOjQfWEI3gYqSPVhCpdKgxICQcb4"
    _headers = {'Content-Type': 'application/json', 'Authorization': token}

    #Realizamos la peticion
    response = requests.post(url, data=json.dumps(_json), headers=_headers)

    #Obtenemos el resultado
    datajson = response.json()
    
    #Verificamos si el DNI existe
    if(datajson['success'] == False):
        mb.showwarning("Advertencia", datajson['message'])
        return
    
    #Mostramos los datos
    persona = datajson['result']

    
    txtPaterno.insert(0, persona['paterno'])
    txtPaterno.config(state="readonly")
    
    txtMaterno.insert(0, persona['materno'])
    txtMaterno.config(state="readonly")
    
    txtNombres.insert(0, persona['nombres'])
    txtNombres.config(state="readonly")
    
    txtDniCui.insert(0, dni + "-" + persona['codigoVerificacion'])
    txtDniCui.config(state="readonly")
    
    txtSexo.insert(0, persona['sexo'])
    txtSexo.config(state="readonly")

ventana.mainloop()