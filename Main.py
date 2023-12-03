from models.PVModel import PVModel
from utils.GraphGenerator import GraphGenerator

if __name__ == '__main__':
    # Instanciar la clase PVModel
    pv_model = PVModel(1, 1)

    # Instanciar la clase GraphGenerator
    graph_generator = GraphGenerator(pv_model)

    # Generar y guardar gráficos para las condiciones especificadas
    graph_generator.single_graph(1000, 25 + 273.15)  # T=25C, G=1000W/m²
    graph_generator.single_graph(300, 45 + 273.15)  # T=45C, G=300W/m²

    # Instanciar la clase PVModel como un arreglo fotovoltaico con 4 paneles en serie y 3 en paralelo
    pv_model = PVModel(4, 3)

    # Instanciar la clase GraphGenerator con el arreglo fotovoltaico
    graph_generator = GraphGenerator(pv_model)

    # Generar y guardar gráficos para las condiciones especificadas
    graph_generator.generate_graphs()
