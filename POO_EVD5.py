"""
Cree una clase llamada Estudiante con los siguientes atributos de instancia: nombre, nota1 y nota2.
Defina un constructor que reciba como parámetros el nombre, la nota1 y la nota2 del estudiante. 
Defina los siguientes métodos de instancia: obtener_nota_promedio() este método devuelve la nota promedio del estudiante y mostrar_informacion() este método muestra en pantalla todos los datos del estudiante (nombre, nota1, nota2 y nota promedio). 
Pruebe el funcionamiento de la clase.
"""

# class Estudiante:
#     def __init__(self,nombre,nota1,nota2):
#         self.nombre = nombre
#         self.nota1 = nota1
#         self.nota2 = nota2
    
#     def obtener_nota_promedio(self):
#         return (self.nota1 + self.nota2) / 2
    
#     def mostrar_informacion(self):
#         return f"""
#         Nombre: {self.nombre}
#         Nota1: {self.nota1}
#         Nota2: {self.nota2}
#         Promedio de notas: {self.obtener_nota_promedio()}
#     """

# estudiante1 = Estudiante('Miguel',3,4)

# print(estudiante1.mostrar_informacion())

"""------------------------------------------------"""

"""
2. Encapsule la clase Estudiante creada en el punto anterior, de tal manera que todos sus atributos de instancia queden privados. 
Agregue los métodos necesarios dentro de la clase para que continúe su funcionamiento y adicionalmente solo acepte notas entre 0 y 5. 
"""

# class Estudiante:
#     def __init__(self, nombre):
#         self.__nombre = nombre
#         self.__nota1 = Estudiante.validar_nota(int(input('Ingresa la nota 1: ')))
#         self.__nota2 = Estudiante.validar_nota(int(input('Ingresa la nota 2: ')))
        
#     @staticmethod
#     def validar_nota(nota):
        
#         if nota < 0 or nota > 5:
#             print('Nota De 0 a 5')
#             return 0
#         else:
#             return nota

#     def obtener_nota_promedio(self):
#         return f"Promedio Nota: {(sum(self.obtener_notas())) / 2}"
    
#     def obtener_nombre(self):
#         return self.__nombre
    
#     def obtener_notas(self):
#         return [self.__nota1,self.__nota2]
    
#     def mostrar_informacion(self):
#         return f"""
#                 Nombre Del Estudiante: {self.obtener_nombre()}
#                 Nota 1: {self.obtener_notas()[0]}
#                 Nota 2: {self.obtener_notas()[1]}
#                 Nota Promedio: {self.obtener_nota_promedio()}"""
        


# estudiante1 = Estudiante('Miguel')

# print(estudiante1)
# print(estudiante1.obtener_nota_promedio())
# print(estudiante1.mostrar_informacion())

"""------------------------------------------------"""

"""
3. A la clase Estudiante del punto anterior realícele las adaptaciones necesarias para que al imprimir un objeto completo de esta clase se presente su nombre y nota promedio.

"""

# class Estudiante:
#     def __init__(self, nombre):
#         self.__nombre = nombre
#         self.__nota1 = Estudiante.validar_nota(int(input('Ingresa la nota 1: ')))
#         self.__nota2 = Estudiante.validar_nota(int(input('Ingresa la nota 2: ')))
#         self.promedio = self.obtener_nota_promedio()

#     def obtener_nota_promedio(self):
#         (sum(self.obtener_notas())) / 2
    
#     def obtener_nombre(self):
#         return self.__nombre
    
#     def obtener_notas(self):
#         return [self.__nota1,self.__nota2]
    
#     def mostrar_informacion(self):
#         return f"""
#                 Nombre Del Estudiante: {self.obtener_nombre()}
#                 Nota 1: {self.obtener_notas()[0]}
#                 Nota 2: {self.obtener_notas()[1]}
#                 Nota Promedio: {self.obtener_nota_promedio()}"""
#     def info(self):
#         print(vars(self))
        


# estudiante1 = Estudiante('Miguel')

# estudiante1.info()

"""------------------------------------------------"""

"""
4. Requerimos que cualquier estudiante creado pertenezca a la misma institución de tal manera que si un estudiante cambia de institución, todos deben hacerlo. Lleve además un control del número de estudiantes de la institución. Realice los ajustes a la clase Estudiante del punto anterior para lograr estos objetivos. 
"""

# class Estudiante:
#     institucion= 'Alguna Institucion'
#     nums_estudiantes = 0
#     def __init__(self):
#         self.__nombre = str(input('ingrese el nombre: '))
#         self.__nota1 = Estudiante.validar_nota(int(input('Ingresa la nota 1: ')))
#         self.__nota2 = Estudiante.validar_nota(int(input('Ingresa la nota 2: ')))
#         self.promedio = self.obtener_nota_promedio()
#         Estudiante.nums_estudiantes +=1

    # @staticmethod
    # def validar_nota(nota):
    #     if nota < 0 or nota > 5:
    #         print('Nota De 0 a 5')
    #         return 0
    #     else:
    #         return nota

#     def obtener_nota_promedio(self):
#         return sum(self.obtener_notas()) / len(self.obtener_notas())
    
#     def obtener_nombre(self):
#         return self.__nombre
    
#     def obtener_notas(self):
#         return [self.__nota1,self.__nota2]
    
#     def mostrar_informacion(self):
#         return f"""
#                 Nombre Del Estudiante: {self.obtener_nombre()}
#                 Institución: {self.institucion}
#                 Nota 1: {self.obtener_notas()[0]}
#                 Nota 2: {self.obtener_notas()[1]}
#                 Nota Promedio: {self.obtener_nota_promedio()}"""
    
#     @classmethod
#     def cambiar_institucion(cls,ins):
#         cls.institucion = ins
#         print(f"algún estudiante a cambiado de institución")
        


# estudiante1 = Estudiante()
# estudiante2 = Estudiante()

# print(estudiante1.mostrar_informacion())
# print(estudiante2.mostrar_informacion())
# print(Estudiante.nums_estudiantes)
# estudiante1.cambiar_institucion('alguna institucion 2')

"""---------------------------------------------------"""

"""
5. Realice el método ver_escala() que al ser invocado en la clase Estudiante presente una tabla con la escala de calificación de todos los estudiantes de la institución. Esta escala es la siguiente: Permita que al invocar al método desde la clase Estudiante.ver_escala() se muestre la tabla anterior. Utilice el módulo tabulate para que la presentación sea la indicada.
"""
from tabulate import tabulate

class Estudiante:
    institucion= 'Alguna Institucion'
    nums_estudiantes = 0
    def __init__(self):
        self.__nombre = str(input('ingrese el nombre: '))
        self.__nota1 = Estudiante.validar_nota(int(input('Ingresa la nota 1: ')))
        self.__nota2 = Estudiante.validar_nota(int(input('Ingresa la nota 2: ')))
        self.promedio = self.obtener_nota_promedio()
        Estudiante.nums_estudiantes +=1

    @staticmethod
    def validar_nota(nota):
        if nota < 0 or nota > 5:
            print('Nota De 0 a 5')
            return 0
        else:
            return nota
        
    @staticmethod
    def ver_escala():
        escala = [
            ['Nota', 'Calificación'],
            ['0 - 1', 'Muy Deficiente'],
            ['1 - 2', 'Insuficiente'],
            ['2 - 3', 'Suficiente'],
            ['3 - 4', 'Bien'],
            ['4 - 5', 'Excelente']
        ]
        print(tabulate(escala, headers='firstrow', tablefmt='fancy_grid'))

    def obtener_nota_promedio(self):
        return sum(self.obtener_notas()) / len(self.obtener_notas())
    
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_notas(self):
        return [self.__nota1,self.__nota2]
    
    def mostrar_informacion(self):
        return f"""
                Nombre Del Estudiante: {self.obtener_nombre()}
                Institución: {self.institucion}
                Nota 1: {self.obtener_notas()[0]}
                Nota 2: {self.obtener_notas()[1]}
                Nota Promedio: {self.obtener_nota_promedio()}"""
    
    @classmethod
    def cambiar_institucion(cls,ins):
        cls.institucion = ins
        print(f"algún estudiante a cambiado de institución")
        


estudiante1 = Estudiante()
estudiante2 = Estudiante()

print(estudiante1.mostrar_informacion())
print(estudiante2.mostrar_informacion())
print(Estudiante.nums_estudiantes)
Estudiante.ver_escala()
estudiante1.cambiar_institucion('alguna institucion 2')


