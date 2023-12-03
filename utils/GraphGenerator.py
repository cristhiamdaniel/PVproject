import matplotlib.pyplot as plt
import os

class GraphGenerator:
    def __init__(self, pv_model):
        self.pv_model = pv_model

    def single_graph(self, G, T, image_path='./images'):
        try:
            resultados, V_max, I_max, P_max = self.pv_model.modelo_pv(G, T)

            # Gráficos
            fig, ax1 = plt.subplots()

            color = 'tab:blue'
            ax1.set_xlabel('Voltaje (V)')
            ax1.set_ylabel('Corriente (A)', color=color)
            ax1.plot(resultados['Voltaje (V)'], resultados['Corriente (A)'], color=color)
            ax1.plot(V_max, I_max, 'ro')
            ax1.axvline(x=V_max, color='gray', linestyle='--')  # Línea punteada
            ax1.tick_params(axis='y', labelcolor=color)
            ax1.grid()
            ax1.set_xlim(0, self.pv_model.V_oc)
            ax1.set_ylim(bottom=0)

            ax2 = ax1.twinx()
            color = 'tab:green'
            ax2.set_ylabel('Potencia (W)', color=color)
            ax2.plot(resultados['Voltaje (V)'], resultados['Potencia (W)'], color=color)
            ax2.plot(V_max, P_max, 'ro')
            ax2.tick_params(axis='y', labelcolor=color)
            ax2.set_ylim(bottom=0)

            plt.title('Curvas I-V y P-V')

            # Crear tabla debajo de la gráfica
            data = [['V_max (V)', f'{V_max:.2f} V'],
                    ['I_max (A)', f'{I_max:.2f} A'],
                    ['P_max (W)', f'{P_max:.2f} W']]
            plt.table(cellText=data, loc='bottom', colWidths=[0.2, 0.2])

            # Ajustar la posición de la gráfica para hacer espacio para la tabla
            plt.subplots_adjust(bottom=0.2)

            # Guardar la figura
            plt.tight_layout()
            plt.savefig(os.path.join(image_path, f"curvas_pv_{G}W_{T-273.15}C.png"), dpi=300)
        except Exception as e:
            print(f'Error al generar la gráfica: {e}')


    def generate_graphs(self, image_path='./images'):
        G_values = [300, 500, 700, 1000]
        T_values = [25, 35, 45, 55]

        fig, axs = plt.subplots(2, 2, figsize=(10, 8))

        # Gráficas I-V y P-V para diferentes valores de G a 25° C
        for G in G_values:
            resultados, V_max, I_max, P_max = self.pv_model.modelo_pv(G, 298)
            axs[0, 0].plot(resultados['Voltaje (V)'], resultados['Corriente (A)'], label=f'G={G} W/m²')
            axs[0, 1].plot(resultados['Voltaje (V)'], resultados['Potencia (W)'], label=f'G={G} W/m²')

        # Gráficas I-V y P-V para diferentes valores de T a G=1000
        for T in T_values:
            resultados, V_max, I_max, P_max = self.pv_model.modelo_pv(1000, T + 273.15)
            axs[1, 0].plot(resultados['Voltaje (V)'], resultados['Corriente (A)'], label=f'T={T} °C')
            axs[1, 1].plot(resultados['Voltaje (V)'], resultados['Potencia (W)'], label=f'T={T} °C')

        axs[0, 0].set_xlabel('Voltaje (V)')
        axs[0, 0].set_ylabel('Corriente (A)')
        axs[0, 0].set_title('Curva I-V a 25°C')
        axs[0, 0].legend()
        axs[0, 0].grid(True)
        axs[0, 0].set_ylim(bottom=0)

        axs[0, 1].set_xlabel('Voltaje (V)')
        axs[0, 1].set_ylabel('Potencia (W)')
        axs[0, 1].set_title('Curva P-V a 25°C')
        axs[0, 1].legend()
        axs[0, 1].grid(True)
        axs[0, 1].set_ylim(bottom=0)

        axs[1, 0].set_xlabel('Voltaje (V)')
        axs[1, 0].set_ylabel('Corriente (A)')
        axs[1, 0].set_title('Curva I-V a G=1000 W/m²')
        axs[1, 0].legend()
        axs[1, 0].grid(True)
        axs[1, 0].set_ylim(bottom=0)

        axs[1, 1].set_xlabel('Voltaje (V)')
        axs[1, 1].set_ylabel('Potencia (W)')
        axs[1, 1].set_title('Curva P-V a G=1000 W/m²')
        axs[1, 1].legend()
        axs[1, 1].grid(True)
        axs[1, 1].set_ylim(bottom=0)

        # Guardar la figura
        plt.tight_layout()
        plt.savefig(os.path.join(image_path, 'curvas_pv.png'), dpi=300)
