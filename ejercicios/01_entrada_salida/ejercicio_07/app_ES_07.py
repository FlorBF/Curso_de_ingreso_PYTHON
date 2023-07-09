import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: florencia belén
apellido: farías
---
Ejercicio: entrada_salida_07
---
Enunciado:
Al presionar el botón  que corresponde a cada operación (suma, resta, multiplicación, y división), 
se deberán obtener los valores contenidos en las cajas de texto (txtOperadorA y txtOperadorB), 
transformarlos en números enteros, realizar dicha operación y luego mostrar el resultado 
de la misma utilizando el Dialog Alert. Ej: "El resultado de la …… es: 755"  
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)
        
        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_restar = customtkinter.CTkButton(master=self, text="Restar", command=self.btn_restar_on_click)
        self.btn_restar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_multiplicar = customtkinter.CTkButton(master=self, text="Multiplicar", command=self.btn_multiplicar_on_click)
        self.btn_multiplicar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_dividir = customtkinter.CTkButton(master=self, text="Dividir", command=self.btn_dividir_on_click)
        self.btn_dividir.grid(row=5, pady=10, columnspan=2, sticky="nsew")

       
          #              SUMA
    def btn_sumar_on_click(self):
        #nombre = self.txt_nombre.get()

        numero_uno_texto = self.txt_operador_a.get()
        numero_uno_a_numero = int(numero_uno_texto)

        numero_dos_texto = self.txt_operador_b.get()
        numero_dos_a_numero = int(numero_dos_texto)

        resultado = numero_uno_a_numero + numero_dos_a_numero
        resultado_a_texto = str(resultado)

        mensaje= "El resultado de la suma es: " + resultado_a_texto #el + está concatenando porque el resultado fue pasado a texto

        alert(title="suma",message=mensaje)



 #operadores aritmeticos:
        #suma +
        #resta -
        #div /
        #multip *
        #% modulo= nos da el resto de una division
        
         #               RESTA
    def btn_restar_on_click(self):
        numero_uno_texto = self.txt_operador_a.get()
        numero_uno_a_numero = int(numero_uno_texto)

        numero_dos_texto = self.txt_operador_b.get()
        numero_dos_a_numero= int(numero_dos_texto)

        resultado = numero_uno_a_numero - numero_dos_a_numero

        resultado_a_texto = str(resultado)
        mensaje= "El resultado de la resta es: " + resultado_a_texto # este + se deja porque no esta "sumando" esta concatenando

        alert(title="resta",message=mensaje)
       # pass


         #               MULTIPLICACIÓN
    def btn_multiplicar_on_click(self):
        numero_uno_texto = self.txt_operador_a.get()
        numero_uno_a_numero = int(numero_uno_texto)

        numero_dos_texto = self.txt_operador_b.get()
        numero_dos_a_numero= int(numero_dos_texto)

        resultado = numero_uno_a_numero * numero_dos_a_numero

        resultado_a_texto = str(resultado)
        mensaje= "El resultado de la multiplicación es: " + resultado_a_texto # este + se deja porque no esta "sumando" esta concatenando

        alert(title="multiplicació",message=mensaje)

        #               DIVISIÓN
    def btn_dividir_on_click(self):
        numero_uno_texto = self.txt_operador_a.get()
        numero_uno_a_numero = int(numero_uno_texto)

        numero_dos_texto = self.txt_operador_b.get()
        numero_dos_a_numero= int(numero_dos_texto)

        resultado = numero_uno_a_numero / numero_dos_a_numero

        resultado_a_texto = str(resultado)
        mensaje= "El resultado de la División es: " + resultado_a_texto # este + se deja porque no esta "sumando" esta concatenando

        alert(title="División",message=mensaje)
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()