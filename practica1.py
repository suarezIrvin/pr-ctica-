def main():
    texto = input("Ingresa el texto: ")

    # 1. Contar el número total de caracteres en el texto.
    total_caracteres = len(texto)
    print(f"1. Número total de caracteres: {total_caracteres}")

    # 2. Contar el número de caracteres sin incluir espacios.
    caracteres_sin_espacios = len(texto.replace(" ", ""))
    print(f"2. Número de caracteres sin espacios: {caracteres_sin_espacios}")

    # 3. Contar la cantidad de vocales que hay en el texto.
    vocales = "aeiouAEIOU"
    cantidad_vocales = sum(1 for char in texto if char in vocales)
    print(f"3. Cantidad de vocales: {cantidad_vocales}")

    # 4. Contar el número total de palabras en el texto ingresado.
    palabras = texto.split()
    total_palabras = len(palabras)
    print(f"4. Número total de palabras: {total_palabras}")

    # 5. Eliminar la primera palabra.
    if palabras:
        sin_primera_palabra = " ".join(palabras[1:])
        print(f"5. Texto sin la primera palabra: {sin_primera_palabra}")
    else:
        print("5. No hay palabras para eliminar.")

    # 6. Reemplazar todos los espacios por guiones medio (-).
    texto_con_guiones = texto.replace(" ", "-")
    print(f"6. Texto con espacios reemplazados por guiones: {texto_con_guiones}")

    # 7. Cambiar las mayúsculas a minúsculas y las minúsculas a mayúsculas.
    texto_intercambiado = texto.swapcase()
    print(f"7. Texto con mayúsculas y minúsculas intercambiadas: {texto_intercambiado}")

if __name__ == "__main__":
    main()
