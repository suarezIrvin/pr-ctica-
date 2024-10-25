import pandas as pd
import numpy as np

# Leer el archivo CSV
data_frame = pd.read_csv(r"C:\Users\Usuario\Downloads\Ciudades_Visitadas_Latinoamerica_2023.csv")

# Mostrar el DataFrame
print("DataFrame:")
print(data_frame)
print("\n" + "="*40 + "\n")

# Funcionalidad 1: Crear y mostrar un array unidimensional
array_unidimensional = np.array([1, 2, 3, 4, 5])
print("Array Unidimensional:")
print(array_unidimensional)
print("\n" + "="*40 + "\n")

# Funcionalidad 2: Sumar dos arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
suma = np.add(array1, array2)
print("Suma de arrays:")
print(suma)
print("\n" + "="*40 + "\n")

# Funcionalidad 3: Calcular la media de un array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
media = np.mean(array)
print("Media del array:")
print(media)
print("\n" + "="*40 + "\n")

# Funcionalidad 4: Cambiar la forma del array a 2x3
array = np.array([1, 2, 3, 4, 5, 6])
array_reshaped = array.reshape(2, 3)
print("Array original:")
print(array)
print("\nArray después de reshape (2x3):")
print(array_reshaped)


# Funcionalidad 5: Acceder al tercer elemento (índice 2) del array
array = np.array([10, 20, 30, 40, 50])
print("Tercer elemento del array:", array[2])
