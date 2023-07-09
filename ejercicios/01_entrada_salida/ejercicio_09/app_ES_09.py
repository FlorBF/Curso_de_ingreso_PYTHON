import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: florencia belen 
apellido: farías
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Incremento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        sueldo_texto = self.txt_sueldo.get()
        incremento_texto = self.txt_incremento.get()
        #float para convertir texto en flotante (numeros con (,) ej: 12.3)
        sueldo_numero = float(sueldo_texto)
        incremento_numero =  float(incremento_texto)

        incremento_pesos = sueldo_numero * incremento_numero / 100
        sueldo_resultado_numero = sueldo_numero + incremento_pesos
        #mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
        alert("sueldo", f"El sueldo actualizado es: {sueldo_resultado_numero}")





    
'''  EJEMPLO DEL PROFE
     
      PRECIO = 1000
                #AUMENTO
           #porcentaje= PRECIO * 0.10
        #aumento = PRECIO* 10 / 100 #muestra el aumento
        #se agrega un punto .10 y luego el desimal ej: 1.10

        #precio_final = PRECIO + aumento
        precio_final = PRECIO * 1.10 #esto solo muestra el resultado final

                #DESCUENTO
        descuento = PRECIO * 10/100
        precio_final = PRECIO - descuento
        precio_final = PRECIO * 1.10

        #si necesito sacarle al 100 porciento 10 porciento 
        #100 - 10 = 90 al 100 porciento le resto 0.10
        precio_final = PRECIO * 0.90

        #el float o flotantes, son los reales ej 10.5 - 0.5- 100.9999
        # el int son numeros enteros, convierte texto en numeros enterosnumeros enteros
        '''
       


        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()