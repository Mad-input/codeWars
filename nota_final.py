# 3.  Un alumno desea saber cuál será su calificación final en la materia de Matemáticas. Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales (se debe leer cada calificación parcial).
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

notas_parciales = list()

for nota in range(0,3):
    nota = float(input(f'Nota del parcial #{nota + 1}: '))
    notas_parciales.append(nota)
    
promedio_parciales = sum(notas_parciales) / len(notas_parciales)
porcentaje_prom_parciales = promedio_parciales * 0.55

exam_final = float(input('Nota examen final: '))
porcentaje_exam_final = exam_final * 0.3
trab_final = float(input('Nota trabajo final: '))
porcentaje_trab_final = exam_final * 0.15

print(f"""
        Promedio nota parciales: {porcentaje_prom_parciales:.2f}
        Porcentaje examen Final: {porcentaje_exam_final:.2f}
        Porcentaje trabajo Final: {porcentaje_trab_final:.2f}
        
        Nota Final de la Materia de Matemáticas: {(porcentaje_prom_parciales + porcentaje_exam_final + porcentaje_trab_final):.2f}
      """)