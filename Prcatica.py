
from random import random          #random=generacion de numeros aleatorios entre 0 y 1(si multiplicamos por 10 serian de 0 a 10)
import pickle                       #pickle=serializar a archivos binarios
from clases import Estudiante, Docente, Auxiliar, Paralelos, Materia
from collections import defaultdict


def adicionar_materia_a_archivo(materia, filename="materias.dat"):
    #Abrir un archivo para escribir en el
    with open(filename "a+b"): as f:
    #Sintaxis para escribir un objeto a un archivo usando pickle
    pickle.dump(materia, f)
    pass


def estudiante_en_dos_materias(filename="materias.dat"):
    repetidos = defaultdict(int)
    with open(filename, "r+b") as f:
        while True:
            materia: Materia = pickle.load(f)
            for paralelo in materia.paralelos:
                for estudiante in paralelo.estudiantes:
                    repetidos [estudiante] +=1
    pass

# Creacion de Objeto
def main():
    estudiantes = [
        Estudiante(nombre=f"E{i}", dni=f"{i}" * 3, ru=f"{i}" * 4) for i in range(1, 7)
    ]#Esta es una lista por Comprension

    # Creacion de Objeto
    docentes = [
        Docente(
            nombre=f"D{i}", dni=f"{i}", sueldo=round(random() * 10000, 2), titular=True
        )#Esta es una lista por Comprension
        for i in range(8, 11)
    ]

    paralelo_1 = Paralelo(
        sigla="p1", docente=docentes[0], estudiantes=estudiantes[:2], notas=[50, 20]
    )
    paralelo_2 = Paralelo(
        sigla="p2", docente=docentes[1], estudiantes=estudiantes[2:4], notas=[60, 100]
    )
    paralelo_3 = Paralelo(
        sigla="p3",
        docente=docentes[2],
        estudiantes=estudiantes[4:] + [estudiantes[0]],
        notas=[40, 30, 10],
    )

    m1 = Materia(nombre="M1", sigla="M1", paralelos=[paralelo_1, paralelo_2])
    m2 = Materia(nombre="M2", sigla="M2", paralelos=[paralelo_3])

    # Adicionar todas las materias al archivo
    adicionar_materia_a_Archivos(m1)
    adicionar_materia_a_Archivos(m2)
    # Mostrar los estudiantes que están en en ambas materias


if __name__ == "__main__":
    main()