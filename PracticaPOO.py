from dataclasses import dataclass, field

@dataclass
class Persona:
    nombre: str
    dni: str

@dataclass
class Estudiante(Persona):
    ru: str #registro universitario

    def __hash__(self):
        return int(sha256(self.ru.encode()).hexdigest(), 16)
    
@dataclass
class Docente(Persona):
    sueldo: float
    titular: bool

@dataclass
class Auxiliar(Estudiante):
    sueldo: int
    nro_item: int

@dataclass
class Paralelo:
    sigla: str
    docente: Docente = None #Funcion de Composicion
    auxiliar: Auxiliar | None = None #Funcion de Agregacion >Phython 3.10
    estudiantes: list[Estudiante] = field(default_factory=list) #Se creara una lista de objetos tipo estudiante y el field sera por si no pasa la list[Estudiante]
    notas: list[int] = field(default_factory=list)

@dataclass
class Materia:
    nombre: str
    sigla: str
    paralelos: list[Paralelo] = field(default_factory=list)