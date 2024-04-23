function sumOfMinimums(arr) {
  let mins = [];
  for (let i = 0; i < arr.length; i++) {
    let min = Math.min(...arr[i]);
    mins.push(min);
  }
  return mins.reduce((a, b) => a + b);
}
