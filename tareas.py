import mysql.connector
import os
# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="base_tareas"
)
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute("CREATE TABLE IF NOT EXISTS tareas (id INT AUTO_INCREMENT PRIMARY KEY, tarea VARCHAR(255), completada BOOLEAN)")

def agregar_tarea(tarea):
    sql = "INSERT INTO tareas (tarea, completada) VALUES (%s, %s)"
    val = (tarea, False)
    cursor.execute(sql, val)
    conexion.commit()
    print("Tarea agregada correctamente.")

def mostrar_tareas():
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    print("Tareas:")
    for tarea in tareas:
        tarea_id, descripcion, completada = tarea
        estado = "Completada" if completada else "Pendiente"
        print(f"{tarea_id}. {descripcion} - {estado}")

def tachar_tarea(tarea_id):
    sql = "UPDATE tareas SET completada = TRUE WHERE id = %s"
    val = (tarea_id,)
    cursor.execute(sql, val)
    conexion.commit()
    print("Tarea marcada como completada.")

def eliminar_tarea(tarea_id):
    sql = "DELETE FROM tareas WHERE id = %s"
    val = (tarea_id,)
    cursor.execute(sql, val)
    conexion.commit()
    print("Tarea eliminada.")

while True:
    print("GESTOR DE TAREAS:\n_________________")
    print("1- Agregar tarea.\n2- Mostrar tareas.\n3- Marcar tarea realizada.\n4- Eliminar tarea.")
    tarea = int(input("ESCOGE UNA OPCIÓN: "))
    if tarea == 1:
        os.system("cls")
        añadir = input("Escribe la nueva tarea: ")
        agregar_tarea(añadir)
    elif tarea == 2:
        os.system("cls")
        mostrar_tareas()
        print()
    elif tarea == 3:
        os.system("cls")
        tachar = int(input("Selecciona el número de tarea que quiere marcar:"))
        tachar_tarea(tachar)
    elif tarea == 4:
        os.system("cls")
        drop = int(input("Elimina la tarea (escoge su número): "))
        eliminar_tarea(drop)
    else:
        exit()

# Cerrar la conexión
conexion.close()
