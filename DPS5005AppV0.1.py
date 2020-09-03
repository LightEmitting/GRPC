from __future__ import print_function
import tkinter as tk
from tkinter import *
#from tkinter.ttk import *
import _tkinter

#import tkMessageBox
import os

#greeter_client
import logging
import grpc
import helloworld_pb2
import helloworld_pb2_grpc
#---

os.system('clear')
root = tk.Tk()
#root = tk()
root.title('DPS5005 Remote App')
root.geometry("425x400")
#img=PhotoImage(file='~/Descargas/DPS.ico')
#root.tk.call('wm', 'iconphoto', root._w, img)

# -------------------------------- Funtions --------------------------------
def txt(power):
    textbox_code.delete(0, END)
    textbox_code.insert(0, power)
    if power == "OUTPUT ON":
        textbox_2.configure(state='normal')
        textbox_3.configure(state='normal')
        textbox_4.configure(state='normal')
        textbox_5.configure(state='normal')

    else:
        textbox_2.configure(state='disable')
        textbox_3.configure(state='disable')
        textbox_4.configure(state='disable')
        textbox_5.configure(state='disable')

    return 

def txt_add(power):
    textbox_code.insert(0, power)
    return 

def show_code(test):
    textbox_code.delete(0, END)

    state = str(textbox_2['state'])
    if (state == 'disabled'):
        textbox_code.insert(0, "OUTPUT OFF")
        code="OUTPUT OFF"
        return code

    code = '' 
    if (len(textbox_5.get()) != 0 and textbox_5.get().isdigit()):
        textbox_code.insert(0, " MAX C "+ textbox_5.get())
        code = code + "MAX C " + str(textbox_5.get())

    if (len(textbox_4.get()) != 0 and textbox_4.get().isdigit()):
        textbox_code.insert(0, " MAX V "+ textbox_4.get())
        code = "MAX V " + str(textbox_4.get()) + '\n' + code
        
    if (len(textbox_3.get()) != 0 and textbox_3.get().isdigit()):
        textbox_code.insert(0, " SET C "+ textbox_3.get())
        code = "SET C " + str(textbox_3.get()) + '\n' + code
    
    if (len(textbox_2.get()) != 0 and textbox_2.get().isdigit()):
        textbox_code.insert(0, " SET V "+ textbox_2.get())
        code = "SET V " + str(textbox_2.get()) + '\n' + code
        
    textbox_code.insert(0, "OUTPUT ON ")
    code = 'OUTPUT ON\n' + code 
    return code

def run(code):
    if len(textbox_1.get()) != 0:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = helloworld_pb2_grpc.GreeterStub(channel)
            response = stub.SayHello(helloworld_pb2.HelloRequest(name=code))
        print(response.message)
        openNewWindow_1(response.message)

    else:
        openNewWindow_2()
#if __name__ == '__main__':
#    logging.basicConfig()
#    run('no se para que es')    

# function to open a new window on a button click 
def openNewWindow_1(msj): 
    newWindow = Toplevel(root) 
    newWindow.title("Estado") 
    newWindow.geometry("350x200") 
    Label(newWindow, text = msj).grid(padx=0, pady=0)     

def openNewWindow_2(): 
    newWindow = Toplevel(root) 
    newWindow.title("Error: 001") 
    newWindow.geometry("200x200") 
    Label(newWindow, text ="Por favor Ingrese su nombre").grid(padx=0, pady=0)     
# -------------------------------- Define Buttons & Labels & Entrys --------------------------------
label_1 = Label(root, text="Enter your name:")          #name
textbox_1 = Entry(root, state='normal', width=25)                       #entry name

button_1 = Button(root, text="ON", padx=80, pady=20, command=lambda: txt("OUTPUT ON"))   #off button
button_2 = Button(root, text="OFF", padx=80, pady=20, command=lambda: txt("OUTPUT OFF"))       #on button

textbox_2 = Entry(root, state='disable', width=25)
textbox_3 = Entry(root, state='disable', width=25)
label_3 = Label(root, text="Voltage [V]:")
textbox_code = Entry(root, width=50, borderwidth=2)     #entry code

label_2 = Label(root, text="Voltage [V]:")              #voltageerror
label_4 = Label(root, text="V max [V]:")                #maximum voltage
textbox_4 = Entry(root, state='disable', width=25)                       #entry max vol

label_5 = Label(root, text="I maxv [A]:")               #maximum current    
textbox_5 = Entry(root, state='disable', width=25)                       #entry max cur

#button_3 = Button(root, padx=80, pady=20, text="Set", command= openNewWindow)           #set button

button_3 = Button(root, padx=80, pady=20, text="Set", command=lambda: run(show_code(0)))           #set button
#button_3.grid(pady = 10)
button_code = Button(root, text="Code", padx=80, pady=20, command=lambda: show_code(0))    #code button


# -------------------------------- Put the buttons on the screen --------------------------------
label_1.grid(row=1, column=0)
textbox_1.grid(row=1, column=1)

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)

label_2.grid(row=3, column=0)
textbox_2.grid(row=3, column=1)

label_3.grid(row=4, column=0)
textbox_3.grid(row=4, column=1)

label_4.grid(row=5, column=0)
textbox_4.grid(row=5, column=1)

label_5.grid(row=6, column=0)
textbox_5.grid(row=6, column=1)

textbox_code.grid(row=7, column=0, columnspan=2, padx=0, pady=0)

button_3.grid(row=8, column=0)
button_code.grid(row=8, column=1)

#advice.detachedHead = false

root.mainloop()