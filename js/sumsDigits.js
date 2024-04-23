function sumDigits(number) {
  let res = String(Math.abs(number))
    .split("")
    .reduce((a, b) => +a + +b, 0);
  return res;
}
