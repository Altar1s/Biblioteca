import json

class Libreria:
    """Clase libreria."""
    
    def __init__(self):
        """Inicializa la librería con una lista vacía de libros."""
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añadir un libro a la librería.
        
        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            genero (str): El género del libro.
            anio (int): El año de publicación del libro.
        
        Returns:
            str: Mensaje indicando que el libro ha sido añadido.
        """
        self.libros.append({
            'titulo': titulo, 
            'autor': autor, 
            'genero': genero, 
            'anio': anio
        })
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Buscar un libro por su título.
        
        Args:
            titulo (str): El título del libro a buscar.
        
        Returns:
            list: Lista de libros que coinciden con el titulo.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Buscar libros por su autor.
        
        Args:
            autor (str): El autor de los libros a buscar.
        
        Returns:
            list: Lista de libros del autor .
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """
        Eliminar un libro por su título.
        
        Args:
            titulo (str): El título del libro a eliminar.
        
        Returns:
            str: Mensaje indicando si el libro ha sido eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        if len(self.libros) < original_count:
            return "Libro eliminado"
        return "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guardar la lista de libros en un archivo JSON.
        
        Args:
            archivo (str): El nombre del archivo donde se guardan los libros.
        
        Returns:
            str: Mensaje indicando que los libros han sido guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Cargar la lista de libros desde un archivo JSON.
        
        Args:
            archivo (str): El nombre del archivo.
        
        Returns:
            str: Mensaje indicando si los libros han sido cargados o si el archivo no se encontró.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"

# Crear instancia de la librería
mi_libreria = Libreria()

# Añadir algunos libros
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.anadir_libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela", 1985)
mi_libreria.anadir_libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", 1605)
mi_libreria.anadir_libro("1984", "George Orwell", "Distopía", 1949)
mi_libreria.anadir_libro("Fahrenheit 451", "Ray Bradbury", "Distopía", 1953)

# Guardar libros en un archivo JSON
mi_libreria.guardar_libros('libreria.json')

# Cargar libros desde el archivo JSON
print(mi_libreria.cargar_libros('libreria.json'))

# Buscar libros por título
print("Buscar por título 'Cien años de soledad':")
print(mi_libreria.buscar_libro("Cien años de soledad"))

print("Buscar por título 'Don Quijote de la Mancha':")
print(mi_libreria.buscar_libro("Don Quijote de la Mancha"))

print("Buscar por título 'Libro no existente':")
print(mi_libreria.buscar_libro("Libro no existente"))

# Buscar libros por autor
print("Buscar por autor 'Gabriel García Márquez':")
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))

print("Buscar por autor 'George Orwell':")
print(mi_libreria.buscar_por_autor("George Orwell"))

print("Buscar por autor 'Autor no existente':")
print(mi_libreria.buscar_por_autor("Autor no existente"))

# Eliminar libros por título
print("Eliminar libro '1984':")
print(mi_libreria.eliminar_libro("1984"))

print("Eliminar libro 'Libro no existente':")
print(mi_libreria.eliminar_libro("Libro no existente"))

# Verificar que el libro se ha eliminado
print("Buscar por título '1984' después de eliminación:")
print(mi_libreria.buscar_libro("1984"))

# Guardar la lista de libros actualizada
mi_libreria.guardar_libros('libreria_actualizada.json')
print(mi_libreria.libros)