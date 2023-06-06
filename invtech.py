from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%d-%m-%Y %I:%M:%p")

root=Tk()
# set the title of the main window
root.title("Empresa")
# windows + size
root.geometry("1000x900")
#Almacena el menu en el root
barramenu=Menu(root) 
# Main windows + size
root.config(menu=barramenu, bg="#5d5c5a", width=300, height=300) 
# Windows
miframe=Frame(root, bg="#5d5c5a")
miframe.pack(side="top", anchor="w", padx=100)
# Sub windows for buttons
miframe2=Frame(root, bg="#5d5c5a")
miframe2.pack(side="top", anchor="w")

miframe3=Frame(root, bg="#5d5c5a")
miframe3.pack(side="right")


def show_info():
	messagebox.showinfo("Acerca de...", "Programa creado por Alfred Luis Frias Santiago.")

def show_license():
	messagebox.showinfo("Licencia", "Producto bajo licencia python.")

def close_app():
	value_close=messagebox.askokcancel("Exit", "Deseas salir?")

	if value_close==True:
		root.destroy()


last_saved_id = None
# Stores the data entered in the text boxes
customer_date=StringVar()
customerno=StringVar()
customername=StringVar()
customercedula=StringVar()
customernumberphone=StringVar()
customerdevice=StringVar()
customermodel=StringVar()
customerimei=StringVar()
customercolor=StringVar()
customerrepair=StringVar()
customerprice=StringVar()
# Box comment
boxcomment=Text(miframe, bg="#d0e3e3", width=16, height=5)
boxcomment.grid(row=10, column=1, padx=5, pady=5)

# Print box
text_print = f"""Negocio
Fecha:
Calle 16 Agosto #139
Teléfono: 000 000 000
NÚMERO DE RECIBO NO: 

------------------------------------
Cliente:
Cédula:
Teléfono:
Dispositivo:
Modelo:
Imei:
Color:
Reparación:
Precio estimado:
Detalles:
-----------------------------------

Recibido por:_____________

Firma cliente:____________"""

text_box = Text(root, bg="#d0e3e3", width=50, height=30)
text_box.insert(END, text_print)
text_box.pack()


# Clean the print box
def update_text_clean():
    
    text_print = f"""Negocio
    Fecha: 
    Calle 16 Agosto #139
    Teléfono: 000 000 000
    NÚMERO DE RECIBO NO:
    
    ------------------------------------
    Cliente: {customername.get()}
    Cédula: {customercedula.get()}
    Teléfono: {customernumberphone.get()}
    Dispositivo: {customerdevice.get()}
    Modelo: {customermodel.get()}
    Imei: {customerimei.get()}
    Color: {customercolor.get()}
    Reparación: {customerrepair.get()}
    Precio estimado: {customerprice.get()}
    Detalles:
    -----------------------------------
    
    Recibido por:_____________
    
    Firma cliente:____________"""
    
	# Remove leading and trailing spaces from each line
    lines = text_print.split('\n')
    lines = [line.strip() for line in lines]
    text_print = '\n'.join(lines)
    
    text_box.delete(1.0, END)
    text_box.insert(END, text_print)


# Refreshes the screen with the saved customer data
def update_text_current(customerno):
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y %I:%M:%p")
    text_print = f"""Negocio
    Fecha: {current_time}
    Calle 16 Agosto #139
    Teléfono: 000 000 000
    NÚMERO DE RECIBO NO: {last_saved_id}
    
    ------------------------------------
    Cliente: {customername.get()}
    Cédula: {customercedula.get()}
    Teléfono: {customernumberphone.get()}
    Dispositivo: {customerdevice.get()}
    Modelo: {customermodel.get()}
    Imei: {customerimei.get()}
    Color: {customercolor.get()}
    Reparación: {customerrepair.get()}
    Precio estimado: {customerprice.get()}
    Detalles:
    {boxcomment.get(1.0, END)}
    -----------------------------------
    
    Recibido por:_____________
    
    Firma cliente:____________"""
    
	# Remove leading and trailing spaces from each line
    lines = text_print.split('\n')
    lines = [line.strip() for line in lines]
    text_print = '\n'.join(lines)
    
    text_box.delete(1.0, END)
    text_box.insert(END, text_print)


# Update
def update_text(customerno):
    text_print = f"""Negocio
    Fecha: {customer_date.get()}
    Calle 16 Agosto #139
    Teléfono: 000 000 000
    NÚMERO DE RECIBO NO: {customerno.get()}
    
    ------------------------------------
    Cliente: {customername.get()}
    Cédula: {customercedula.get()}
    Teléfono: {customernumberphone.get()}
    Dispositivo: {customerdevice.get()}
    Modelo: {customermodel.get()}
    Imei: {customerimei.get()}
    Color: {customercolor.get()}
    Reparación: {customerrepair.get()}
    Precio estimado: {customerprice.get()}
    Detalles:
    {boxcomment.get(1.0, END)}
    -----------------------------------
    
    Recibido por:_____________
    
    Firma cliente:____________"""
    
	# Remove leading and trailing spaces from each line
    lines = text_print.split('\n')
    lines = [line.strip() for line in lines]
    text_print = '\n'.join(lines)
    
    text_box.delete(1.0, END)
    text_box.insert(END, text_print)


# Obtains the data from the database to display in
def update_text_print():
    text_print = f"""Negocio
    Fecha: {customer_date.get()}
    Calle 16 Agosto #139
    Teléfono: 000 000 000
    NÚMERO DE RECIBO NO: {customerno.get()}
    
    ------------------------------------
    Cliente: {customername.get()}
    Cédula: {customercedula.get()}
    Teléfono: {customernumberphone.get()}
    Dispositivo: {customerdevice.get()}
    Modelo: {customermodel.get()}
    Imei: {customerimei.get()}
    Color: {customercolor.get()}
    Reparación: {customerrepair.get()}
    Precio estimado: {customerprice.get()}
    Detalles:
    {boxcomment.get(1.0, END)}
    -----------------------------------
    
    Recibido por:_____________
    
    Firma cliente:____________"""
    
	# Remove leading and trailing spaces from each line
    lines = text_print.split('\n')
    lines = [line.strip() for line in lines]
    text_print = '\n'.join(lines)
    
    text_box.delete(1.0, END)
    text_box.insert(END, text_print)



DB_NAME = "datosusuario.db"
def create_database():
    # Use with statement to handle database connection
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        try:
            # Create table with primary key and autoincrement
            cursor.execute('''
			CREATE TABLE DATOSUSUARIO (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DATE TEXT,
			NOMBRE TEXT,
			CEDULA TEXT,
			TELEFONO TEXT,
			DISPOSITIVO TEXT,
			MODELO TEXT,
			IMEI TEXT,
			COLOR TEXT,
			REPARACION TEXT,
			PRECIO TEXT,
			COMENTARIOS TEXT)
			''')
            # Commit changes to database
            conn.commit()
            # Show success message
            messagebox.showinfo("Aviso", "Base de datos creada con éxito.")
        
        except :
            messagebox.showwarning("¡Atención!", "La base de datos ya existe.")



def insert_data(customername, customercedula, customernumberphone, customerdevice, customermodel, customerimei, customercolor, customerrepair, customerprice, boxcomment):
    global last_saved_id
    # Date of created register
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y %I:%M:%p")
    
    # Connecto to the database
    with sqlite3.connect("datosusuario.db") as conn:
        cursor = conn.cursor()
	
        # Create the table and insert the data of the new record
        try:
            cursor.execute("""
                INSERT INTO DATOSUSUARIO 
                (DATE, NOMBRE, CEDULA, TELEFONO, DISPOSITIVO, MODELO, IMEI, COLOR, REPARACION, PRECIO, COMENTARIOS)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (current_time, customername, customercedula, customernumberphone, customerdevice, customermodel, customerimei, customercolor, customerrepair, customerprice, boxcomment))
            conn.commit()
            last_saved_id = cursor.lastrowid
	    
            messagebox.showinfo("Crear", "Registro creado")
            
	    
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el registro: {e}")


def create_reg():
    confirm_registration = messagebox.askyesno("Confirmar", "¿Crear registro?")
    
    # when "yes" is pressed, it collects the data from the text boxes and sends it to the "insert_data" function to create the record.
    if confirm_registration:
        insert_data(customername.get(), customercedula.get(), customernumberphone.get(), customerdevice.get(), customermodel.get(), customerimei.get(), customercolor.get(), customerrepair.get(), customerprice.get(), boxcomment.get("1.0", END))
	
    else:
        return
    # Refreshes the screen with the saved customer data
    update_text_current(customerno)



def read_reg():
    conexion_bd = sqlite3.connect("datosusuario.db")
    cursor_bd = conexion_bd.cursor()
    
    try:
        
        cursor_bd.execute("SELECT * FROM DATOSUSUARIO WHERE ID=?", (customerno.get(),))

        usuario = cursor_bd.fetchone()

        if usuario is not None:
            customerno.set(usuario[0])
            customer_date.set(usuario[1])
            customername.set(usuario[2])
            customercedula.set(usuario[3])
            customernumberphone.set(usuario[4])
            customerdevice.set(usuario[5])
            customermodel.set(usuario[6])
            customerimei.set(usuario[7])
            customercolor.set(usuario[8])
            customerrepair.set(usuario[9])
            customerprice.set(usuario[10])
            boxcomment.delete(1.0, END)  # Limpia el cuadro de comentarios antes de insertar el texto
            boxcomment.insert(1.0, usuario[11])
        else:
            messagebox.showwarning("¡Atención!", "No se encontró el registro.")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el registro: {e}")

    conexion_bd.close()
    
    update_text_print()


def update_reg():
    global last_saved_id
    update_confirmation = messagebox.askyesno("Actualizar", "¿Actualizar registro?")

    if update_confirmation:
        datos = (customername.get(),
                 customercedula.get(),
                 customernumberphone.get(),
                 customerdevice.get(),
                 customermodel.get(),
                 customerimei.get(),
                 customercolor.get(),
                 customerrepair.get(),
                 customerprice.get(),
                 boxcomment.get("1.0", END))

        with sqlite3.connect("datosusuario.db") as conn:
            cursor = conn.cursor()

            try:
                cursor.execute("""
                    UPDATE DATOSUSUARIO SET 
                        NOMBRE=?,
                        CEDULA=?,
                        TELEFONO=?,
                        DISPOSITIVO=?,
                        MODELO=?,
                        IMEI=?,
                        COLOR=?,
                        REPARACION=?,
                        PRECIO=?,
                        COMENTARIOS=?
                    WHERE ID=?
                """, datos + (customerno.get(),))

                rows_affected = cursor.rowcount
                last_saved_id = cursor.lastrowid

                if rows_affected > 0:
                    messagebox.showinfo("Crear", "Registro actualizado con éxito")
                else:
                    messagebox.showerror("Error", "No se encontró el registro.")

            except Exception as e:
                messagebox.showerror("Error", f"No se pudo actualizar el registro: {e}")
    else:
        return
    
    update_text(customerno)



def delete_reg():

    delete_question = messagebox.askyesno("Confirmación", "¿Está seguro que desea borrar el registro?")

    if delete_question:
        try:
            with sqlite3.connect("datosusuario.db") as conexion_bd:

                cursor_bd = conexion_bd.cursor()
                cursor_bd.execute("DELETE FROM DATOSUSUARIO WHERE ID=?", (customerno.get(),))

            messagebox.showinfo("BBDD", "Registro borrado con exito")

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Ocurrió un error al borrar el registro: {error}")
    else:
        return


def clean_boxes():
     customerno.set("")
     customername.set("")
     customercedula.set("")
     customernumberphone.set("")
     customerdevice.set("")
     customermodel.set("")
     customerimei.set("")
     customercolor.set("")
     customerrepair.set("")
     customerprice.set("")
     customer_date.set("")
     boxcomment.delete(1.0, END)
     # Clean the print box
     update_text_clean()
     

# Navigation bar buttons
archivomenu=Menu(barramenu, tearoff=0) 
archivomenu.add_command(label="Open")
archivomenu.add_command(label="Create database", command=create_database)
archivomenu.add_command(label="Save")

# line between the buttons
archivomenu.add_separator()

archivomenu.add_command(label="Close")
archivomenu.add_command(label="Exit", command=close_app)

archivotools=Menu(barramenu, tearoff=0) 
archivotools.add_command(label="Borrar", command=delete_reg)

# Button help
archivoayuda=Menu(barramenu, tearoff=0) 
archivoayuda.add_command(label="License", command=show_license)
archivoayuda.add_command(label="About", command=show_info)

# Menu button tex
barramenu.add_cascade(label="Archivo", menu=archivomenu)
barramenu.add_cascade(label="Herramientas", menu=archivotools)
barramenu.add_cascade(label="Ayuda", menu=archivoayuda)


# Boxes
boxno=Entry(miframe, textvariable=customerno)
boxno.grid(row=0, column=1, padx=5, pady=5) 

boxname =Entry(miframe, bg="#d0e3e3", textvariable=customername)
boxname.grid(row=1, column=1, padx=5, pady=5)

boxcedula=Entry(miframe, bg="#d0e3e3", textvariable=customercedula)
boxcedula.grid(row=2, column=1, padx=5, pady=5)

box_number_phone=Entry(miframe, bg="#d0e3e3", textvariable=customernumberphone)
box_number_phone.grid(row=3, column=1, padx=5, pady=5)

boxdevice=Entry(miframe, bg="#d0e3e3", textvariable=customerdevice)
boxdevice.grid(row=4, column=1, padx=5, pady=5) 

boxmodel=Entry(miframe, bg="#d0e3e3", textvariable=customermodel)
boxmodel.grid(row=5, column=1, padx=5, pady=5)

boximei=Entry(miframe, bg="#d0e3e3", textvariable=customerimei)
boximei.grid(row=6, column=1, padx=5, pady=5)

boxcolor=Entry(miframe, bg="#d0e3e3",  textvariable=customercolor)
boxcolor.grid(row=7, column=1, padx=5, pady=5) 

boxrepair=Entry(miframe, bg="#d0e3e3", textvariable=customerrepair)
boxrepair.grid(row=8, column=1, padx=5, pady=5)

boxprice=Entry(miframe, bg="#d0e3e3", textvariable=customerprice)
boxprice.grid(row=9, column=1, padx=5, pady=5)

# Box comment and size
boxcomment=Text(miframe, bg="#d0e3e3", width=16, height=5)
# Box location
#boxcomment.grid(row=10, column=1, padx=5, pady=5)
boxcomment.grid(row=10, column=1, padx=5, pady=5, sticky=W)

boxdate=Entry(miframe, bg="#d0e3e3", textvariable=customer_date)
boxdate.grid(row=11, column=1, padx=5, pady=5)

# Scroll bar
scrollVert=Scrollbar(miframe, command=boxcomment.yview)
# Scroll bar location
scrollVert.grid(row=10, column=2, sticky="nsew")
# makes the bar move
boxcomment.config(yscrollcommand=scrollVert.set) 




# Text boxes
receipt_number=Label(miframe, text="No:")
receipt_number.grid(row=0, column=0, sticky="e", padx=5, pady=5)

# crea un objeto Label para mostrar la fecha
date_label = Label(miframe, text="Fecha entrada")
date_label.grid(row=11, column=0, padx=5, pady=5)


customer_name=Label(miframe, text="Nombre:")
customer_name.grid(row=1, column=0, sticky="e", padx=5, pady=5)

cedula=Label(miframe, text="Cédula:")
cedula.grid(row=2, column=0, sticky="e", padx=5, pady=5)

number_phone=Label(miframe, text="Número de teléfono:")
number_phone.grid(row=3, column=0, sticky="e", padx=5, pady=5)

device=Label(miframe, text="Dispositivo:")
device.grid(row=4, column=0, sticky="e", padx=5, pady=5) 

device_model=Label(miframe, text="Modelo:")
device_model.grid(row=5, column=0, sticky="e", padx=5, pady=5)

device_imei=Label(miframe, text="Imei:")
device_imei.grid(row=6, column=0, sticky="e", padx=5, pady=5)

device_color=Label(miframe, text="Color:")
device_color.grid(row=7, column=0, sticky="e", padx=5, pady=5)

repair=Label(miframe, text="Reparación:")
repair.grid(row=8, column=0, sticky="e", padx=5, pady=5)

price=Label(miframe, text="Precio estimado:")
price.grid(row=9, column=0, sticky="e", padx=5, pady=5)

comment=Label(miframe, text="Comentarios:")
comment.grid(row=10, column=0, sticky="e", padx=5, pady=5)


# Bottom buttons
create=Button(miframe2, text="Guardar", command=create_reg, bg="#c7ffd6")
create.grid(row=9, column=0, pady=5, padx=5)

read=Button(miframe2, text="Buscar", command=read_reg)
read.grid(row=9, column=1, pady=5, padx=5)

update=Button(miframe2, text="Actualizar", command=update_reg)
update.grid(row=9, column=2, pady=5, padx=5)

clean=Button(miframe2, text="Limpiar", command=clean_boxes)
clean.grid(row=9, column=3, pady=5, padx=5)

#delete=Button(miframe2, text="Borrar", command=delete_reg, bg="#ffc7c7")
#delete.grid(row=9, column=4, pady=5, padx=5)

print_button = Button(miframe2, text="Imprimir")
print_button.grid(row=9, column=4, pady=5, padx=5)


root.mainloop()