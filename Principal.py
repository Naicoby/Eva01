# Contenido del archivo principal.py

from Biblioteca import Biblioteca
from Articulos import Libro, Revista, Periodico

# Acciones del programa principal:
# 1. Crear una instancia de la biblioteca.
biblioteca = Biblioteca()

# 2. Instanciar al menos un libro, una revista y un periodico.
libro = Libro("El Poder ", "Erick.Tapia", 49990, 450)
revista = Revista("", "Varios Autores", 9990, 190)
periodico = Periodico("La Cuarta", "Equipo Periodistico", 1490, "04/09/2025")

# 3. Usar el setter para modificar el precio.
print(f"Precio original del libro: ${libro.get_precio():,.2f}")
libro.set_precio(14000)
print(f"Nuevo precio del libro: ${libro.get_precio():,.2f}\n")

# 4. Agregar los materiales a la biblio
biblioteca.agregar_material(libro)
biblioteca.agregar_material(revista)
biblioteca.agregar_material(periodico)

# 5. Mostrar el catalogo.
biblioteca.mostrar_catalogo()