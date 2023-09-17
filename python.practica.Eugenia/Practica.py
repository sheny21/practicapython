# Función para calcular el promedio de las notas de un estudiante
def calcular_promedio(notas):
    notas = [float(nota) for nota in notas.split(',')]
    promedio = sum(notas) / len(notas)
    return promedio

# Lista de alumnos y sus notas en formato "nombre|nota1,nota2,nota3"
alumnos = [
    "Juan|80,81,80,90",
    "Paola|97,88,76,77",
    "Marco|98,94,90,91",
]

# Nombre del archivo de salida
nombre_archivo = "promedios.txt"

# Calcular los promedios y guardarlos en el archivo
with open(nombre_archivo, "w") as archivo:
    for alumno in alumnos:
        nombre, notas = alumno.split('|')
        promedio = calcular_promedio(notas)
        archivo.write(f"{nombre}: {promedio:.2f}\n")

print(f"Los promedios se han guardado en {nombre_archivo}")