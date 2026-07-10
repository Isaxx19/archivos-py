import unittest
from validar_ip import es_ip_valida

class TestValidarIP(unittest.TestCase):

    def test_ip_valida(self):
        # Caso 1: Una IP completamente valida
        self.assertTrue(es_ip_valida("192.168.1.1"))

    def test_octeto_mayor_a_255(self):
        # Caso 2: Un octeto se pasa del limite (300)
        self.assertFalse(es_ip_valida("192.168.300.1"))

    def test_con_letras(self):
        # Caso 3: Contiene caracteres no numericos
        self.assertFalse(es_ip_valida("192.168.1.abc"))

    def test_menos_de_4_partes(self):
        # Caso 4: Solo tiene 3 octetos
        self.assertFalse(es_ip_valida("192.168.1"))

    def test_mas_de_4_partes(self):
        # Caso 5: Tiene 5 octetos
        self.assertFalse(es_ip_valida("192.168.1.1.5"))

if __name__ == '__main__':
    unittest.main()