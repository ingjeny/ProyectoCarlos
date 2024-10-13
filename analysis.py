import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def analyze_data():
    data = pd.read_csv('static/housing.csv')

    data.columns = ['Precio', 'Área', 'Habitaciones', 'Baños', 'Pisos', 'Carretera Principal', 'Cuarto de Huéspedes',
                    'Sótano', 'Calefacción Agua', 'Aire Acondicionado', 'Estacionamientos', 'Área Preferencial', 'Mobiliario']

    summary = data.describe()

    summary.index = ['Conteo', 'Media', 'Desviación Estándar', 'Mínimo', '1er Cuartil (25%)', 'Mediana (50%)', '3er Cuartil (75%)', 'Máximo']

    summary['Precio'] = summary['Precio'].apply(lambda x: '{:,.0f}'.format(x))
    summary['Área'] = summary['Área'].apply(lambda x: '{:,.0f}'.format(x))
    summary = summary.round(2)

    plt.figure(figsize=(10, 6))
    plt.hist(data['Precio'], bins=30, color='blue', edgecolor='black')

    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))

    plt.title('Distribución de Precios de Viviendas')
    plt.xlabel('Precio (COP)')
    plt.ylabel('Frecuencia')
    plt.grid(True)

    plt.savefig('static/price_distribution.png')

    return summary.to_html(classes='table table-striped', index=True)
