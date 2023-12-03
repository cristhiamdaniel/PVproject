import unittest
from models.PVModel import PVModel


class TestPVModel(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para las pruebas, instanciar la clase con valores conocidos
        self.pv_model = PVModel(1, 1)

    def test_modelo_pv(self):
        # Prueba del modelo PV bajo condiciones estándar
        G = 1000  # Irradiancia en W/m^2
        T = 298  # Temperatura en K
        resultados, V_max, I_max, P_max = self.pv_model.modelo_pv(G, T)

        # Asegúrate de que los resultados no son None o vacíos
        self.assertIsNotNone(resultados)
        self.assertGreater(len(resultados), 0)

        # Asegúrate de que el punto de máxima potencia es razonable
        self.assertGreater(V_max, 0)
        self.assertGreater(I_max, 0)
        self.assertGreater(P_max, 0)

        # Puedes agregar más aserciones aquí para verificar los valores específicos

    def test_invalid_inputs(self):
        # Prueba para asegurar que se manejan entradas inválidas
        G = -1000  # Valor inválido de Irradiancia
        T = -298  # Valor inválido de Temperatura
        with self.assertRaises(ValueError):
            self.pv_model.modelo_pv(G, T)

        # Añadir más casos de prueba para otros tipos de entradas inválidas


# Para ejecutar las pruebas si este archivo se llama directamente
if __name__ == '__main__':
    unittest.main()
