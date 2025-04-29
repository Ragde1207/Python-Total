'''
Archivo para probar unittest usando el modulo ModulaA para la prueba
'''
import unittest
import ModuloA

#(unittest.TestCase) permite usar los metodos TestCase para su uso en la clase
class Prueba(unittest.TestCase):

    def test_funcion(self):

        palabra = "buen día"
        resultado = ModuloA.todomayusculas(palabra)

        #.assertEqual verifica que el resultado almacenado sea igual a lo especificado
        self.assertEqual(resultado, "Buen Día")

if __name__ == "__main__":
    unittest.main()

