# Contenido del archivo material.py 
class Material:

    """Clase base para materiales de la biblioteca."""  
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio 

# getter y setter para el atributo privado precio.

    def get_precio(self):

        return self.__precio

# setter con validacion para precio.

    def set_precio(self, nuevo_precio):

        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser un valor positivo.")

# definir metodo descripcion.   

    def descripcion(self):

        return f"Material: '{self.titulo}', Autor: {self.autor}"