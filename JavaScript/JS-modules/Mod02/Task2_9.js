const numerolista = [1, 2, 3, 4, 5, 6, 7, 8];

function even(array) {
  let parilliset = [];
  for (let i = 0; i < array.length; i++) {
    if (array[i] % 2 === 0) {
      parilliset.push(array[i]);
    }
  }
  return parilliset;
}

console.log(numerolista);
console.log(even(numerolista));