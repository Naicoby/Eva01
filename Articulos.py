from  material import Material

class Libro(Material):

    def __init__(self, titulo, autor, precio, paginas):
        super().__init__(titulo, autor, precio)
        self.paginas = paginas

    def descripcion(self):

        # Aplicacion de polimorfismo.                                                   
        return f"Libro: '{self.titulo}', Autor: {self.autor}, Paginas: {self.paginas}"

#  Crear clase Revista que herede de Material con atributo adicional edicion.
class Revista(Material):
    def __init__(self, titulo, autor, precio, edicion):
        super().__init__(titulo, autor, precio)
        self.edicion = edicion

# implementar metodo descripcion.

    def descripcion(self):
        return f"Revista: '{self.titulo}', Autor: {self.autor}, Edicion: {self.edicion}"

# Crear clase Periodico que herede de Material con atributo adicional fecha_publicacion.

class Periodico(Material):
    def __init__(self, titulo, autor, precio, fecha_publicacion):
        super().__init__(titulo, autor, precio)
        self.fecha_publicacion = fecha_publicacion

# implementar metodo descripcion.

    def descripcion(self):
        return f"Periodico: '{self.titulo}', Autor: {self.autor}, Fecha: {self.fecha_publicacion}"