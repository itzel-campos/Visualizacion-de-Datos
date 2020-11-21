#Imports necesarios para la ejecucion del programa
import sys
import sqlite3
from sqlite3 import Error
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox

#Se crea la ventana del login
ventana_login = Tk()
ventana_login.title (" Ventana de acceso ")
ventana_login.geometry ("310x200")
ventana_login.resizable(0, 0)
color='Pink'  
ventana_login['bg']=color

#Se hacen las especificaciones del login 
usuario_label = Label(ventana_login, text = "Usuario:")
usuario_label.grid(row=1, column=0, padx=85, pady=5)
usuario_entry = Entry(ventana_login)
usuario_entry.grid(row=2, column=0, padx=85)

#Proteccion de la contraseña 
contraseña_label = Label(ventana_login, text = "Contraseña:")
contraseña_label.grid(row=3, column=0, padx=85, pady=5)
contraseña_entry = Entry(ventana_login, show = "*")
contraseña_entry.grid(row=4, column=0, padx=85)

def login():
    #Conexion a la base de datos y la creacion de la tabla usuario
    connection = sqlite3.connect('Analisis.db')
    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Usuario(Usuario INTEGER NOT NULL, Pass TEXT NOT NULL);")

    usuario = usuario_entry.get()
    password = contraseña_entry.get()

    c.execute('SELECT * FROM Usuario WHERE Usuario = ? AND Pass = ?', (usuario, password))
#Validacion de datos ingresados
    if c.fetchall():
        MessageBox.showinfo(title = "Login correcto", message = "Datos de ingreso correctos")
        c.close()
        ventana_login.destroy()

#Se crea la clase Articulos para crear las funciones a utilizar en la manipulacion de datos 
        class Articulos:

            def abrirBD(self):
                conexion=sqlite3.connect("Analisis.db")
                return conexion
#Funcion para poder ingresar un analisis 
            def dar_de_alta(self, datos):
                cone=self.abrirBD()
                cursor=cone.cursor()
                sql="INSERT INTO Analisis(Id_Analisis, Nombre, Precio, Descripcion, TipoAnalisis) VALUES (?,?,?,?,?)"
                cursor.execute(sql, datos)
                cone.commit()
                cone.close()
#Funcion para poder modificar algun campo del analisis registrado 
            def modificacion(self, datos):
                try:
                    cone=self.abrirBD()
                    cursor=cone.cursor()
                    sql="UPDATE Analisis SET Nombre = ?, Precio = ?, TipoAnalisis = ? WHERE Id_Analisis = ?"
                    cursor.execute(sql, datos)
                    cone.commit()
                    return cursor.rowcount
                except:
                    cone.close()
#Funcion para eliminar algun analisis registrado 
            def dar_de_baja(self, datos):
                try:
                    cone=self.abrirBD()
                    cursor=cone.cursor()
                    sql="DELETE FROM Analisis WHERE Id_Analisis = ?"
                    cursor.execute(sql, datos)
                    cone.commit()
                    return cursor.rowcount
                except:
                    cone.close()
#Funcion para consultar datos de algun analisis 
            def consultar(self, datos):
                try:
                    cone=self.abrirBD()
                    cursor=cone.cursor()
                    sql="SELECT Nombre, Precio, TipoAnalisis FROM Analisis WHERE Id_Analisis = ?"
                    cursor.execute(sql, datos)
                    return cursor.fetchall()
                finally:
                    cone.close()
#Funcion para ingresar algun cliente                     
            def alta_cliente(self, datos):
                cone=self.abrirBD()
                cursor=cone.cursor()
                sql="INSERT INTO Cliente(Id_Cliente, Precio, Fecha, Laboratorista) VALUES (?,?,?,?)"
                cursor.execute(sql, datos)
                cone.commit()
                cone.close()

        #---------------------------------------------------------------------------------------------------

        # Creación de la base de datos en SQLite3
        try:
            with sqlite3.connect("Analisis.db") as conn:
                c = conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS Analisis (Id_Analisis INTEGER PRIMARY KEY, Nombre TEXT NOT NULL, Precio INTEGER NOT NULL, Descripcion TEXT, TipoAnalisis TEXT);")
                c.execute("CREATE TABLE IF NOT EXISTS Cliente(Id_Cliente INTEGER PRIMARY KEY, Precio INTEGER NOT NULL, Fecha TEXT NOT NULL, Laboratorista TEXT);")
                print("Se pudieron crear las tablas \n")
        except Error as e:
            print(e)

        #---------------------------------------------------------------------------------------------------

        # Definir ventana
        ventana = Tk()
        articulo1 = Articulos()
        ventana.minsize(500, 500)
        ventana.title("Producto Integrador de Aprendizaje")
        ventana.resizable(0, 0)

        #---------------------------------------------------------------------------------------------------

        # Aviso para salir de la aplicación
        def salir():
            resultado = MessageBox.askquestion("Abandonar","¿Seguro que desea salir de la aplicacion?")
            if resultado == "yes":
                ventana.destroy()

        #---------------------------------------------------------------------------------------------------

        # Pantallas creadas para navegar
        def home():
            home_label.config(
                fg="gray",
                bg="pink",
                font=("Arial Narrow", 30),
                padx=210,
                pady=20
            )
            home_label.grid(row=0, column=0)

            # Pocisionamiento y Estilo de la ventana 
            home_frame.grid(row=1)
#Creacion de botones
            boton_agregar.grid(row=1, column=0, padx=15, pady=30, sticky=NW)
            boton_actualizacion.grid(row=1, column=1, padx=15, pady=30, sticky=NE)
            boton_borrar.grid(row=2, column=0, padx=15, pady=30, sticky=SW)
            boton_seleccionar.grid(row=2, column=1, padx=15, pady=30, sticky=SE)
            home_separator.grid(row=3, column=0)
            home_separator2.grid(row=3, column=1)
            boton_datosC.grid(row=4, column=0, padx=15, pady=30, sticky=SW)
            barra_status.grid(row=5, column=0, ipadx=8, ipady=8)
#Estilo de botones 
            boton_agregar.config(bg="#E6E6FA", fg="black", font=("Arial Narrow", 14, "bold"), bd=5,)
            boton_actualizacion.config(bg="#FFFACD", fg="black", font=("Arial Narrow", 14, "bold"), bd=5,)
            boton_borrar.config(bg="#E0FFFF", fg="black", font=("Arial Narrow", 14, "bold"), bd=5,)
            boton_seleccionar.config(bg="#FAFAD2", fg="black", font=("Arial Narrow", 14, "bold"), bd=5,)
            boton_datosC.config(bg="#FFB6C1", fg="black", font=("Arial Narrow", 14, "bold"), bd=5,)
            home_separator.config(font=("Arial Narrow", 14))
            home_separator2.config(font=("Arial Narrow", 14))
            barra_status.config(bg="black", fg="white", font=("Arial Narrow", 10, "bold"), borderwidth=5)

            # Ocultar otras ventanas
            agregar_label.grid_remove()
            agregar_frame.grid_remove()
            actualizacion_label.grid_remove()
            actualizacion_frame.grid_remove()
            borrar_label.grid_remove()
            borrar_frame.grid_remove()
            seleccionar_label.grid_remove()
            seleccionar_frame.grid_remove()
            cliente_label.grid_remove()
            cliente_frame.grid_remove()
            return True
#Funcion para la ventana de agregar 
        def agregar_A():
            agregar_label.config(
                fg="gray",
                bg="pink",
                font=("Arial Narrow", 30),
                padx=100,
                pady=20
            )
            agregar_label.grid(row=0, column=0, columnspan=10)

            # Pocisionamiento y Estilo de la ventana
            agregar_frame.grid(row=1)

            agregar_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            agregar_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            agregar_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            agregar_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

            agregar_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            agregar_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

            agregar_description_label.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
            agregar_description_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
            agregar_description_entry.config(width=30, height=5, font=("Arial", 12), padx=15, pady=15)

            agregar_category.place(x=50, y=250)

            guardar.grid(row=6, column=1, padx=5, pady=30, sticky=E)
            guardar.config(padx=15, pady=5, bg="#E6E6FA", fg="black", font=("Arial Narrow", 10, "bold"))

            # Ocultar otras ventanas 
            home_label.grid_remove()
            home_frame.grid_remove()
            actualizacion_label.grid_remove()
            actualizacion_frame.grid_remove()
            borrar_label.grid_remove()
            borrar_frame.grid_remove()
            seleccionar_label.grid_remove()
            seleccionar_frame.grid_remove()
            cliente_label.grid_remove()
            cliente_frame.grid_remove()
            return True
#Funcion para la ventana de actualizar
        def actualizacion_A():
            actualizacion_label.config(
                fg="gray",
                bg="pink",
                font=("Arial Narrow", 30),
                padx=150,
                pady=20
            )
            actualizacion_label.grid(row=0, column=0)

            # Pocisionamiento y Estilo de la ventana 
            actualizacion_frame.grid(row=1)

            actualizacion_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            actualizacion_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            actualizacion_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            actualizacion_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

            actualizacion_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            actualizacion_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

            actualizacion_description_label.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
            actualizacion_description_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
            actualizacion_description_entry.config(width=30, height=5, font=("Arial", 12), padx=15, pady=15)

            actualizacion_category.place(x=50, y=250)

            actualizar.grid(row=6, column=1, padx=5, pady=30, sticky=E)
            actualizar.config(padx=15, pady=5, bg="#FFFACD", fg="black", font=("Arial Narrow", 10, "bold"))

            # Ocultar otras ventanas 
            home_label.grid_remove()
            home_frame.grid_remove()
            agregar_label.grid_remove()
            agregar_frame.grid_remove()
            borrar_label.grid_remove()
            borrar_frame.grid_remove()
            seleccionar_label.grid_remove()
            seleccionar_frame.grid_remove()
            cliente_label.grid_remove()
            cliente_frame.grid_remove()
            return True
#Funcion para la ventana de eliminar 
        def borrar_A():
            borrar_label.config(
                fg="gray",
                bg="pink",
                font=("Arial Narrow", 30),
                padx=150,
                pady=20
            )
            borrar_label.grid(row=0, column=0)

            # Pocisionamiento y Estilo de la ventana 
            borrar_frame.grid(row=1)

            borrar_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            borrar_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            eliminar.grid(row=2, column=1, padx=5, pady=30, sticky=E)
            eliminar.config(padx=15, pady=5, bg="#E0FFFF", fg="black", font=("Arial Narrow", 10, "bold"))

            # Ocultar otras ventanas 
            home_label.grid_remove()
            home_frame.grid_remove()
            agregar_label.grid_remove()
            agregar_frame.grid_remove()
            actualizacion_label.grid_remove()
            actualizacion_frame.grid_remove()
            seleccionar_label.grid_remove()
            seleccionar_frame.grid_remove()
            seleccionar_frame.grid_remove()
            cliente_label.grid_remove()
            cliente_frame.grid_remove()
            return True
#Funcion para la ventana de consultar 
        def seleccionar_A():
            seleccionar_label.config(
                fg="gray",
                bg="pink",
                font=("Arial Narrow", 30),
                padx=150,
                pady=20
            )
            seleccionar_label.grid(row=0, column=0)

            # Pocisionamiento y Estilo de la ventana 
            seleccionar_frame.grid(row=1)

            seleccionar_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            seleccionar_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            seleccionar_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            seleccionar_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

            seleccionar_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            seleccionar_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

            seleccionar_description_label.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
            seleccionar_description_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
            seleccionar_description_entry.config(width=30, height=5, font=("Arial", 12), padx=15, pady=15)

            seleccionar_category.place(x=50, y=250)

            consultar.grid(row=6, column=1, padx=5, pady=30, sticky=E)
            consultar.config(padx=15, pady=5, bg="#FAFAD2", fg="black", font=("Arial Narrow", 10, "bold"))

            # Ocultar otras ventanas 
            home_label.grid_remove()
            home_frame.grid_remove()
            agregar_label.grid_remove()
            agregar_frame.grid_remove()
            actualizacion_label.grid_remove()
            actualizacion_frame.grid_remove()
            borrar_label.grid_remove()
            borrar_frame.grid_remove()
            cliente_label.grid_remove()
            cliente_frame.grid_remove()
            return True
#Funcion para la ventana de clientes 
        def datos_cliente():
            cliente_label.config(
                fg="gray",
                bg="pink",
                font=("Arial Narrow", 30),
                padx=150,
                pady=20
            )
            cliente_label.grid(row=0, column=0)
            
            # Pocisionamiento y Estilo de la ventana 
            cliente_frame.grid(row=1)
            
            cliente_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            cliente_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            cliente_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            cliente_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

            cliente_date_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            cliente_date_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

            cliente_description_label.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
            cliente_description_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
            cliente_description_entry.config(width=30, height=5, font=("Arial", 12), padx=15, pady=15)
            
            cliente.grid(row=6, column=1, padx=5, pady=30, sticky=E)
            cliente.config(padx=15, pady=5, bg="#FAFAD2", fg="black", font=("Arial Narrow", 10, "bold"))


            # Ocultar otras ventanas 
            home_label.grid_remove()
            home_frame.grid_remove()
            agregar_label.grid_remove()
            agregar_frame.grid_remove()
            actualizacion_label.grid_remove()
            actualizacion_frame.grid_remove()
            borrar_label.grid_remove()
            borrar_frame.grid_remove()
            seleccionar_label.grid_remove()
            seleccionar_frame.grid_remove()
            return True

       
        #---------------------------------------------------------------------------------------------------

        # Funciones para el manejo de productos que mandan llamar una funcion del archivo articulos.py
        #Funcion que agrega un analisis a la base de datos
        def agregar_analisis():
            try:
                datos = (id_analis.get(), nombre_analis.get(), precio_analis.get(), agregar_description_entry.get("1.0", "end-1c"), agregar_category.get())
                if id_analis.get() == "" or nombre_analis.get() == "" or precio_analis.get() == "" or agregar_description_entry.get("1.0", "end-1c") == "" or agregar_category.get() == "Categoria":
                    MessageBox.showwarning("Atencion", "Favor de proporcionar los datos completos.")
                else:
                    articulo1.dar_de_alta(datos)
                    MessageBox.showinfo("Información", "Los datos fueron cargados")
                    id_analis.set("")
                    nombre_analis.set("")
                    precio_analis.set("")
                    agregar_description_entry.delete("1.0", END)
                    agregar_category.set("Categoria")

                    app_status.set("¡Se ah agregado un analisis!")
            except:
                app_status.set("¡Ha ocurrido un error!")
                MessageBox.showerror("Error","Esta clave ya esta en uso")
#Funcion que actualizar un analisis a la base de datos
        def actualizar_analisis():
            datos = (nombre_analis.get(), precio_analis.get(), tipo_analis.get(), id_analis.get())
            if id_analis.get() == "" or nombre_analis.get() == "" or precio_analis.get() == "" or tipo_analis.get() == "":
                 MessageBox.showwarning("Atencion", "Favor de proporcionar los datos completos.")
            else:
                 datos = (nombre_analis.get(), precio_analis.get(), tipo_analis.get(), id_analis.get())
                 cantidad = articulo1.modificacion(datos)
                 if cantidad == 1:
                     app_status.set("¡Se acabas de modificar un analisis!")
                     MessageBox.showinfo("Modificacion correcta", "Se modificó el analisis correctamente")
                 else:
                     app_status.set("No existe ese analisis en la base de datos.")
                     MessageBox.showinfo( "Verificar los datos","No existe un analisis con el código proporcionado")
#Funcion que elimina un analisis a la base de datos
        def borrar_analisis():
            datos = (id_analis.get(), )
            cantidad = articulo1.dar_de_baja(datos)
            if cantidad == 1:
                app_status.set("Acabas de eliminar el analisis correctamente")
                MessageBox.showinfo("Informacion","Se eliminó el analisis correctamente")
            else:
                app_status.set("No existe ese analisis en la base de datos.")
                MessageBox.showinfo( "Aviso","No existe un analisis con el código")
#Funcion que consulta un analisis a la base de datos
        def consulta_analisis():
            datos = (id_analis.get(), )
            respuesta = articulo1.consultar(datos)
            if len(respuesta)>0:
                nombre_analis.set(respuesta[0][0])
                precio_analis.set(respuesta[0][1])
                tipo_analis.set(respuesta[0][2])
                app_status.set("Mostrando datos del producto...")
            else:
                nombre_analis.set("")
                precio_analis.set("")
                tipo_analis.set("Categoria")
                app_status.set("No existe ese analisis en la base de datos.")
                MessageBox.showinfo( "Error","No existe un analisis con el código")
#Funcion que obtiene los datos de un cliente                 
        def datos_clientes():
            try:
               datos = (id_cliente.get(), precio.get(), fecha.get(), laboratorista.get())
               if id_cliente.get() == "" or precio.get() == "" or fecha.get() == "" or laboratorista.get() == "":
                 MessageBox.showwarning("Atencion", "Favor de proporcionar los datos completos.")
                 articulo1.alta_cliente(datos)
                 MessageBox.showinfo("Información", "Los datos fueron cargados")
                 id_cliente.set("")
                 precio.set("")
                 fecha.set("")
                 laboratorista.set("")

                 app_status.set("¡Se ah agregado un cliente!")
            except:
                app_status.set("¡Ha ocurrido un error!")
                MessageBox.showerror("Se ah presentado un error favor de consultar el manual de usuario.")

        #---------------------------------------------------------------------------------------------------

        # Variables a utilizar
        analisis = {}
        id_analis = IntVar()
        nombre_analis = StringVar()
        precio_analis = StringVar()
        descripcion_analis = StringVar()
        tipo_analis = StringVar()
        id_cliente =IntVar()
        precio = StringVar()
        fecha = StringVar()
        laboratorista = StringVar()
        app_status = StringVar()

        #---------------------------------------------------------------------------------------------------

        # Definir campos de pantalla (Inicio)
        home_frame = Frame(ventana)

        home_label = Label(ventana, text="Menu de inicio")
        boton_agregar = Button(home_frame, text="Añadir analisis", command=agregar_A)
        boton_actualizacion = Button(home_frame, text="Actualizar analisis", command=actualizacion_A)
        boton_borrar = Button(home_frame, text="Eliminar analisis", command=borrar_A)
        boton_seleccionar = Button(home_frame, text="Consultar analisis", command=seleccionar_A)
        boton_datosC = Button(home_frame, text="Datos del cliente", command=datos_cliente)
        home_separator = Label(home_frame, text="-------------------------------------")
        home_separator2 = Label(home_frame, text="-------------------------------------")

        barra_status = Label(ventana, textvariable=app_status)
        app_status.set("Estado de la aplicación: -- Bienvenido --")

        #---------------------------------------------------------------------------------------------------

        # Definir campos de pantalla (Añadir)
        agregar_label = Label(ventana, text="Añadir analisis")

        # Campos del formulario (Añadir)
        agregar_frame = Frame(ventana)

        agregar_id_label = Label(agregar_frame, text="Clave del analisis: ")
        agregar_id_entry = Entry(agregar_frame, textvariable=id_analis)

        agregar_name_label = Label(agregar_frame, text="Nombre del analisis: ")
        agregar_name_entry = Entry(agregar_frame, textvariable=nombre_analis)

        agregar_price_label = Label(agregar_frame, text="Precio: ")
        agregar_price_entry = Entry(agregar_frame, textvariable=precio_analis)

        agregar_description_label = Label(agregar_frame, text="Descripcion del analisis: ")
        agregar_description_entry = Text(agregar_frame)

        agregar_category = ttk.Combobox(agregar_frame)
        agregar_category.set("Tipo de analisis")
        agregar_category['values'] = ('Urgente', 'Especial', 'Rutinario')
        agregar_category.current()

        guardar = Button(agregar_frame, text="Guardar", command=agregar_analisis)

        #---------------------------------------------------------------------------------------------------

        # Definir campos de pantalla (Actualizar)
        actualizacion_label = Label(ventana, text="Actualizar analisis")

        # Campos del formulario (Actualizar)
        actualizacion_frame = Frame(ventana)

        actualizacion_id_label = Label(actualizacion_frame, text="Clave del analisis: ")
        actualizacion_id_entry = Entry(actualizacion_frame, textvariable=id_analis)

        actualizacion_name_label = Label(actualizacion_frame, text="Nombre del analisis: ")
        actualizacion_name_entry = Entry(actualizacion_frame, textvariable=nombre_analis)

        actualizacion_price_label = Label(actualizacion_frame, text="Precio: ")
        actualizacion_price_entry = Entry(actualizacion_frame, textvariable=precio_analis)

        actualizacion_description_label = Label(actualizacion_frame, text="Descripción del analisis: ")
        actualizacion_description_entry = Text(actualizacion_frame)

        actualizacion_category = ttk.Combobox(actualizacion_frame, textvariable=tipo_analis)
        actualizacion_category.set("Tipo de analisis")
        actualizacion_category['values'] = ('Urgente', 'Especial', 'Rutinario')
        actualizacion_category.current()

        actualizar = Button(actualizacion_frame, text="Actualizar", command=actualizar_analisis)

        #---------------------------------------------------------------------------------------------------

        # Definir campos de pantalla (Eliminar)
        borrar_label = Label(ventana, text="Eliminar analisis")

        # Campos del formulario (Eliminar)
        borrar_frame = Frame(ventana)

        borrar_id_label = Label(borrar_frame, text="Clave del analisis: ")
        borrar_id_entry = Entry(borrar_frame, textvariable=id_analis)

        eliminar = Button(borrar_frame, text="Eliminar", command=borrar_analisis)

        #---------------------------------------------------------------------------------------------------

        # Definir campos de pantalla (Consultar)
        seleccionar_label = Label(ventana, text="Consultar analisis")

        # Campos del formulario (Consultar)
        seleccionar_frame = Frame(ventana)

        seleccionar_id_label = Label(seleccionar_frame, text="Clave del analisis: ")
        seleccionar_id_entry = Entry(seleccionar_frame, textvariable=id_analis)

        seleccionar_name_label = Label(seleccionar_frame, text="Nombre del analisis: ")
        seleccionar_name_entry = Entry(seleccionar_frame, textvariable=nombre_analis)

        seleccionar_price_label = Label(seleccionar_frame, text="Precio: ")
        seleccionar_price_entry = Entry(seleccionar_frame, textvariable=precio_analis)

        seleccionar_description_label = Label(seleccionar_frame, text="Descripción: ")
        seleccionar_description_entry = Text(seleccionar_frame)

        seleccionar_category = ttk.Combobox(seleccionar_frame, textvariable=tipo_analis)
        seleccionar_category.set("Tipo de analisis")
        seleccionar_category['values'] = ('Urgente', 'Especial', 'Rutinario')
        seleccionar_category.current()

        consultar = Button(seleccionar_frame, text="Consultar", command=consulta_analisis)

        #---------------------------------------------------------------------------------------------------
        
        cliente_label = Label(ventana, text="Clientes")
        
        # Definir campos de pantalla (Clientes)
        cliente_frame = Frame(ventana)

        cliente_id_label = Label(cliente_frame, text="Clave del cliente: ")
        cliente_id_entry = Entry(cliente_frame, textvariable=id_cliente)

        cliente_price_label = Label(cliente_frame, text="Precio: ")
        cliente_price_entry = Entry(cliente_frame, textvariable=precio)

        cliente_date_label = Label(cliente_frame, text="Fecha en la que se solicita: ")
        cliente_date_entry = Entry(cliente_frame, textvariable=fecha)

        cliente_description_label = Label(cliente_frame, text="Laboratorista que realiza: ")
        cliente_description_entry = Text(cliente_frame)
        
        cliente = Button(cliente_frame, text="Datos del Cliente", command=datos_cliente)


        #---------------------------------------------------------------------------------------------------

        # Cargar la pantalla Inicio
        home()

        # Menú superior
        menu_superior = Menu(ventana)
        menu_superior.add_command(label="Inicio", command=home)
        menu_superior.add_command(label="Añadir", command=agregar_A)
        menu_superior.add_command(label="Actualizar", command=actualizacion_A)
        menu_superior.add_command(label="Eliminar", command=borrar_A)
        menu_superior.add_command(label="Consultar", command=seleccionar_A)
        menu_superior.add_command(label="Datos del Clientes", command=datos_cliente)
        menu_superior.add_command(label="Salir", command=lambda: salir())

        # Cargar Menú
        ventana.config(menu=menu_superior)

        # Cargar ventana
        ventana.mainloop()
        
    else:
        MessageBox.showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")
#Boton para el login
Logear = Button(ventana_login, text="Iniciar Sesión", command = login)
Logear.grid(row=5, column=0, pady=20)
Logear.config(padx=15, pady=5, bg="#33B5E5", fg="white", font=("Arial", 10, "bold"))

#Cargar ventana del login
ventana_login.mainloop()



