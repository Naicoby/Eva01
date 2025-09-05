# Contenido del archivo biblioteca.py

class Biblioteca:
    """Clase para gestionar el catalogo de la biblioteca."""
    def __init__(self):
        self.catalogo = []

    def agregar_material(self, material):
        """Metodo para agregar un material a la lista."""
        self.catalogo.append(material)

# definir metodo mostrar_catalogo.

    def mostrar_catalogo(self):
        """Metodo para mostrar todos los materiales en el catalogo."""
        print("--- Catalogo de Materiales ---")
        valor_total = 0
        for material in self.catalogo:
            # Polimorfismo en accion: cada objeto llama a su propio metodo descripcion.
            print(f"- {material.descripcion()}")
            print(f"  Precio: ${material.get_precio():,.2f}")
            valor_total += material.get_precio()

#mostrar valor total del catalogo.

        print(f"\nValor total del catalogo: ${valor_total:,.2f}")
        print("-------------------------------")







