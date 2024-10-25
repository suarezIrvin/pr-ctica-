import matplotlib.pyplot as plt
import pandas as pd

# Leer el archivo CSV
data_frame = pd.read_csv(r"C:\Users\Usuario\Downloads\Ciudades_Visitadas_Latinoamerica_2023.csv")

ciudades = data_frame['Ciudad']
visitantes = data_frame['Visitantes']

# Crear gráfico de líneas
plt.plot(ciudades, visitantes, marker='o', linestyle='-', color='b')

# Personalizar el gráfico
plt.title('Visitantes en Ciudades de Latinoamérica (2023)')
plt.xlabel('Ciudades')
plt.ylabel('Número de Visitantes')

# Mostrar gráfico
plt.show()

# Crear gráfico de barras
plt.bar(ciudades, visitantes, color='g')

# Personalizar el gráfico
plt.title('Visitantes en Ciudades de Latinoamérica (2023)')
plt.xlabel('Ciudades')
plt.ylabel('Número de Visitantes')

# Mostrar gráfico
plt.show()

# Crear gráfico de dispersión
plt.scatter(ciudades, visitantes, color='r')

# Personalizar el gráfico
plt.title('Relación de Visitantes por Ciudad')
plt.xlabel('Ciudades')
plt.ylabel('Número de Visitantes')

# Mostrar gráfico
plt.show()

# Gráfico de líneas con personalización
plt.plot(ciudades, visitantes, marker='o', linestyle='-', color='purple')

# Personalización avanzada
plt.title('Visitantes en Ciudades de Latinoamérica (2023)', fontsize=16, color='darkred')
plt.xlabel('Ciudades', fontsize=14)
plt.ylabel('Número de Visitantes', fontsize=14)
plt.grid(True)  # Añadir una cuadrícula
plt.xticks(rotation=45)  # Rotar etiquetas del eje X

# Mostrar gráfico
plt.show()

# Crear gráfico de barras
plt.bar(ciudades, visitantes, color='teal')

# Personalizar gráfico
plt.title('Visitantes en Ciudades de Latinoamérica (2023)')
plt.xlabel('Ciudades')
plt.ylabel('Número de Visitantes')

# Guardar el gráfico en formato PNG y PDF
plt.savefig('grafico_visitas_ciudades.png')
plt.savefig('grafico_visitas_ciudades.pdf')

# Mostrar gráfico
plt.show()

