import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: florencia belen
apellido: farías
---
Ejercicio: entrada_salida_06
---
Enunciado:
Al presionar el botón  'Sumar', se deberán obtener los valores contenidos en las cajas de texto (txt_operador_A y txt_operador_B), 
transformarlos en números enteros, realizar la suma y luego mostrar el resultado de la operación utilizando el Dialog Alert. 
Ej: "El resultado de la sumas es: 755" 
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
        self.btn_sumar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_sumar_on_click(self):
        #self.txt_operador_a = lo guarde en mi variable numero
        #self.txt_operador_b =lo guarde en mi variable numero

        #guardo el numero que ingreso el usuario en texto y luego lo paso a numero entero
        #ej de lo que sucede si no lo convierto a numero "5" + "5"= se concatena, o sea =55, no lo suma.
        numero_uno_texto = self.txt_operador_a.get()
        #convierte el texto a numero(int)
        numero_uno_a_numero = int(numero_uno_texto)
        
        numero_dos_texto  = self.txt_operador_b.get()
        #convierte el texto a numero(int)
        numero_dos_a_numero = int(numero_dos_texto)
        #int= num entero

        #(resultado en numero)
        resultado = numero_uno_a_numero + numero_dos_a_numero
        #necesito convertir "numero_uno_a_numero + numero_dos_a_numero" a texto, porque "resultado" es numero, utilizando str

         #"El resultado de la suma es : 755"
         #convierto el numero a texto para concatenar con str=Texto
        resultado_a_texto = str(resultado)

        mensaje = ("El resultado de la seuma es: " + resultado_a_texto)
        #          "el resultado de la suma es: "  +  ej:"20" resultado de la suma que hagamos

        alert(title="respuesta", message=mensaje) # con esto quedaría "el resultado de la suma es: xxxx"

        #SI LO PONGO ASÍ, CONCATENA Y NO ME SUMA:
        # alert(title="sumador",message="el resultado es : " + resultado) porque el + concatena.


                 #otra opción
       # operador_a= int(self.txt_operador_a.get())
        #operador_b= int(self.txt_operador_b.get())
        #alert(title="ejercicio 06",message=f"el reesultado de la suma es :{operador_a+operador_b}")


       # pass
     
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()