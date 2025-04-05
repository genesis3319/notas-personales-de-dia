# Escritura de Archivo de Texto
# Creamos un nuevo archivo llamado my_notes.txt y escribimos notas personales en él.

# Abrimos el archivo en modo escritura ('w'), esto creará el archivo si no existe.
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo.
    file.write("Nota 1: Recuerda comprar el pan para el desayuno.\n")
    file.write("Nota 2: Terminar el proyecto de Matemáticas.\n")
    file.write("Nota 3: Llamar a la aduela.\n")

# Lectura de Archivo de Texto
# Ahora abrimos el archivo my_notes.txt en modo lectura ('r').
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea.
    for line in file:
        # Mostramos cada línea leída en la consola.
        print(line.strip())  # strip() se usa para eliminar el salto de línea al final.

# No es necesario cerrar el archivo manualmente cuando usamos 'with',
# ya que se cierra automáticamente al salir del bloque.