/*Se le dará una matriz y un valor límite. Debe comprobar que todos los valores de la matriz estén por debajo o iguales al valor límite. 
Si es así, devuelve verdadero. De lo contrario, devuelve falso.
Puede asumir que todos los valores de la matriz son números.*/

function smallEnough(a, limit) {
  return a.every((c) => c <= limit);
}
