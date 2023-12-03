import unittest
import os
from models.PVModel import PVModel
from utils.GraphGenerator import GraphGenerator

class TestGraphGenerator(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para las pruebas, instanciar las clases necesarias
        self.pv_model = PVModel(1, 1)
        self.graph_generator = GraphGenerator(self.pv_model)
        self.image_path = os.path.abspath('./images')
        if not os.path.exists(self.image_path):
            os.makedirs(self.image_path)

    def test_single_graph(self):
        # Prueba para verificar que la generación de un solo gráfico funciona correctamente
        G = 1000  # Irradiancia en W/m^2
        T = 298   # Temperatura en K
        filename = f"curvas_pv_{G}W_{T-273.15}C.png"
        filepath = os.path.join(self.image_path, filename)

        # Asegurarse de que el archivo no exista antes de la prueba
        if os.path.exists(filepath):
            os.remove(filepath)

        # Llamada al método que podría levantar errores si algo sale mal
        self.graph_generator.single_graph(G, T)

        # Verificar que el archivo se haya creado en el sistema de archivos
        self.assertTrue(os.path.exists(filepath))

        # Opcional: limpiar el archivo después de la prueba
        if os.path.exists(filepath):
            os.remove(filepath)

    # Agregar más pruebas para otros métodos como generate_graphs

# Para ejecutar las pruebas si este archivo se llama directamente
if __name__ == '__main__':
    unittest.main()
