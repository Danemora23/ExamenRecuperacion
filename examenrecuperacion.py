#Logica de sistemas
#primer semestre
#Darwin Daneri Morales López
#0907-19-11615
from tkinter import ttk
from tkinter import *
 
class Desk:
    def __init__(self, window):
      
       
        #ancho
        ancho = 400
       
        #alto
        alto = 250
       
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window
 
        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))
 
        #centramos el contenido
        self.wind.columnconfigure(0, weight=1)
       
        #le damos un titulo a la ventana
        self.wind.title('EXAMEN RECUPERACION')
       
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'EXAMEN RECUPERACION')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
       
        # creamos un etiqueta
        Label(frame, text = '1er Numero: ').grid(row = 1, column = 0)
       
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
       
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = '2do Numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.focus()
        self.var2.grid(row = 2, column = 1)

         # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = '3er Numero: ').grid(row = 3, column = 0)
        self.var3 = Entry(frame)
        self.var3.focus()
        self.var3.grid(row = 3, column = 1)
       
        #Creamos un boton 1
        Button(frame, text = 'Boton 1', command = self.sumar).grid(row = 5, columnspan =2, sticky = W + E)

        #Creamos un boton 2
        Button(frame, text = 'Boton 2', command = self.resta).grid(row = 6, columnspan =2, sticky = W + E)
 
        #designamos un área de mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
       
    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0 and len(self.var3.get()) != 0
   
    # esta es la función primer boton
    def sumar(self):
        if self.validation():
            resultado = float( self.var1.get() ) * float( self.var2.get() ) * float( self.var3.get() )
            self.message['text'] = 'multiplicación de los 3 campos:{}'.format(resultado)
        else:
            self.message['text'] = 'los campos requeridos'

    # esta es la función segundo boton
    def resta(self):
        if self.validation():
            resultado = float( self.var1.get() ) > float( self.var2.get() )
            self.message['text'] = 'CONCATENAR:{}'.format(resultado)
        else:
            self.message['text'] = 'los campos requeridos' 

 
#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
   
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
   
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana
    app = Desk(window)
 
    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()