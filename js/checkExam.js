/*
*La primera matriz de entrada es la clave para las respuestas correctas de un examen, como ["a", "a", "b", "d"]. 
*El segundo contiene las respuestas enviadas por un estudiante.
*Las dos matrices no están vacías y tienen la misma longitud. 
*Devuelve la puntuación de esta matriz de respuestas, dando +4 por cada respuesta correcta, -1 por cada respuesta incorrecta 
*y +0 por cada respuesta en blanco, representada como una cadena vacía (en C se usa el carácter de espacio).

*Si la puntuación <0, devuelve 0.
*/

function checkExam(array1, array2) {
  let note = 0;
  for (let i = 0; i < array1.length; i++) {
    if (array1[i] === array2[i]) note += 4;
    else if (array2[i] == "") note += 0;
    else note--;
  }
  return note < 0 ? 0 : note;
}

console.log(checkExam(["a", "a", "c", "b"], ["a", "a", "b", ""]));
