import unittest
import json
import os
from libreria import Libreria

class TestLibreria(unittest.TestCase):
    
    def setUp(self):
        """Configura el entorno de prueba creando una instancia de la clase Libreria."""
        self.libreria = Libreria()
        self.libro = {'titulo': 'El Quijote', 'autor': 'Miguel de Cervantes', 'genero': 'Novela', 'anio': 1605}

    def test_anadir_libro(self):
        """Prueba el método anadir_libro."""
        respuesta = self.libreria.anadir_libro(**self.libro)
        self.assertEqual(respuesta, "Libro añadido")
        self.assertIn(self.libro, self.libreria.libros)

    def test_buscar_libro(self):
        """Prueba el método buscar_libro."""
        self.libreria.anadir_libro(**self.libro)
        resultado = self.libreria.buscar_libro('El Quijote')
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0], self.libro)

    def test_buscar_por_autor(self):
        """Prueba el método buscar_por_autor."""
        self.libreria.anadir_libro(**self.libro)
        resultado = self.libreria.buscar_por_autor('Cervantes')
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0], self.libro)

    def test_eliminar_libro(self):
        """Prueba el método eliminar_libro."""
        self.libreria.anadir_libro(**self.libro)
        respuesta = self.libreria.eliminar_libro('El Quijote')
        self.assertEqual(respuesta, "Libro eliminado")
        self.assertNotIn(self.libro, self.libreria.libros)
        respuesta_no_encontrado = self.libreria.eliminar_libro('El Quijote')
        self.assertEqual(respuesta_no_encontrado, "Libro no encontrado")

    def test_guardar_libros(self):
        """Prueba el método guardar_libros."""
        archivo = 'libros_test.json'
        self.libreria.anadir_libro(**self.libro)
        respuesta = self.libreria.guardar_libros(archivo)
        self.assertEqual(respuesta, "Libros guardados")
        with open(archivo, 'r') as f:
            libros = json.load(f)
        self.assertEqual(libros, [self.libro])
        os.remove(archivo)

    def test_cargar_libros(self):
        """Prueba el método cargar_libros."""
        archivo = 'libros_test.json'
        with open(archivo, 'w') as f:
            json.dump([self.libro], f)
        respuesta = self.libreria.cargar_libros(archivo)
        self.assertEqual(respuesta, "Libros cargados")
        self.assertEqual(self.libreria.libros, [self.libro])
        os.remove(archivo)
        respuesta_no_encontrado = self.libreria.cargar_libros('no_existe.json')
        self.assertEqual(respuesta_no_encontrado, "Archivo no encontrado")

if __name__ == '__main__':
    unittest.main()
