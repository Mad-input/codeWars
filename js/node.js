// // Array de 50 nombres
// let nombres = [
//   "Juan",
//   "María",
//   "Carlos",
//   "Ana",
//   "Luis",
//   "Laura",
//   "Pedro",
//   "Sofía",
//   "Miguel",
//   "Isabel",
//   "Roberto",
//   "Elena",
//   "Javier",
//   "Carmen",
//   "Diego",
//   "Raquel",
//   "Francisco",
//   "Patricia",
//   "Alejandro",
//   "Lucía",
//   "Gabriel",
//   "Natalia",
//   "Fernando",
//   "Daniela",
//   "Ricardo",
//   "Victoria",
//   "Pablo",
//   "Valeria",
//   "Alberto",
//   "Marta",
//   "Jorge",
//   "Eva",
//   "Oscar",
//   "Beatriz",
//   "Ignacio",
//   "Claudia",
//   "Manuel",
//   "Teresa",
//   "Emilio",
//   "Lorena",
//   "Andrés",
//   "Olga",
//   "Antonio",
//   "Silvia",
//   "Héctor",
//   "Rosa",
//   "Gonzalo",
//   "Verónica",
// ];

// // Array de 50 números telefónicos
// let numerosTelefonicos = [
//   "123456789",
//   "987654321",
//   "555123456",
//   "789012345",
//   "456789012",
//   "321987654",
//   "111222333",
//   "444555666",
//   "777888999",
//   "000111222",
//   "999888777",
//   "666555444",
//   "333222111",
//   "888777666",
//   "555444333",
//   "222111000",
//   "666777888",
//   "111222333",
//   "555666777",
//   "999000111",
//   "444555666",
//   "888999000",
//   "222333444",
//   "666777888",
//   "000111222",
//   "333444555",
//   "777888999",
//   "123456789",
//   "987654321",
//   "555123456",
//   "789012345",
//   "456789012",
//   "321987654",
//   "111222333",
//   "444555666",
//   "777888999",
//   "000111222",
//   "999888777",
//   "666555444",
//   "333222111",
//   "888777666",
//   "555444333",
//   "222111000",
//   "666777888",
//   "111222333",
//   "555666777",
//   "999000111",
//   "444555666",
//   "888999000",
// ];

// // Array de 50 números de dos dígitos
// let numerosDosDigitos = [
//   12, 34, 56, 78, 90, 23, 45, 67, 89, 10, 43, 21, 65, 87, 98, 54, 32, 76, 98,
//   10, 23, 45, 67, 89, 32, 54, 76, 98, 10, 43, 21, 65, 87, 98, 54, 32, 76, 98,
//   10, 23, 45, 67, 89, 32, 54, 76, 98, 10, 43, 21, 65,
// ];

// const In = [];

// for (let i = 0; i < nombres.length; i++) {
//   In.push(
//     `
//     INSERT INTO USERS (name,age,phoneNumber) VALUES ("${nombres[i]}", ${numerosDosDigitos[i]} , ${numerosTelefonicos[i]});
//     `
//   );
// }

// console.log(In.join(""));

// function solution(roman) {
//   const VALUES = {
//     I: 1,
//     V: 5,
//     X: 10,
//     L: 50,
//     C: 100,
//     D: 500,
//     M: 1000,
//   };

//   let count = 0;
//   let chars = roman.split("");

//   for (let i = 0; i < chars.length; i++) {
//     let char = chars[i];
//     char = char.toUpperCase();
//     for (const key in VALUES) {
//       if (char === key) {
//         count += VALUES[char];
//       }
//     }
//     if (char === "I" && chars[i + 1] !== "I") {
//       count -= VALUES[char] - 1;
//     }
//   }

//   return count;
// }

// console.log(solution("CXLVI"));

function findShort(s) {
  let newStr = s.split(" ");
  let min = newStr[0];
  for (let i = 0; i < newStr.length; i++) {
    const len = newStr[i].length;
    if (len < min.length) min = len;
  }
  return min;
}

console.log(findShort("Let's travel abroad shall we"));
